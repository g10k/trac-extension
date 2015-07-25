# -*- encoding: utf-8 -*-
from django.contrib import auth
class AuthRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model and 'sqlite_models' in model.__module__:
            return 'trac_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model and  'sqlite_models' in model.__module__:
            return 'trac_db'
        return None


    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if model and  'sqlite_models' in model.__module__:
            return db == 'trac_db'
        return None
