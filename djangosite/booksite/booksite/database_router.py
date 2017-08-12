from django.conf import settings

DATABASES_MAPPING = settings.DATABASE_APPS_MAPPING

class DatabaseAppsRouter(object):
    def db_for_read(self,model,**hints):
        if model._meta.app_label in DATABASES_MAPPING:
            return DATABASES_MAPPING[model.meta.app_label]
        return None

    def db_for_write(self,model,**hints):
        if model._meta.app_label in DATABASES_MAPPING:
            return DATABASES_MAPPING[model.meta.app_label]
        return None

    def allow_relation(self,obj1,obj2,**hints):
        db_obj1 = DATABASES_MAPPING.get[obj1._meta.app_label]
        db_obj2 = DATABASES_MAPPING.get[obj2._meta.app_label]
        if db_obj1 and db_obj2:
            return True
        else:
            return False
        return None

    def allow_migrate(self,db,app_label,model_name = None,**hints):
        print db,app_label,model_name,hints
        if db in DATABASES_MAPPING.values():
            return DATABASES_MAPPING.get(app_label) == db
        elif app_label in  DATABASES_MAPPING:
            return False
        return None
