__author__ = 'markrop'

from django.contrib import admin

from polls.models import Poll

admin.site.register(Poll)
