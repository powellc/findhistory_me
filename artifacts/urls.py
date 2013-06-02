from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from .views import OrganizationDetailView, OrganizationListView, ArtifactDetailView, \
                   ArtifactListView, TourListView, TourDetailView, WhatsHereView, get_nearby_artifacts

# custom views vendors
urlpatterns = patterns('market.views',
    url(r'^$', view=OrganizationListView.as_view(), name="artifacts_index"),
    url(r'^whats-here/$', view=WhatsHereView.as_view(), name="whats_here"),
    url(r'^lookup-loc/(?P<loc>[-\w]+)/$', view=get_nearby_artifacts, name="lookup_loc"),
    url(r'^(?P<slug>[-\w]+)/', view=OrganizationDetailView.as_view(), name="organization_detail"),
    url(r'^(?P<organization_slug>[-\w]+)/artifacts/', view=ArtifactListView.as_view(), name="artifact_list"),
    url(r'^(?P<organization_slug>[-\w]+)/artifacts/(?P<slug>[-\w]+)/', view=ArtifactDetailView.as_view(), name="artifact_detail"),
    url(r'^(?P<organization_slug>[-\w]+)/tours/', view=TourListView.as_view(), name="tour_list"),
    url(r'^(?P<organization_slug>[-\w]+)/tours/(?P<slug>[-\w]+)/', view=TourDetailView.as_view(), name="tour_detail"),
)
