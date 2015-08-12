# -*- encoding: utf-8 -*-
class AuthRouter(object):
    """
    Router для контроля за использованием баз данных
    """
    def db_for_read(self, model, **hints):
        """
        для моделей trac используем sqlite БД
        """
        if model and 'trac_models' in model.__module__:
            return 'trac_db'
        return None

    def db_for_write(self, model, **hints):
        """
        для моделей trac используем sqlite БД
        """
        if model and  'trac_models' in model.__module__:
            return 'trac_db'
        return None


    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        для моделей trac используем sqlite БД
        """
        if model and  'trac_models' in model.__module__:
            return db == 'trac_db'
        return None
