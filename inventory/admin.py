# coding: utf-8
from django.forms import TextInput, Textarea
from django.db import models
from django.contrib import admin

from inventory.models import TestSystem, Tool,MiscItem

class InventoryModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    search_fields = ['name', 'code']

    def get_search_results(self, request, queryset, search_term):
    	
    	q1, use_distinct = super(
    		InventoryModelAdmin, self).get_search_results(
    			request,
    			queryset,
    			search_term.lower()
    		)

    	if search_term:
    		s2 = search_term.lower()[0].upper() + search_term.lower()[1:]
    	else:
    		s2 = ''	
    	q2, use_distinct = super(
    		InventoryModelAdmin, self).get_search_results(
    			request,
    			queryset,
    			s2
    		)

    	queryset = (q1.all() | q2.all()).distinct()

    	return queryset, use_distinct

class EquipmentAdmin(InventoryModelAdmin):

    def status(self, obj):
        if obj.test_status() == 'RED':
            return '''
                    <div style="width:30px;
                            height:30px;
                            border-radius: 30px;
                            background-color:#ea7456;">
                    </div>
                    '''
        elif obj.test_status() == 'YELLOW':
            return '''
                    <div style="width:30px;
                            height:30px;
                            border-radius: 30px;
                            background-color:#f4ef6d;">
                    </div>
                    '''
        else:
            return '''
                    <div style="width:30px;
                            height:30px;
                            border-radius: 30px;
                            background-color:#59c559;">
                    </div>
                    '''
    
    status.allow_tags = True
    status.short_description = ''

    list_display = ('name', 'next_test_date', 'status')


# Register your models here.

admin.site.register(TestSystem, EquipmentAdmin)
admin.site.register(Tool, EquipmentAdmin)
admin.site.register(MiscItem, InventoryModelAdmin)

