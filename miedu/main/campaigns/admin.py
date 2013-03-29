from django.contrib import admin
from campaigns.models import Campaign, CampaignMilestone, CampaignComment, CampaignFAQItem
from projects.models import Project


class CampaignMilestoneInline(admin.StackedInline):
    model = CampaignMilestone
    max_num = 5
    extra = 1
    readonly_fields = (
    )

    fieldsets = (
        ('Additional Content Blocks', {
            'classes': ('collapse',),
            'fields': (
                ('subheading', 'media'),
                'completed',
                'body',
                ('milestone_date', 'completed'),
            )                
        }),
    )

class CampaignCommentInline(admin.TabularInline):
    model = CampaignComment
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
    model = CampaignFAQItem
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

class ProjectInline(admin.StackedInline):
    model = Project
    max_num = 5
    extra = 1
    readonly_fields = (
        'created_on',
    )

    fieldsets = (
        ('Campaign Projects', {
            'classes': ('collapse',),
            'fields': (
                ('title', 'headline'),
                'description',
                ('call_to_action', 'ranking', 'main', 'dp_url'),
                ('created_on', 'delivery_date'),
                ('funding_amount', 'number_available', 'number_claimed'),
            )                
        }),
    )

class CampaignAdmin(admin.ModelAdmin):
    inlines = [CampaignMilestoneInline, CampaignCommentInline, FAQInline, ProjectInline]
    readonly_fields = (
        'created_on',
    )
    fieldsets = (
        (None, {'fields': ( 
        			('account'),
                    ('active', 'completed', 'consummated'),
                    ('currently_featured', 'feature_score'),
                    ('minimum_pledge', 'amount_pledged', 'goal'),
                    ('created_on', 'number_backers'),
                    ('start_date', 'end_date', 'completion_date'),
                    ('city', 'state', 'country'),
                    'tags',
                    'title',
                    'caption',
                    'headline',
                    'description',
                    'endline',
                    'summary',
                    'call_to_action',
                    'multimedia',
                    'backers',
                    )
                }
        ),
    )
    list_display = ('account', 'active', 'amount_pledged', 'goal', 'created_on',)

admin.site.register(Campaign, CampaignAdmin)