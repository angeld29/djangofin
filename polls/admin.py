# -*- coding: utf-8 -*-

from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class PollAdmin(admin.ModelAdmin):
#  fields = ['pub_date', 'question']
  date_hierarchy = 'pub_date'
  search_fields = ['question']
  list_filter = ['pub_date']
  list_display = ('question', 'pub_date')
  fieldsets = [
    (None,               {'fields': ['question']}),
    ('Date information', {'fields': ['pub_date']}),
  ]
  inlines = [ChoiceInline]

#admin.site.register(Choice)
admin.site.register(Poll, PollAdmin)
