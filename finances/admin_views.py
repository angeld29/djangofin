# -*- coding: utf-8 -*-
'''
Created on 21.08.2011

@author: Angeld
'''
#######################################
#TODO
#-render table template/tags
# -simple text
# -different types
#-filters for table
# -select
# -text
# -date
# -multiselect
# -ajax
#-sort for table
#######################################
from django.contrib.admin.views.main import ChangeList

#from django.template import RequestContext
#from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
#from finances.models import Ticket
#from django.db.models import Sum
class FilterList(object):
  def __init__(self):
    pass
class StatsListView(ListView):
  template = 'finances/stats.html'
  context_object_name="data"
  filters = ('test filter')

  def get_context_data(self, **kwargs):
    context = super(StatsListView, self).get_context_data(**kwargs)
    context['filters'] = self.filters
    return context

  @method_decorator(staff_member_required)
  def dispatch(self, *args, **kwargs):
    return super(StatsListView, self).dispatch(*args, **kwargs)

