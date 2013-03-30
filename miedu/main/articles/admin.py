from django.contrib import admin
from articles.models import Article, ArticleComment
from projects.models import Project


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
    inlines = [ArticleCommentInline]
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
                    ('tags', 'url'),
                    )
                }
        ),
    )
    list_display = ('title', 'created_on', 'last_edited', 'heading',)
    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', 'js/libs/tiny_mce/tinymce_setup.js',)

admin.site.register(Article, ArticleAdmin)