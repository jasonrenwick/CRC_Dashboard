# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Element
from .models import Criteria
from .models import Farmerscore
from .models import Farmer

admin.site.register(Element)
admin.site.register(Criteria)
admin.site.register(Farmerscore)
admin.site.register(Farmer)

   # Register your models here.
