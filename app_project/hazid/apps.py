from django.apps import AppConfig

class HazidConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hazid'

    def ready(self):
        import hazid.signals
