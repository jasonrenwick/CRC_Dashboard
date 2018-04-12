# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import a_Element
from .models import b_Element
from .models import Criteria
from .models import Farmer_a_score
from .models import Farmer_b_score

from .models import Farmer


admin.site.register(a_Element)
admin.site.register(b_Element)

admin.site.register(Criteria)
admin.site.register(Farmer_a_score)
admin.site.register(Farmer_b_score)
admin.site.register(Farmer)


   # Register your models here.
