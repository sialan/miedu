from django.contrib import admin
from lessons.models import Lesson, LessonArticle, LessonComment, LessonFAQItem
from projects.models import Project


class LessonArticleInline(admin.StackedInline):
    model = LessonArticle
    max_num = 5
    extra = 1
    readonly_fields = (
    )

    fieldsets = (
        ('Additional Content Blocks', {
            'classes': ('collapse',),
            'fields': (
                ('article', 'suggested_order', 'importance'),
                'instructions',
                'rationale',
                'tags',
            )                
        }),
    )

class LessonCommentInline(admin.TabularInline):
    model = LessonComment
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

class FAQInline(admin.TabularInline):
    model = LessonFAQItem
    max_num = 5
    extra = 1
    fieldsets = (
        ('FAQ', {
            'classes': ('collapse',),
            'fields': (
                'question',
                'answer',
            )                
        }),
    )

class LessonAdmin(admin.ModelAdmin):
    inlines = [LessonArticleInline, LessonCommentInline, FAQInline]
    readonly_fields = (
        'last_edited',
    )
    fieldsets = (
        (None, {'fields': ( 
        			('title', 'course_number', 'course_code'),
                    ('organization', 'last_edited', 'course_staff'),
                    ('partner_name', 'partner_url', 'partner_dp'),
                    ('credit_name', 'credit_value', 'image', 'video_intro'),
                    'about',
                    'prerequisites',
                    'objectives',
                    ('effort_value', 'effort_units'),
                    ('resources', 'tags'),
                    )
                }
        ),
    )
    list_display = ('title', 'last_edited',)

admin.site.register(Lesson, LessonAdmin)