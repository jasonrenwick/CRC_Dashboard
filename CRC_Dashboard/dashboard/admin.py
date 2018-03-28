# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Criterions
from .models import Criteria
from .models import Farmerscores

admin.site.register(Criterions)
admin.site.register(Criteria)
admin.site.register(Farmerscores)

   # Register your models here.
