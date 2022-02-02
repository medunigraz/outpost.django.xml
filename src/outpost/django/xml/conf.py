import os

from appconf import AppConf
from django.conf import settings


class XMLAppConf(AppConf):

    class Meta:
        prefix = "xml"
