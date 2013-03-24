# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'accounts_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('marital_status', self.gf('django.db.models.fields.CharField')(default='S', max_length=1)),
            ('kids', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('origin_country', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('origin_city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('current_country', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('current_city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(default='S', max_length=4)),
            ('function', self.gf('django.db.models.fields.CharField')(default='S', max_length=4)),
            ('objective', self.gf('django.db.models.fields.TextField')()),
            ('headline', self.gf('django.db.models.fields.TextField')()),
            ('unread', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('facebook_session_key', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('twitter_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('twitter_session_key', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('linkedin_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('linkedin_session_key', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('other_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('other_session_key', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'accounts', ['Account'])

        # Adding M2M table for field groups on 'Account'
        db.create_table(u'accounts_account_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('account', models.ForeignKey(orm[u'accounts.account'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(u'accounts_account_groups', ['account_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'Account'
        db.create_table(u'accounts_account_user_permissions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('account', models.ForeignKey(orm[u'accounts.account'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(u'accounts_account_user_permissions', ['account_id', 'permission_id'])

        # Adding model 'Organization'
        db.create_table(u'accounts_organization', (
            (u'group_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.Group'], unique=True, primary_key=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('dp', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'accounts', ['Organization'])

        # Adding model 'Education'
        db.create_table(u'accounts_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Account'])),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Organization'])),
            ('certification', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('concentration', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=34, null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'accounts', ['Education'])

        # Adding model 'Experience'
        db.create_table(u'accounts_experience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Account'])),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Organization'])),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'accounts', ['Experience'])

        # Adding model 'Supporter'
        db.create_table(u'accounts_supporter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(related_name='account_root', to=orm['accounts.Account'])),
            ('supporter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='account_node', to=orm['accounts.Account'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_viewed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('amount_supported', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('campaign_field', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('relationship', self.gf('django.db.models.fields.CharField')(default='UN', max_length=2)),
        ))
        db.send_create_signal(u'accounts', ['Supporter'])

        # Adding model 'TaggedActivity'
        db.create_table(u'accounts_taggedactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'accounts_taggedactivity_tagged_items', to=orm['contenttypes.ContentType'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='activity_detail', to=orm['tags.Activity'])),
        ))
        db.send_create_signal(u'accounts', ['TaggedActivity'])

        # Adding model 'TaggedAward'
        db.create_table(u'accounts_taggedaward', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'accounts_taggedaward_tagged_items', to=orm['contenttypes.ContentType'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='award_detail', to=orm['tags.Award'])),
        ))
        db.send_create_signal(u'accounts', ['TaggedAward'])

        # Adding model 'TaggedCertification'
        db.create_table(u'accounts_taggedcertification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'accounts_taggedcertification_tagged_items', to=orm['contenttypes.ContentType'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='certification_detail', to=orm['tags.Certification'])),
        ))
        db.send_create_signal(u'accounts', ['TaggedCertification'])

        # Adding model 'TaggedInterest'
        db.create_table(u'accounts_taggedinterest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'accounts_taggedinterest_tagged_items', to=orm['contenttypes.ContentType'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='interest_detail', to=orm['tags.Interest'])),
        ))
        db.send_create_signal(u'accounts', ['TaggedInterest'])

        # Adding model 'TaggedLanguage'
        db.create_table(u'accounts_taggedlanguage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'accounts_taggedlanguage_tagged_items', to=orm['contenttypes.ContentType'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='language_detail', to=orm['tags.Language'])),
        ))
        db.send_create_signal(u'accounts', ['TaggedLanguage'])

        # Adding model 'TaggedSkill'
        db.create_table(u'accounts_taggedskill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'accounts_taggedskill_tagged_items', to=orm['contenttypes.ContentType'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skill_detail', to=orm['tags.Skill'])),
        ))
        db.send_create_signal(u'accounts', ['TaggedSkill'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'accounts_account')

        # Removing M2M table for field groups on 'Account'
        db.delete_table('accounts_account_groups')

        # Removing M2M table for field user_permissions on 'Account'
        db.delete_table('accounts_account_user_permissions')

        # Deleting model 'Organization'
        db.delete_table(u'accounts_organization')

        # Deleting model 'Education'
        db.delete_table(u'accounts_education')

        # Deleting model 'Experience'
        db.delete_table(u'accounts_experience')

        # Deleting model 'Supporter'
        db.delete_table(u'accounts_supporter')

        # Deleting model 'TaggedActivity'
        db.delete_table(u'accounts_taggedactivity')

        # Deleting model 'TaggedAward'
        db.delete_table(u'accounts_taggedaward')

        # Deleting model 'TaggedCertification'
        db.delete_table(u'accounts_taggedcertification')

        # Deleting model 'TaggedInterest'
        db.delete_table(u'accounts_taggedinterest')

        # Deleting model 'TaggedLanguage'
        db.delete_table(u'accounts_taggedlanguage')

        # Deleting model 'TaggedSkill'
        db.delete_table(u'accounts_taggedskill')


    models = {
        u'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'current_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'current_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'educations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mi_education'", 'symmetrical': 'False', 'through': u"orm['accounts.Education']", 'to': u"orm['accounts.Organization']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'experiences': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mi_experience'", 'symmetrical': 'False', 'through': u"orm['accounts.Experience']", 'to': u"orm['accounts.Organization']"}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'facebook_session_key': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'function': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '4'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'headline': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '4'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kids': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'linkedin_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'linkedin_session_key': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'objective': ('django.db.models.fields.TextField', [], {}),
            'origin_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'origin_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'other_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'other_session_key': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'purchases': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'purchase'", 'to': u"orm['campaigns.Campaign']", 'through': u"orm['transactions.Transaction']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'supporters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['accounts.Account']", 'null': 'True', 'through': u"orm['accounts.Supporter']", 'blank': 'True'}),
            'twitter_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'twitter_session_key': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'unread': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'accounts.education': {
            'Meta': {'object_name': 'Education'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Account']"}),
            'certification': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'concentration': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Organization']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'accounts.experience': {
            'Meta': {'object_name': 'Experience'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Account']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Organization']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'accounts.organization': {
            'Meta': {'object_name': 'Organization', '_ormbases': [u'auth.Group']},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dp': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            u'group_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.Group']", 'unique': 'True', 'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'accounts.supporter': {
            'Meta': {'object_name': 'Supporter'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'account_root'", 'to': u"orm['accounts.Account']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'amount_supported': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'campaign_field': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_viewed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'default': "'UN'", 'max_length': '2'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'supporter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'account_node'", 'to': u"orm['accounts.Account']"})
        },
        u'accounts.taggedactivity': {
            'Meta': {'object_name': 'TaggedActivity'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'accounts_taggedactivity_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activity_detail'", 'to': u"orm['tags.Activity']"})
        },
        u'accounts.taggedaward': {
            'Meta': {'object_name': 'TaggedAward'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'accounts_taggedaward_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'award_detail'", 'to': u"orm['tags.Award']"})
        },
        u'accounts.taggedcertification': {
            'Meta': {'object_name': 'TaggedCertification'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'accounts_taggedcertification_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'certification_detail'", 'to': u"orm['tags.Certification']"})
        },
        u'accounts.taggedinterest': {
            'Meta': {'object_name': 'TaggedInterest'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'accounts_taggedinterest_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interest_detail'", 'to': u"orm['tags.Interest']"})
        },
        u'accounts.taggedlanguage': {
            'Meta': {'object_name': 'TaggedLanguage'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'accounts_taggedlanguage_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'language_detail'", 'to': u"orm['tags.Language']"})
        },
        u'accounts.taggedskill': {
            'Meta': {'object_name': 'TaggedSkill'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'accounts_taggedskill_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skill_detail'", 'to': u"orm['tags.Skill']"})
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
        u'campaigns.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'campaign'", 'null': 'True', 'to': u"orm['accounts.Account']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'amount_pledged': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'backers': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'call_to_action': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '34'}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'completion_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'consummated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currently_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'endline': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'feature_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'goal': ('django.db.models.fields.IntegerField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimum_pledge': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'multimedia': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['multimedia.Multimedia']", 'symmetrical': 'False'}),
            'number_backers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'multimedia.multimedia': {
            'Meta': {'object_name': 'Multimedia'},
            'caption_overlay': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Organization']", 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'owner_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'resource_uri': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subcategory': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uploaded_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Account']", 'null': 'True', 'blank': 'True'}),
            'uploaded_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'tags.activity': {
            'Meta': {'object_name': 'Activity'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tags.award': {
            'Meta': {'object_name': 'Award'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tags.certification': {
            'Meta': {'object_name': 'Certification'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tags.interest': {
            'Meta': {'object_name': 'Interest'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tags.language': {
            'Meta': {'object_name': 'Language'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'proficiency': ('django.db.models.fields.CharField', [], {'max_length': '34'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tags.skill': {
            'Meta': {'object_name': 'Skill'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'proficiency': ('django.db.models.fields.CharField', [], {'max_length': '34'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'transactions.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Account']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'amount_supported': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaigns.Campaign']"}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consummated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_viewed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'default': "'UN'", 'max_length': '2'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['accounts']