from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from mezzanine.pages.models import Page
from filebrowser_safe.fields import FileBrowseField
from django.contrib.localflavor.us.models import PhoneNumberField, USStateField
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.gis.db import models as gis_models

from .utils import get_lat_long

class StandardMetadata(models.Model):
    """
    A basic (abstract) model for metadata.

	Subclass new models from 'StandardMetadata' instead of 'models.Model'.
    """
    created = models.DateTimeField(default=datetime.now, editable=False)
    updated = models.DateTimeField(default=datetime.now, editable=False)
    created_by = models.ForeignKey(User)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        super(StandardMetadata, self).save(*args, **kwargs)

class Location(StandardMetadata):
    """Location model.

        Just a simple way to keep track of where a market is being held.
        Contains just a name, slug, address, and description."""

    title=models.CharField(_('title'), max_length=255)
    slug=models.SlugField(_('slug'), unique=True)
    address=models.CharField(_('address'), max_length=255, blank=True, null=True)
    city=models.CharField(_('city'), max_length=100, blank=True, null=True)
    state=USStateField(_('state'), blank=True, null=True)
    zipcode=models.CharField(_('zip'), max_length=5, blank=True, null=True)
    lat_long=models.CharField(_('lat and long coords'), max_length=255, blank=True, null=True)
    point = gis_models.PointField()

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')
        ordering = ('city',)

    def __unicode__(self):
        return u'%s' % (self.title)

    @permalink
    def get_absolute_url(self):
        return ('location_detail', None, {'slug': self.slug})


    def save(self):
        if not self.lat_long:
            location = "%s+%s+%s+%s" % (self.address, self.city, self.state, self.zipcode)
            self.lat_long = get_lat_long(location)
            if not self.lat_long:
                location = "%s+%s+%s" % (self.city, self.state, self.zipcode)
                self.lat_long = get_lat_long(location)

        super(Location, self).save()

class Organization(Page, Location):
    phone = PhoneNumberField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)

    @permalink
    def get_absolute_url(self):
        return ('organization_detail', None, {'slug': self.slug})

class ArtifactType(StandardMetadata):
    title = models.CharField(max_length=255)
    slug=models.SlugField(_('slug'), unique=True)

    @permalink
    def get_absolute_url(self):
        return ('artifact_type_detail', None, {'slug': self.slug})

    def __unicode__(self):
        return u'%s' % (self.title)

class Artifact(Location):
    organization = models.ForeignKey(Organization)
    inventory_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = FileBrowseField(max_length=255)
    built = models.CharField(max_length=6, blank=True, null=True)
    architect = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(max_length=255, blank=True, null=True)
    type = models.ForeignKey(ArtifactType)

    @permalink
    def get_absolute_url(self):
        return ('artifact_detail', None, {'organization_slug':self.organization.slug, 'slug': self.slug})

class Tour(Location):
    description = models.TextField(blank=True, null=True)
    image = FileBrowseField(max_length=255)
    organization = models.ForeignKey(Organization)

    @permalink
    def get_absolute_url(self):
        return ('tour_detail', None, {'organization_slug':self.organization.slug, 'slug': self.slug})

class TourStop(Location):
    order = models.IntegerField()
    artifacts = models.ManyToManyField(Artifact)

