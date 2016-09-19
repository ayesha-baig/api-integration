"""
Management command to rename an app from old name to new name
"""
import logging
from django.core.management.base import BaseCommand
from django.db import connection, transaction
from django.apps import apps


log = logging.getLogger(__name__)


def get_app_model_names(app_name):
    app = apps.get_app_config(app_name)
    return app.models


class Command(BaseCommand):
    """
    Renames an app from old name to new name and updates database accordingly
    """
    help = 'Renames an app from old name to new name and updates database accordingly'

    def add_arguments(self, parser):
        parser.add_argument('old_app_name', type=str)
        parser.add_argument('new_app_name', type=str)

    def handle(self, *args, **options):
        log.info('renaming app and related tables')

        # Get the 'old app name' as an argument
        old_app_name = options['old_app_name']

        # Get the 'new app name' as an argument
        new_app_name = options['new_app_name']

        cursor = connection.cursor()

        with transaction.atomic():
            cursor.execute('UPDATE django_content_type SET app_label = %s WHERE app_label = %s',
                           [new_app_name, old_app_name])

            # Get the names of old app's models to rename tables in database
            old_app_model_names = get_app_model_names(old_app_name)

            for model_name in old_app_model_names:
                new_table_name = new_app_name + '_' + model_name
                old_table_name = old_app_name + '_' + model_name

                sql = 'ALTER TABLE %s RENAME TO %s' % (old_table_name, new_table_name)
                cursor.execute(sql)

            log.info('app and related tables successfully renamed')
