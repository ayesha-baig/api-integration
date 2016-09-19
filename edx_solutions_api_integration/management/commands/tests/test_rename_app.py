"""
Test for rename_app command
"""
import mock
from django.db import connection, transaction
from django.test import TestCase
from django.core.management import call_command
from django.contrib.contenttypes.models import ContentType


class RenameAppTests(TestCase):
    """
    Test suite for renaming app and related database tables
    """

    def setUp(self):
        super(RenameAppTests, self).setUp()

        self.old_app_name = 'old_app'
        self.new_app_name = 'new_app'

        self.model_names = {
            'fake_table',
            'dummy_table'
        }

        self.old_app_content_type = ContentType.objects.create(
            app_label=self.old_app_name,
            model='dummymodel'
        )

        self.cursor = connection.cursor()
        for table_name in self.model_names:
            create_table_sql = 'CREATE TABLE %s (' \
                               'id integer NOT NULL PRIMARY KEY AUTOINCREMENT,' \
                               'name varchar(50) NOT NULL)' % (self.old_app_name + '_' + table_name)
            self.cursor.execute(create_table_sql)

    def tearDown(self):
        super(RenameAppTests, self).tearDown()

        for table_name in self.model_names:
            self.cursor.execute('DROP TABLE %s' % (self.new_app_name + '_' + table_name))

    def table_exists(self, table_name):
        """
        Checks if table exists in database
        """
        tables = connection.introspection.table_names()
        return table_name in tables

    def test_rename_app(self):
        """
        Test the app renaming
        """
        for table_name in self.model_names:
            self.assertEqual(self.table_exists(self.old_app_name + '_' + table_name), True)

        self.assertEqual(ContentType.objects.filter(app_label=self.old_app_name).count(), 1)
        self.assertEqual(ContentType.objects.filter(app_label=self.new_app_name).count(), 0)

        with mock.patch('edx_solutions_api_integration.management.commands.rename_app.get_app_model_names') as patched_get_model_names:
            patched_get_model_names.return_value = self.model_names
            call_command('rename_app', self.old_app_name, self.new_app_name)

        # Check that tables with old app name prefix do not exist
        for table_name in self.model_names:
            self.assertEqual(self.table_exists(self.old_app_name + '_' + table_name), False)

        # Check that tables with new app name prefix do exist
        for table_name in self.model_names:
            self.assertEqual(self.table_exists(self.new_app_name + '_' + table_name), True)

        self.assertEqual(ContentType.objects.filter(app_label=self.old_app_name).count(), 0)
        self.assertEqual(ContentType.objects.filter(app_label=self.new_app_name).count(), 1)
