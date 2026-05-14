from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Сериализация курса"""

    lessons_count = SerializerMethodField()

    def get_lessons_count(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    """Сериализация урока"""

    class Meta:
        model = Lesson
        fields = '__all__'