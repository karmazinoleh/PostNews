from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myauth'

    def ready(self):
        from django.contrib.auth.models import Group
        Group.objects.get_or_create(name='Publisher')