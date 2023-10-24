from django.contrib import admin

from .models import Census


class CensusAdmin(admin.ModelAdmin):
    list_display = ('voting_id', 'voter_id')
    # list_display = ('voting_id', 'voter_id','adscription')
    list_filter = ('voting_id', )
    # list_filter = ('voting_id', 'adscription' )
    search_fields = ('voter_id', )
    
    # def adscription(self, obj):
    #     return obj.adscription

admin.site.register(Census, CensusAdmin)
