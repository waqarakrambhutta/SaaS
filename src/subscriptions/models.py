from django.db import models
from django.contrib.auth.models import Group, Permission

SUBSCRIPTIONS_PERMISSIONS = [
            ("advance", "Advanced Pro Plan"), # subscriptions.advance
            ("pro", "Pro Perm"), # subscriptions.pro
            ("basic", "Basic Perm"), # subscriptions.basic
            ("basic_ai", "Basic AI Perm")
        ]

class Subscription(models.Model):
    name = models.CharField(max_length=120)
    group = models.ManyToManyField(Group)
    permission = models.ManyToManyField(Permission, limit_choices_to={
        'content_type__app_label':'subscriptions',
        'codename__in': [x[0] for x in SUBSCRIPTIONS_PERMISSIONS]
    })

    def __str__(self):
        return self.name
    

    class Meta:
        permissions = SUBSCRIPTIONS_PERMISSIONS