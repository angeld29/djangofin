from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.db.models.aggregates import Sum
from finances.admin_views import StatsListView
from finances.models import Ticket

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'djtut14.views.home', name='home'),
  # url(r'^djtut14/', include('djtut14.foo.urls')),

  (r'^admin/finances/stats/$',  StatsListView.as_view(
    queryset=Ticket.objects.values('good__article').annotate(sumtotal=Sum('total')).values('sumtotal','good__article__label'),
    context_object_name="data",
    template_name = 'finances/stats.html',
    filters = ('test2'),
  )),
  url(r'^admin_tools/', include('admin_tools.urls')),
  # Uncomment the admin/doc line below to enable admin documentation:
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
)
