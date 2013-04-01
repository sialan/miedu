from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    # Default url
     url(r'^$', 'home.views.home_view.index', name='home'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^team/$', TemplateView.as_view(template_name="team.html"), name='team'),
    url(r'^terms/$', TemplateView.as_view(template_name="terms.html"), name='terms'),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name='contact'),
    url(r'^tutorial/$', TemplateView.as_view(template_name="tutorial.html"), name='tutorial'),

    # Site tutorial info    
    url(r'^tutorial/build', TemplateView.as_view(template_name="build.html"), name='tut-build'),
    url(r'^tutorial/campaign', TemplateView.as_view(template_name="run.html"), name='tut-campaign'),
    url(r'^tutorial/advanced', TemplateView.as_view(template_name="advanced.html"), name='tut-advanced'),

    # Blogs and Event info
    #url(r'^blog', 'blogs.views.blog_view.blog', name='blog'),
    # TODO: capture payment url string
    url(r'^blog/(?P<post_id>\d+)', 'blogs.views.post_view.post', name='blog-post'),

    # Learning resources
    url(r'^learn', 'plans.views.plan_view.plan', name='learn'),
    url(r'^learn/(?P<article_id>\d+)', 'articles.views.article_view.article', name='tutorial'),
    #url(r'^learn/(?P<lesson_id>\d+)', 'lessons.views.lesson_view', name='lesson'),
    #url(r'^learn/(?P<lesson_id>\d+)/(?P<article_id>\d+)', 'articles.views.article_view', name='tutorial'),

    # Accounts info pages and registration
    url(r'^registration', 'accounts.views.registration_view.registration', name='registration'),
    url(r'^login/$', 'accounts.views.login_view.login', name='login'),
    url(r'^logout/$', 'accounts.views.logout_view.logout', name='logout'),
    #url(r'^account/(?P<account_id>\d+)', 'accounts.views.account_view.profile', name='account'),

    # Campaigns
    url(r'^campaign/browse/$', 'campaigns.views.campaign_list_view.campaigns', name='campaign-list'),
    #url(r'^campaign/new', 'campaigns.views.campaign_new_view', name='campaign-new'),
    #url(r'^campaign/(?P<campaign_id>\d+)', 'campaigns.views.campaign_detail_view', name='campaign-detail'),
    #url(r'^campaign/(?P<campaign_id>\d+)/edit', 'campaigns.views.campaign_edit_view', name='campaign-edit'),

    # Enabling the admin and accompanying documentation:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'', include('social_auth.urls')),

)

"""
# Create your views here.
# Basic contact info and static corporate info


    url(r'^account/(?P<account_id>\d+)/edit', 'accounts.views.profile_view', name='profile'),
    
    #url(r'^campaign/browse$', 'campaigns.views.campaign_list_walkthrough_view', name='campaign-list-walkthrough'),
    # url(r'^campaign/(?P<campaign_id>\d+)/projects', 'projects.views.project_list_view', name='project-list'),
    # url(r'^campaign/(?P<campaign_id>\d+)/projects/(?P<project_id>\d+)', 'projects.views.project_detail_view', name='project-detail'),

    # Payment history for registered users
    url(r'^account/(?P<account_id>\d+)/payments', 'transactions.views.history_view', name='payment-history'),
    # TODO: capture payment url string
    url(r'^account/(?P<account_id>\d+)/payments/(?P<transaction_id>\d+)', 'transactions.views.payment_view', name='payment'),
"""
    