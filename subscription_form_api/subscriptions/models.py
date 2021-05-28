from django.db import models
from django.utils.translation import gettext_lazy as _


class Subscription(models.Model):
    """Customer subscription model"""

    TYPES = (
        ('free', _('Free')),
        ('plus', _('Plus')),
        ('pro', _('Pro'))
    )

    name = models.CharField(_('customer name'), max_length=128)
    email = models.EmailField(_('email address'))
    subscription_type = models.CharField(
        _('subscription type'), max_length=8, choices=TYPES, default='free')
