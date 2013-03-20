from django.contrib import admin
from projects.models import Project
from multimedia.models import Multimedia
from accounts.models import Account

"""
class MultimediaInline(admin.TabularInline):
    model = Multimedia
    max_num = 5
    extra = 1
    readonly_fields = (
        'uploaded_on',
    )

    fieldsets = (
        ('Related Multimedia', {
            'classes': ('collapse',),
            'fields': (
                ('uploaded_by', 'uploaded_on'),
                'title',
                'tags',
            )                
        }),
    )

class BackerInline(admin.TabularInline):
    model = Account
    max_num = 5
    extra = 1
    readonly_fields = (
    )

    fieldsets = (
        ('Backers of this Project', {
            'classes': ('collapse',),
            'fields': (
                'username',
            )                
        }),
    )
"""

class ProjectAdmin(admin.ModelAdmin):
    search_fields = ["campaign", "title"]
    readonly_fields = ("created_on",)
    fieldsets = (
        (None, {'fields': ( 
                    ('campaign', 'title'),
                    'headline',
                    'description',
                    'call_to_action',
                    ('ranking', 'main'),
                    'dp_url',
                    ('created_on', 'delivery_date'),
                    ('funding_amount', 'number_available', 'number_claimed'),
                    'backers',
                    'multimedia_updates',
                    )
                }
        ),
    )

    list_display = ('campaign', 'title', 'main', 'created_on',)

admin.site.register(Project, ProjectAdmin)