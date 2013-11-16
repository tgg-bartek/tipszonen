from django.contrib import admin 

from .models import Pick, ExpertCategory


class PickAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': (('matchup', 'slug', 'match_date'),  
                               ('odds', 'stake', 'bookmaker'), 
                                'selection', 'analysis', 'expert', 'published')
                }
        ),
        ('Postmatch info',  {'fields':['match_score', 'pick_outcome']}),
    ]
    list_display = ('published', 'matchup', 'match_date')
    list_display_links = ('matchup',)
    list_editable = ('published',)
    list_filter = ('published', 'created_at', 'expert')
    prepopulated_fields = {'slug': ('matchup',)}
    search_fields = ('matchup', 'analysis')

class ExpertCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Pick, PickAdmin)
admin.site.register(ExpertCategory, ExpertCategoryAdmin)