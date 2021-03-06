""" Django REST Framework Serializers """

from edx_solutions_api_integration.utils import generate_base_uri
from rest_framework import serializers


class GradeSerializer(serializers.Serializer):
    """ Serializer for model interactions """
    grade = serializers.Field()


class CourseLeadersSerializer(serializers.Serializer):
    """ Serializer for course leaderboard """
    id = serializers.IntegerField(source='user__id')  # pylint: disable=invalid-name
    username = serializers.CharField(source='user__username')
    title = serializers.CharField(source='user__profile__title')
    avatar_url = serializers.CharField(source='user__profile__avatar_url')
    # Percentage grade (versus letter grade)
    grade = serializers.FloatField(source='grade')
    recorded = serializers.DateTimeField(source='modified')


class CourseCompletionsLeadersSerializer(serializers.Serializer):
    """ Serializer for course completions leaderboard """
    id = serializers.IntegerField(source='user__id')  # pylint: disable=invalid-name
    username = serializers.CharField(source='user__username')
    title = serializers.CharField(source='user__profile__title')
    avatar_url = serializers.CharField(source='user__profile__avatar_url')
    completions = serializers.SerializerMethodField('get_completion_percentage')

    def get_completion_percentage(self, obj):
        """
        formats get completions as percentage
        """
        total_completions = self.context['total_completions'] or 0
        completions = obj['completions'] or 0
        completion_percentage = 0
        if total_completions > 0:
            completion_percentage = min(100 * (completions / float(total_completions)), 100)
        return completion_percentage


class CourseSerializer(serializers.Serializer):
    """ Serializer for Courses """
    id = serializers.CharField(source='id')  # pylint: disable=invalid-name
    name = serializers.CharField(source='name')
    category = serializers.CharField(source='category')
    number = serializers.CharField(source='number')
    org = serializers.CharField(source='org')
    uri = serializers.CharField(source='uri')
    course_image_url = serializers.CharField(source='course_image_url')
    resources = serializers.CharField(source='resources')
    due = serializers.DateTimeField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def get_uri(self, course):
        """
        Builds course detail uri
        """
        return "{}/{}".format(generate_base_uri(self.context['request']), course.id)


class OrganizationCourseSerializer(CourseSerializer):
    """ Serializer for Organization Courses """
    name = serializers.CharField(source='display_name')
    enrolled_users = serializers.CharField()

    class Meta(object):
        """ Serializer/field specification """
        fields = ('id', 'name', 'number', 'org', 'start', 'end', 'due', 'enrolled_users', )
