from django.contrib import admin
from plans.models import Plan, LessonPlan


class LessonPlanInline(admin.StackedInline):
    model = LessonPlan
    max_num = 5
    extra = 1
    readonly_fields = (
    )

    fieldsets = (
        ('Lesson Plan', {
            'classes': ('collapse',),
            'fields': (
                'lessons',
                ('suggested_order', 'importance'),
                'instructions',
                'rationale',
                'tags',
            )                
        }),
    )

class PlanAdmin(admin.ModelAdmin):
    inlines = [LessonPlanInline]
    readonly_fields = (
        'last_edited',
    )
    fieldsets = (
        (None, {'fields': ( 
                    ('category', 'subcategory', 'level'),
                    'title',
                    'description',
                    ('goal', 'last_edited'),
                    'tags',
                    )
                }
        ),
    )
    list_display = ('category', 'subcategory', 'title',)

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', 'js/libs/tiny_mce/tinymce_setup.js',)

admin.site.register(Plan, PlanAdmin)