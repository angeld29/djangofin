#-*- coding: utf-8 -*- 
#!/usr/bin/env python

#from django.db import models
from django.contrib.admin.filterspecs import FilterSpec, ChoicesFilterSpec
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext as _
from django.contrib.admin.util import get_model_from_relation, \
    reverse_field_path, get_limit_choices_to_from_path

import logging

class FkFilterSpec(ChoicesFilterSpec):
    
    def __init__(self, f, request, params, model, *args, **kwargs):
        super(FkFilterSpec, self).__init__(f, request, params, model, *args, **kwargs)
        
        other_model = get_model_from_relation(f)
        rel_name = other_model._meta.pk.name
        # ******* Extract parameters ********
        the_args = f.fk_filterspec.copy() 
        #The field of the related table
        fk_field = the_args['fk_field'] 
        other_model2 = get_model_from_relation(other_model._meta.get_field(fk_field))
        fk_field_rel_name = other_model2._meta.pk.name
        
        #The name in the related table to use as label in the choices
        label = the_args.pop('label', '')
        
        #the foreign key field. By default the field the filter is assigned
        fk = the_args.pop('fk', f.name) 
        
        # ******* Build the filter definition ********
        
        self.lookup_kwarg_fk = '{0}__{1}__{2}__exact'.format(fk, fk_field, fk_field_rel_name )
        self.lookup_kwarg = '{0}__{1}__exact'.format(fk,rel_name) #self.lookup_kwarg_fk,
        self.lookup_val = request.GET.get(self.lookup_kwarg, None)
        self.lookup_val_fk = request.GET.get(self.lookup_kwarg_fk, None)
             
        self.lookup_labels = {}
        #get the list of values
#        if label:
#            label_field = '{0}__{1}'.format(fk, label)
#        else:
#            label_field = '{0}'.format(fk)
        #filter_field = '{0}__{1}'.format(fk, fk_field)
        #values_list = model.objects.filter().values_list(fk,label_field)
        #values_list = model.objects.select_related(fk).filter(**{filter_field:self.lookup_val_fk }).values_list(fk,label_field)
        
        values_list = other_model.objects.select_related().filter(**{fk_field:self.lookup_val_fk }).values_list(fk_field_rel_name,label)
        #if self.lookup_val:
        for (v, l) in values_list:
            self.lookup_labels[v] = l
        if self.lookup_val:
            values_list = other_model.objects.filter(**{rel_name:self.lookup_val }).values_list(fk_field_rel_name,label)
            for (v, l) in values_list:
                self.lookup_labels[v] = l
        self.lookup_choices =self.lookup_labels.keys() 
         
        #
        
#        logging.debug(self.lookup_val_fk) 
#        logging.debug(self.lookup_val)
#        logging.debug(fk)
#        logging.debug(fk_field)
#        logging.debug(values_list)
#        logging.debug(self.lookup_choices)
        
    def choices(self, cl):
        yield {'selected': self.lookup_val is None,
               'query_string': cl.get_query_string({}, [self.lookup_kwarg]),
               'display': _('All')}
        for val in self.lookup_choices:
            yield {'selected': smart_unicode(val) == self.lookup_val,
                    'query_string': cl.get_query_string({self.lookup_kwarg: val}),
                    'display': smart_unicode(self.lookup_labels[val])}
    
    def has_output(self):
        return len(self.lookup_choices) > 0
    @classmethod
    def register_filterspec(cls):
        """register the filter. To be called in the models.py"""
        FilterSpec.filter_specs.insert(0,
            (lambda f: len(getattr(f, 'fk_filterspec', [])), cls)
        )

#FilterSpec.filter_specs.insert(0,(lambda f: len(getattr(f, 'fk_filterspec', [])), FkFilterSpec))
