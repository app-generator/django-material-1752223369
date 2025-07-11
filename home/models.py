# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Sensor Data(models.Model):

    #__Sensor Data_FIELDS__
    temperature = models.IntegerField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    gas concentration = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True, default=timezone.now)
    device id = models.ForeignKey(Device, on_delete=models.CASCADE)

    #__Sensor Data_FIELDS__END

    class Meta:
        verbose_name        = _("Sensor Data")
        verbose_name_plural = _("Sensor Data")


class Device(models.Model):

    #__Device_FIELDS__
    device id = models.CharField(max_length=255, null=True, blank=True)
    device name = models.CharField(max_length=255, null=True, blank=True)
    device description = models.CharField(max_length=255, null=True, blank=True)
    device status = models.CharField(max_length=255, null=True, blank=True)
    ip address = models.CharField(max_length=255, null=True, blank=True)
    mac address = models.CharField(max_length=255, null=True, blank=True)
    added at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Device_FIELDS__END

    class Meta:
        verbose_name        = _("Device")
        verbose_name_plural = _("Device")


class Wireless Log(models.Model):

    #__Wireless Log_FIELDS__
    log text = models.TextField(max_length=255, null=True, blank=True)
    device id = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Wireless Log_FIELDS__END

    class Meta:
        verbose_name        = _("Wireless Log")
        verbose_name_plural = _("Wireless Log")



#__MODELS__END
