from django.contrib.auth.models import User
from .models import Like
from recipes.models import Recipe
from rest_framework import status
from rest_framework.test import APITestCase


class LikeListViewTests(APITestCase):
    def setUp(self):
        self.merel = User.objects.create_user(username='merel', password='password')
        self.recipe_1 = Recipe.objects.create(
            owner=self.merel,
            title='a recipe',
            instructions="1. cook",
            cooking_time='23',
            prep_time='23'
        )

    def test_can_list_all_likes(self):
        Like.objects.create(
            owner=self.merel,
            recipe=self.recipe_1)
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    # def test_logged_in_user_can_like(self):
    #     self.client.login(username='merel', password='password')
    #     response = self.client.post('/likes/', {
    #         'owner': self.merel,
    #         'recipe': self.recipe_1})
    #     count = Like.objects.count()
    #     self.assertEqual(count, 1)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cannot_like(self):
        response = self.client.post('/likes/', {'owner': self.merel})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)