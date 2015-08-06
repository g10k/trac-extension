# coding: utf-8
import re

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class RequireLoginMiddleware(object):
    """
    Middleware component that wraps the login_required decorator around 
    matching URL patterns. To use, add the class to MIDDLEWARE_CLASSES and 
    define LOGIN_REQUIRED_URLS and LOGIN_REQUIRED_URLS_EXCEPTIONS in your 
    settings.py. For example:
    ------
    LOGIN_REQUIRED_URLS = (
        r'/topsecret/(.*)$',
    )
    LOGIN_REQUIRED_URLS_EXCEPTIONS = (
        r'/topsecret/login(.*)$', 
        r'/topsecret/logout(.*)$',
    )

    LOGIN_REQUIRED_URLS_PERMS = {
        r'/crm/(.*)$': ('crm.have_access', 'crm.models', 'CrmUser'),    # модуль и класс, у которого определен метод 
                                                                        #   @classmethod 
                                                                        #   def get_user(cls, username): ...
                                                                        # и метод объекта 
                                                                        #   def has_perm(self, perm_name): ...
                                                                        # принимающий в качестве perm_name 'crm.have_access'
    }
    ------                 
    LOGIN_REQUIRED_URLS is where you define URL patterns; each pattern must 
    be a valid regex.     

    LOGIN_REQUIRED_URLS_EXCEPTIONS is, conversely, where you explicitly 
    define any exceptions (like login and logout URLs).
    """
    def __init__(self):
        self.required = tuple([re.compile(url) for url in settings.LOGIN_REQUIRED_URLS])
        self.exceptions = tuple([re.compile(url) for url in settings.LOGIN_REQUIRED_URLS_EXCEPTIONS])

        # дополнение по правам на урлы
        try:
            self.required_perm = dict([(re.compile(url), perm) for url, perm in settings.LOGIN_REQUIRED_URLS_PERMS.items()])
        except AttributeError:
            self.required_perm = {}
        # куда редиректим в случае ограничения прав
        try:
            self.access_deny = dict([(re.compile(url), perm) for url, perm in settings.LOGIN_REQUIRED_URLS_ACCESS_DENY.items()])
        except AttributeError:
            self.access_deny = {}
 
            

    def process_view(self,request,view_func,view_args,view_kwargs):
        # An exception match should immediately return None
        for url in self.exceptions:
            if url.match(request.path): return None
        
        if request.user.is_authenticated(): 
            
            # проверим, что текущая страница - не одна из страниц с уведомлением об ограничении прав
            if not request.user.is_superuser and request.path not in self.access_deny.values():
                # проверим есть ли условия по правам на урл
                for url in self.required_perm:
                    # если у пользователя нет прав на урл
                    if url.match(request.path): 
                        perm, module_str, user_class_str = self.required_perm[url]
                        # импортируем модуль с классом пользователя
                        mod = __import__(module_str)
                        components = module_str.split('.')
                        for comp in components[1:]:
                            mod = getattr(mod, comp)
                        # класс пользователя
                        user_class = getattr(mod, user_class_str)
                        # объект пользователя
                        user = user_class.get_user(request.user.username)
                        if not user or not user.has_perm(perm):
                            # перенаправим его в соответствии  с настройками
                            for url in self.access_deny:
                                if url.match(request.path):
                                    return redirect(self.access_deny[url])
                            
            

            # No need to process URLs if user already logged in
            return None
        # Requests matching a restricted URL pattern are returned 
        # wrapped with the login_required decorator
        for url in self.required:
            if url.match(request.path):
                if settings.LOGIN_URL:
                    login_url = settings.LOGIN_URL
                else:
                    # если не задан url для логина, то получим начало пути из request.path
                    # например portal или crm
                    login_url = '/' + request.path.split('/')[1] +'/login/'
                    
                return login_required(view_func, login_url=login_url)(request,*view_args,**view_kwargs)
        # Explicitly return None for all non-matching requests
        return None
