from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    
def ready(self):
        # Import the templatetags here to ensure they load
        import home.templatetags.custom_filters   
