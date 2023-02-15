from django.db import models # noqa
from django.utils.translation import gettext as _


# Create your models here.
class Mapping(models.Model):
    name = models.CharField(_('name'), max_length=100)
    latitude = models.CharField(_('latitude'), max_length=64)
    longitude = models.CharField(_('longitude'), max_length=64)
    expiration_date = models.DateField(_('data_de_expiração'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = (_('Mapping'))
        verbose_name_plural = (_('Mappings'))
