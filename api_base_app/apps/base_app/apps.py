from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_app'

class CoreConfig(AppConfig):
    name = 'base_app'