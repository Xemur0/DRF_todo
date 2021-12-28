from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, \
    APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

import project
from project.models import Project, Todo
from .views import UserCustomViewSet
from .models import User


# Create your tests here.

class TestUserViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_1234'

        self.data = {'username': 'Balalayka', 'first_name': 'Aleksey', 'last_name': 'Yo',
                     'email': 'balalayka@gmail.com'}
        self.update_data = {'username': 'MadBalalayka', 'first_name': 'Aleksandr', 'last_name': 'YOLO',
                            'email': 'Madbalalayka@gmail.com'}
        self.url = '/api/users/'
        self.admin = User.objects.create_superuser(self.name, 'admin@admin.ru', self.password)

    def test_get_list(self):
        # создаем обьект класса APIRequestFactory
        factory = APIRequestFactory()
        # определяем адрес и метод для отправки запроса
        request = factory.get(self.url)
        # указываем какой тип запроса будет передан в UserCustomViewSet
        view = UserCustomViewSet.as_view({'get': 'list'})
        # передаем во view и получаем ответ
        response = view(request)
        # проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')

        # изменил вьюху
        view = UserCustomViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')

        # пройти авторизацию
        force_authenticate(request, self.admin)
        view = UserCustomViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        client = APIClient()
        # создаем юзера череза ОРМ для проверки детализации
        user = User.objects.create(**self.data)

        # запрос
        response = client.get(f'{self.url}{user.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_guest(self):
        client = APIClient()
        # создаем юзера череза ОРМ для проверки обновления
        user = User.objects.create(**self.data)

        # запрос на изменение данных
        response = client.put(f'{self.url}{user.id}/', self.update_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_admin(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        client.login(username=self.name, password=self.password)
        response = client.put(f'{self.url}{user.id}/', self.update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_update = User.objects.get(id=user.id)

        self.assertEqual(user_update.first_name, 'Aleksandr')
        self.assertEqual(user_update.last_name, 'YOLO')
        self.assertEqual(user_update.email, 'Madbalalayka@gmail.com')
        client.logout()

    def tearDown(self) -> None:
        pass


class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        import math
        response = math.sqrt(4)
        self.assertEqual(response, 2)


class TestProjectViewSet(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_1234'
        self.url = '/api/project/'

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_admin(self):
        # создаем проект
        proj = Project.objects.create(name='test', url_rep='http://www.test.ru')
        # авторизация
        self.client.login(username=self.name, password=self.password)
        # запрос
        response = self.client.put(f'{self.url}{proj.id}/',
                                   {'name': 'test1', 'url_rep': 'http://www.test11.ru', 'users': [1]})
        # проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем проект
        projct = Project.objects.get(id=proj.id)
        # проверка
        self.assertEqual(projct.name, 'test1')
        # логаут
        self.client.logout()

    def test_update_mixer(self):
        proj = mixer.blend(Project)  # сам генерирует тестовые данные
        self.client.login(username=self.name, password=self.password)
        # запрос
        response = self.client.put(f'{self.url}{proj.id}/',
                                   {'name': 'test1', 'url_rep': 'http://www.test11.ru', 'users': [1]})
        # проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем проект
        projct = Project.objects.get(id=proj.id)
        # проверка
        self.assertEqual(projct.name, 'test1')
        # логаут
        self.client.logout()

    def test_update_mixer_text(self):
        proj = mixer.blend(Project, name='John Wick')  # кастомный вариант, с конкретными данными
        self.client.login(username=self.name, password=self.password)
        # запрос
        response = self.client.put(f'{self.url}{proj.id}/',
                                   {'name': 'test1', 'url_rep': 'http://www.test11.ru', 'users': [1]})
        # проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем проект
        projct = Project.objects.get(id=proj.id)
        # проверка
        self.assertEqual(projct.name, 'test1')
        # логаут
        self.client.logout()
