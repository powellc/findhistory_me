# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ArtifactImage'
        db.delete_table(u'artifacts_artifactimage')

        # Adding model 'TourStop'
        db.create_table(u'artifacts_tourstop', (
            (u'location_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['artifacts.Location'], unique=True, primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'artifacts', ['TourStop'])

        # Adding M2M table for field artifacts on 'TourStop'
        m2m_table_name = db.shorten_name(u'artifacts_tourstop_artifacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tourstop', models.ForeignKey(orm[u'artifacts.tourstop'], null=False)),
            ('artifact', models.ForeignKey(orm[u'artifacts.artifact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tourstop_id', 'artifact_id'])

        # Adding model 'Location'
        db.create_table(u'artifacts_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2, null=True, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('lat_long', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'artifacts', ['Location'])

        # Adding model 'Tour'
        db.create_table(u'artifacts_tour', (
            (u'location_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['artifacts.Location'], unique=True, primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('filebrowser_safe.fields.FileBrowseField')(max_length=255)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artifacts.Organization'])),
        ))
        db.send_create_signal(u'artifacts', ['Tour'])

        # Adding model 'ArtifactType'
        db.create_table(u'artifacts_artifacttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'artifacts', ['ArtifactType'])

        # Deleting field 'Artifact.updated'
        db.delete_column(u'artifacts_artifact', 'updated')

        # Deleting field 'Artifact.latlong'
        db.delete_column(u'artifacts_artifact', 'latlong')

        # Deleting field 'Artifact.address'
        db.delete_column(u'artifacts_artifact', 'address')

        # Deleting field 'Artifact.id'
        db.delete_column(u'artifacts_artifact', u'id')

        # Deleting field 'Artifact.city'
        db.delete_column(u'artifacts_artifact', 'city')

        # Deleting field 'Artifact.created'
        db.delete_column(u'artifacts_artifact', 'created')

        # Deleting field 'Artifact.title'
        db.delete_column(u'artifacts_artifact', 'title')

        # Deleting field 'Artifact.zipcode'
        db.delete_column(u'artifacts_artifact', 'zipcode')

        # Deleting field 'Artifact.created_by'
        db.delete_column(u'artifacts_artifact', 'created_by_id')

        # Deleting field 'Artifact.slug'
        db.delete_column(u'artifacts_artifact', 'slug')

        # Deleting field 'Artifact.state'
        db.delete_column(u'artifacts_artifact', 'state')

        # Adding field 'Artifact.location_ptr'
        db.add_column(u'artifacts_artifact', u'location_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['artifacts.Location'], unique=True, primary_key=True),
                      keep_default=False)

        # Adding field 'Artifact.inventory_id'
        db.add_column(u'artifacts_artifact', 'inventory_id',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.built'
        db.add_column(u'artifacts_artifact', 'built',
                      self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.architect'
        db.add_column(u'artifacts_artifact', 'architect',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.style'
        db.add_column(u'artifacts_artifact', 'style',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.type'
        db.add_column(u'artifacts_artifact', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['artifacts.ArtifactType']),
                      keep_default=False)

        # Deleting field 'Organization.city'
        db.delete_column(u'artifacts_organization', 'city')

        # Deleting field 'Organization.latlong'
        db.delete_column(u'artifacts_organization', 'latlong')

        # Deleting field 'Organization.name'
        db.delete_column(u'artifacts_organization', 'name')

        # Deleting field 'Organization.address'
        db.delete_column(u'artifacts_organization', 'address')

        # Deleting field 'Organization.state'
        db.delete_column(u'artifacts_organization', 'state')

        # Deleting field 'Organization.zipcode'
        db.delete_column(u'artifacts_organization', 'zipcode')

        # Adding field 'Organization.location_ptr'
        db.add_column(u'artifacts_organization', u'location_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['artifacts.Location'], unique=True),
                      keep_default=False)

        # Adding field 'Organization.phone'
        db.add_column(u'artifacts_organization', 'phone',
                      self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organization.website'
        db.add_column(u'artifacts_organization', 'website',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'ArtifactImage'
        db.create_table(u'artifacts_artifactimage', (
            ('image', self.gf('filebrowser_safe.fields.FileBrowseField')(max_length=255)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artifact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artifacts.Artifact'])),
        ))
        db.send_create_signal(u'artifacts', ['ArtifactImage'])

        # Deleting model 'TourStop'
        db.delete_table(u'artifacts_tourstop')

        # Removing M2M table for field artifacts on 'TourStop'
        db.delete_table(db.shorten_name(u'artifacts_tourstop_artifacts'))

        # Deleting model 'Location'
        db.delete_table(u'artifacts_location')

        # Deleting model 'Tour'
        db.delete_table(u'artifacts_tour')

        # Deleting model 'ArtifactType'
        db.delete_table(u'artifacts_artifacttype')

        # Adding field 'Artifact.updated'
        db.add_column(u'artifacts_artifact', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 6, 2, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Artifact.latlong'
        db.add_column(u'artifacts_artifact', 'latlong',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.address'
        db.add_column(u'artifacts_artifact', 'address',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.id'
        db.add_column(u'artifacts_artifact', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Adding field 'Artifact.city'
        db.add_column(u'artifacts_artifact', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.created'
        db.add_column(u'artifacts_artifact', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 6, 2, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Artifact.title'
        db.add_column(u'artifacts_artifact', 'title',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=255),
                      keep_default=False)

        # Adding field 'Artifact.zipcode'
        db.add_column(u'artifacts_artifact', 'zipcode',
                      self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.created_by'
        db.add_column(u'artifacts_artifact', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Artifact.slug'
        db.add_column(u'artifacts_artifact', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='none', max_length=50),
                      keep_default=False)

        # Adding field 'Artifact.state'
        db.add_column(u'artifacts_artifact', 'state',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Artifact.location_ptr'
        db.delete_column(u'artifacts_artifact', u'location_ptr_id')

        # Deleting field 'Artifact.inventory_id'
        db.delete_column(u'artifacts_artifact', 'inventory_id')

        # Deleting field 'Artifact.built'
        db.delete_column(u'artifacts_artifact', 'built')

        # Deleting field 'Artifact.architect'
        db.delete_column(u'artifacts_artifact', 'architect')

        # Deleting field 'Artifact.style'
        db.delete_column(u'artifacts_artifact', 'style')

        # Deleting field 'Artifact.type'
        db.delete_column(u'artifacts_artifact', 'type_id')

        # Adding field 'Organization.city'
        db.add_column(u'artifacts_organization', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organization.latlong'
        db.add_column(u'artifacts_organization', 'latlong',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organization.name'
        db.add_column(u'artifacts_organization', 'name',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=255),
                      keep_default=False)

        # Adding field 'Organization.address'
        db.add_column(u'artifacts_organization', 'address',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organization.state'
        db.add_column(u'artifacts_organization', 'state',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organization.zipcode'
        db.add_column(u'artifacts_organization', 'zipcode',
                      self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Organization.location_ptr'
        db.delete_column(u'artifacts_organization', u'location_ptr_id')

        # Deleting field 'Organization.phone'
        db.delete_column(u'artifacts_organization', 'phone')

        # Deleting field 'Organization.website'
        db.delete_column(u'artifacts_organization', 'website')


    models = {
        u'artifacts.artifact': {
            'Meta': {'ordering': "('city',)", 'object_name': 'Artifact', '_ormbases': [u'artifacts.Location']},
            'architect': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'built': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image': ('filebrowser_safe.fields.FileBrowseField', [], {'max_length': '255'}),
            'inventory_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['artifacts.Location']", 'unique': 'True', 'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artifacts.Organization']"}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artifacts.ArtifactType']"})
        },
        u'artifacts.artifacttype': {
            'Meta': {'object_name': 'ArtifactType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'artifacts.location': {
            'Meta': {'ordering': "('city',)", 'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat_long': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        u'artifacts.organization': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Organization', '_ormbases': [u'pages.Page', u'artifacts.Location']},
            u'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['artifacts.Location']", 'unique': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'artifacts.tour': {
            'Meta': {'ordering': "('city',)", 'object_name': 'Tour', '_ormbases': [u'artifacts.Location']},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image': ('filebrowser_safe.fields.FileBrowseField', [], {'max_length': '255'}),
            u'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['artifacts.Location']", 'unique': 'True', 'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artifacts.Organization']"})
        },
        u'artifacts.tourstop': {
            'Meta': {'ordering': "('city',)", 'object_name': 'TourStop', '_ormbases': [u'artifacts.Location']},
            'artifacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['artifacts.Artifact']", 'symmetrical': 'False'}),
            u'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['artifacts.Location']", 'unique': 'True', 'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'generic.assignedkeyword': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'AssignedKeyword'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': u"orm['generic.Keyword']"}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {})
        },
        u'generic.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'pages.page': {
            'Meta': {'ordering': "('titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': u"orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['artifacts']