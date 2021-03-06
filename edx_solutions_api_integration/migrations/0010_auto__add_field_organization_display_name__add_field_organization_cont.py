# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, missing-docstring, unused-argument, unused-import, line-too-long
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Organization.display_name'
        db.add_column('edx_solutions_api_integration_organization', 'display_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organization.contact_name'
        db.add_column('edx_solutions_api_integration_organization', 'contact_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organization.contact_email'
        db.add_column('edx_solutions_api_integration_organization', 'contact_email',
                      self.gf('django.db.models.fields.EmailField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organization.contact_phone'
        db.add_column('edx_solutions_api_integration_organization', 'contact_phone',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Organization.display_name'
        db.delete_column('edx_solutions_api_integration_organization', 'display_name')

        # Deleting field 'Organization.contact_name'
        db.delete_column('edx_solutions_api_integration_organization', 'contact_name')

        # Deleting field 'Organization.contact_email'
        db.delete_column('edx_solutions_api_integration_organization', 'contact_email')

        # Deleting field 'Organization.contact_phone'
        db.delete_column('edx_solutions_api_integration_organization', 'contact_phone')

    models = {
        'edx_solutions_api_integration.coursecontentgrouprelationship': {
            'Meta': {'unique_together': "(('course_id', 'content_id', 'group_profile'),)", 'object_name': 'CourseContentGroupRelationship'},  # pylint: disable=C0301
            'content_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'group_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['edx_solutions_api_integration.GroupProfile']"}),  # pylint: disable=C0301
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'record_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'edx_solutions_api_integration.coursegrouprelationship': {
            'Meta': {'object_name': 'CourseGroupRelationship'},
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'record_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'edx_solutions_api_integration.groupprofile': {
            'Meta': {'object_name': 'GroupProfile', 'db_table': "'auth_groupprofile'"},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'group': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.Group']", 'unique': 'True'}),  # pylint: disable=C0301
            'group_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'db_index': 'True'}),  # pylint: disable=C0301
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'record_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'edx_solutions_api_integration.grouprelationship': {
            'Meta': {'object_name': 'GroupRelationship'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'group': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.Group']", 'unique': 'True', 'primary_key': 'True'}),  # pylint: disable=C0301
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent_group': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'child_groups'", 'null': 'True', 'blank': 'True', 'to': "orm['edx_solutions_api_integration.GroupRelationship']"}),  # pylint: disable=C0301
            'record_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'edx_solutions_api_integration.linkedgrouprelationship': {
            'Meta': {'object_name': 'LinkedGroupRelationship'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'from_group_relationship': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_group_relationships'", 'to': "orm['edx_solutions_api_integration.GroupRelationship']"}),  # pylint: disable=C0301
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'record_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'to_group_relationship': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_group_relationships'", 'to': "orm['edx_solutions_api_integration.GroupRelationship']"})  # pylint: disable=C0301
        },
        'edx_solutions_api_integration.organization': {
            'Meta': {'object_name': 'Organization'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),  # pylint: disable=C0301
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),  # pylint: disable=C0301
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),  # pylint: disable=C0301
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),  # pylint: disable=C0301
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'organizations'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),  # pylint: disable=C0301
            'workgroups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'organizations'", 'symmetrical': 'False', 'to': "orm['projects.Workgroup']"})  # pylint: disable=C0301
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})  # pylint: disable=C0301
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},  # pylint: disable=C0301
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),  # pylint: disable=C0301
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),  # pylint: disable=C0301
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),  # pylint: disable=C0301
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},  # pylint: disable=C0301
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'projects.project': {
            'Meta': {'unique_together': "(('course_id', 'content_id'),)", 'object_name': 'Project'},
            'content_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        'projects.workgroup': {
            'Meta': {'object_name': 'Workgroup'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'workgroups'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),  # pylint: disable=C0301
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'workgroups'", 'to': "orm['projects.Project']"}),  # pylint: disable=C0301
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'workgroups'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"})  # pylint: disable=C0301
        }
    }

    complete_apps = ['edx_solutions_api_integration']
