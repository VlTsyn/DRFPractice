from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="courses/images", blank=True, null=True, verbose_name="Превью курса")


    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):

    name = models.CharField(max_length=100, verbose_name="Название урока")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="lessons/images", blank=True, null=True, verbose_name="Превью урока")
    link = models.URLField(blank=True, null=True, verbose_name="Ссылка на видео")


    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
