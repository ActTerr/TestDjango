# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.apps import AppConfig


class OrganizationConfig(AppConfig):
    name = 'organization'
    verbose_name = u"组织管理"