# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Income(models.Model):
#    id = models.IntegerField()
#    id_user = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User)
    amount = models.DecimalField(null=True, max_digits=17, decimal_places=2, blank=True)
    dt = models.DateField(null=True, blank=True)

class Article(models.Model):
    label = models.CharField(max_length=128, blank=True)
    def __unicode__(self):
        return self.label    

class Good(models.Model):
    label = models.CharField(max_length=128, blank=True, )
    article = models.ForeignKey(Article, verbose_name='категория')
    def __unicode__(self):
        return u'%s' % (self.label)


class Ticket(models.Model):
    user = models.ForeignKey(User, verbose_name='кто')
    dt = models.DateField(null=True, blank=True, verbose_name='дата')
    total = models.DecimalField(null=True, max_digits=17, decimal_places=2, blank=True, verbose_name='сумма')
    #article = models.ForeignKey(Article, verbose_name='статья расходов')
    good = models.ForeignKey(Good, verbose_name='товар/услуга')
    good.custom_filter_spec = True
    good.fk_filterspec = {'fk_field':'article', 
                          'label':'label', 
                          'title':'товар/услуга'}    
    comment = models.CharField('коментарий', max_length=765, blank=True)
    def article(self):
       return self.good.article
    
    class Meta:
        verbose_name = "чек"
        verbose_name_plural = "чеки"

#from filterspecs import FkFilterSpec
#FkFilterSpec.register_filterspec()
