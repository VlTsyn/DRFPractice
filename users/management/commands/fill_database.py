from django.core.management.base import BaseCommand
from materials.models import Course, Lesson
from users.models import Payment, User
from datetime import datetime


class Command(BaseCommand):
    """Команда для очистки и заполнения БД тестовыми данными"""

    help = 'Очистка и заполнение БД тестовыми данными'

    def handle(self, *args, **kwargs):


        self.stdout.write(self.style.WARNING('Очистка БД...'))
        Payment.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('БД очищена'))

        self.stdout.write(self.style.WARNING('Создание тестовых пользователей...'))
        user1 = User.objects.create(
            email='ivan@example.com',
            password='password123',
            phone='+79001234567',
            city='Москва'
        )
        user2 = User.objects.create(
            email='maria@example.com',
            password='password123',
            phone='+79007654321',
            city='Санкт-Петербург'
        )
        user3 = User.objects.create(
            email='alex@example.com',
            password='password123',
            phone='+79009876543',
            city='Казань'
        )
        users = [user1, user2, user3]
        self.stdout.write(self.style.SUCCESS('Тестовые пользователи созданы'))

        self.stdout.write(self.style.WARNING('Создание тестовых курсов...'))
        course1 = Course.objects.create(
            name='Python разработчик',
            description='Курс по Python'
        )
        course2 = Course.objects.create(
            name='JavaScript Frontend',
            description='Курс по JavaScript'
        )
        course3 = Course.objects.create(
            name='Data Science',
            description='Курс по машинному обучению и анализу данных'
        )
        courses = [course1, course2, course3]
        self.stdout.write(self.style.SUCCESS('Тестовые курсы созданы'))

        self.stdout.write(self.style.WARNING('Создание тестовых уроков...'))
        lesson1 = Lesson.objects.create(
            course=courses[0],
            name='Введение в Python',
            description='Основы синтаксиса Python',
        )
        lesson2 = Lesson.objects.create(
            course=courses[0],
            name='ООП в Python',
            description='Объектно-ориентированное программирование',
        )
        lesson3 = Lesson.objects.create(
            course=courses[1],
            name='HTML и CSS',
            description='Основы верстки',
        )
        lesson4 = Lesson.objects.create(
            course=courses[1],
            name='JavaScript основы',
            description='Базовый синтаксис JavaScript',
        )
        lesson5 = Lesson.objects.create(
            course=courses[2],
            name='Введение в Data Science',
            description='Что такое Data Science и с чем его едят',
        )
        lessons = [lesson1, lesson2, lesson3, lesson4, lesson5]
        self.stdout.write(self.style.SUCCESS('Тестовые уроки созданы'))

        self.stdout.write(self.style.WARNING('Создание тестовых платежей...'))
        payments_data = [
            {
                'user': user1,
                'payment_date': datetime(2026, 5, 1, 10, 30),
                'paid_course': courses[0],
                'paid_lesson': None,
                'amount': 15000,
                'payment_method': 'transfer',
            },
            {
                'user': user2,
                'payment_date': datetime(2026, 5, 2, 14, 15),
                'paid_course': courses[1],
                'paid_lesson': None,
                'amount': 20000,
                'payment_method': 'cash',
            },
            {
                'user': user3,
                'payment_date': datetime(2026, 5, 3, 9, 45),
                'paid_course': courses[2],
                'paid_lesson': None,
                'amount': 25000,
                'payment_method': 'transfer',
            },
            {
                'user': user1,
                'payment_date': datetime(2026, 5, 4, 16, 0),
                'paid_course': None,
                'paid_lesson': lessons[0],
                'amount': 5000,
                'payment_method': 'cash',
            },
            {
                'user': user2,
                'payment_date': datetime(2026, 5, 5, 11, 30),
                'paid_course': None,
                'paid_lesson': lessons[2],
                'amount': 3000,
                'payment_method': 'transfer',
            },
            {
                'user': user3,
                'payment_date': datetime(2026, 5, 6, 13, 20),
                'paid_course': courses[0],
                'paid_lesson': None,
                'amount': 15000,
                'payment_method': 'cash',
            },
            {
                'user': user1,
                'payment_date': datetime(2026, 5, 7, 10, 0),
                'paid_course': None,
                'paid_lesson': lessons[4],
                'amount': 7000,
                'payment_method': 'transfer',
            },
            {
                'user': user2,
                'payment_date': datetime(2026, 5, 8, 15, 45),
                'paid_course': courses[1],
                'paid_lesson': None,
                'amount': 20000,
                'payment_method': 'transfer',
            },
        ]

        for payment in payments_data:
            Payment.objects.create(**payment)

        self.stdout.write(self.style.SUCCESS('Тестовые платежи созданы'))

        self.stdout.write(self.style.SUCCESS('=' * 50))
        self.stdout.write(self.style.SUCCESS(f'ИТОГО СОЗДАНО:'))
        self.stdout.write(self.style.SUCCESS(f'Пользователей: {len(users)}'))
        self.stdout.write(self.style.SUCCESS(f'Курсов: {len(courses)}'))
        self.stdout.write(self.style.SUCCESS(f'Уроков: {len(lessons)}'))
        self.stdout.write(self.style.SUCCESS(f'Платежей: {Payment.objects.count()}'))