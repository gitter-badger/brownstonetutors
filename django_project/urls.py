from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import patterns, url, include

from django.views.generic import TemplateView
admin.autodiscover()


urlpatterns = patterns('',
	url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^', include('favicon.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^$', include('BrownstoneTutors.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^invitations/', include('GroupInvitations.urls', namespace='GroupInvitations')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/fullcalendar/', 
    	TemplateView.as_view(template_name="fullcalendar.html"), 
    	name='fullcalendar'),
    url(r'^schedule/', include('SessionSchedule.urls')),
    #url(r'^schedule/', include('schedule.urls')),
)

admin.site.site_header = 'Brownstone Tutors Administration'
admin.site.site_title  = 'Brownstone Tutors Administration'
admin.site.index_title = 'Brownstone Tutors Administration'