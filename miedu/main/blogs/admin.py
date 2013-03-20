from django.contrib import admin
from blogs.models import Post, BlogComment

class CommentInline(admin.TabularInline):
    model = BlogComment
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

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    search_fields = ["title"]
    readonly_fields = ("created",)
    fieldsets = (
        (None, {'fields': ( 
        			('title', 'author', 'created'),
                    ('category', 'subcategory'),
                    ('photo', 'link'),
                    'tagline',
                    'body',
                    'tags',
                    )
                }
        ),
    )

admin.site.register(Post, PostAdmin)