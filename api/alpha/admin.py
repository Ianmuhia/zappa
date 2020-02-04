# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Notification, Student


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)
    def get_search_results(self, request, queryset, search_term):
        queryset = super().get_search_results(request, queryset, search_term)
        return queryset
        
admin.site.register(Post, PostAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    search_fields = ('title', 'text')
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        return queryset, use_distinct
admin.site.register(Notification, NotificationAdmin)
  
class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'first_name', 'sir_name', 'course')
    # search_fields = ('registration_number',)
    # def get_search_results(self, request, queryset, search_term):
    #     queryset, use_distinct = super().get_search_results(request, queryset, search_term)
    #     try:
    #         search_term_as_int = int(search_term)
    #     except ValueError:
    #         pass
    #     else:
    #         queryset |= self.model.objects.filter(registraion_number=search_term_as_int)
    #         return queryset, use_distinct
admin.site.register(Student, StudentAdmin)