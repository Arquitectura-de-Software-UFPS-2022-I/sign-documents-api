from django.apps import AppConfig


class ValidateSignatureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'validate_signature'

class CoreConfig(AppConfig):
    name = 'validate_signature'
