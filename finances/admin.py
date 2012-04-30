# -*- coding: utf-8 -*-
'''
Created on 21.08.2011

@author: Angeld
'''
from django.contrib import admin
#from django.forms.models import *
from django.conf import settings
from models import *
from django import forms
from django.forms import TextInput, Textarea
#from ajax_filtered_fields.forms import ForeignKeyByRelatedField, ManyToManyByRelatedField, AjaxForeignKeyField, ForeignKeyByLetter


class TicketAdminForm(forms.ModelForm):
    #good = ForeignKeyByRelatedField(Good, "article")
    comment = forms.CharField(widget=TextInput(attrs={'size':'200'}))
    class Media:
        js = (
#            settings.ADMIN_MEDIA_PREFIX + "js/SelectBox.js",
#            settings.ADMIN_MEDIA_PREFIX + "js/SelectFilter2.js",
            '/static/admin_tools/js/jquery/jquery.min.js',
            '/static/js/ajax_filtered_fields.js',
        )    
    class Meta:
        model = Ticket
        
class TicketAdmin(admin.ModelAdmin):
    form = TicketAdminForm
        
    #fields = ('dt', 'user','total', 'article','good', 'comment' )
    #comment = forms.CharField(widget=forms.TextInput(attrs={'size':'140'}))
    #comment = forms.CharField(max_length=10)
    #comment = forms.Textarea();
    #comment = forms.URLField(initial='http://')
    #good=ForeignKeyByLetter(Article, field_name="label")
    list_select_related = True
    list_display = ('dt', 'total','good', 'article', 'user')
    #list_display_links = ('good',  'user')
    list_filter = ( 'dt', 'user', 'good__article', 'good')
    date_hierarchy = 'dt'
    ordering = ('-dt',)
#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#       if db_field.name == 'article':
#            kwargs['queryset'] = Article.objects.exclude(area=None)    
    raw_id_fields = ('good',)
    #filter_horizontal = ('article',)
#class TicketInlineFormset(models.BaseInlineFormSet):
#    def add_fields(self, form, index):
#        super(TicketInlineFormset, self).add_fields(form, index)
#        
#        if form.instance:
#            try:        
#                article = form.instance.article    
#            except Article.DoesNotExist:
#                pass   
#            else:  
#                good = Good.objects.filter(article=article)
#        form.fields['good'].queryset = good
#        
#class TicketInfoInline(admin.TabularInline):
#    model = Ticket
#    formset = TicketInlineFormset

class GoodInline(admin.TabularInline):
    model = Good
    #max_num = 3
    label = forms.CharField(max_length=200)
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None,               {'fields': ['label']}),
    #             ('РўРѕРІР°СЂС‹', {'inlines' : [GoodInline]}),
    ]
    inlines = [GoodInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'200'})},
        #models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }    
    #list_display = ('label', 'article')
    #list_filter = ('article',)
    #ordering = ('article',)

class GoodAdmin(admin.ModelAdmin):
    #inlines = [TicketInfoInline]
    list_display = ('label', 'article')
    list_filter = ('article',)
    ordering = ('article',)
    
#class AuthorAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'email')
#    search_fields = ('first_name', 'last_name')
#
#class BookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'publisher', 'publication_date')
#    list_filter = ('publication_date',)
#    date_hierarchy = 'publication_date'
#    ordering = ('-publication_date',)
#    filter_horizontal = ('authors',)

admin.site.register(Income)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Ticket, TicketAdmin)

