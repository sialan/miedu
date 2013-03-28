from django.contrib import admin
from articles.models import Article, Tab, ArticleComment
from projects.models import Project


class TabInline(admin.StackedInline):
    model = Tab
    max_num = 5
    extra = 1
    readonly_fields = (
    )

    fieldsets = (
        ('Additional Content Blocks', {
            'classes': ('collapse',),
            'fields': (
                ('subheading', 'style'),
                'body',
                ('media_resource', 'caption'),
                'field_one',
                'field_two',
                'field_three',
            )                
        }),
    )

class ArticleCommentInline(admin.TabularInline):
    model = ArticleComment
    max_num = 5
    extra = 1
    readonly_fields = (
        'created',
    )

    fieldsets = (
        ('Comments', {
            'classes': ('collapse',),
            'fields': (
                ('author', 'created'),
                'heading',
                'body',
            )                
        }),
    )

class ArticleAdmin(admin.ModelAdmin):
    inlines = [TabInline, ArticleCommentInline]
    readonly_fields = (
        'created_on',
        'last_edited',
    )
    fieldsets = (
        (None, {'fields': ( 
        			'title',
                    ('created_on', 'last_edited', 'main'),
                    ('created_by', 'moderators'),
                    'heading',
                    'body',
                    'resources',
                    'endline',
                    'summation',
                    'tags',
                    )
                }
        ),
    )
    list_display = ('title', 'created_on', 'last_edited', 'heading',)

admin.site.register(Article, ArticleAdmin)