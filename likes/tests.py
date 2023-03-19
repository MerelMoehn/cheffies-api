from django.contrib.auth.models import User
from .models import Like
from recipes.models import Recipe
from rest_framework import status
from rest_framework.test import APITestCase


class LikeListViewTests(APITestCase):
    def setUp(self):
        self.merel = User.objects.create_user(
            username='merel', password='password')
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

    def test_user_not_logged_in_cannot_like(self):
        response = self.client.post('/likes/', {'owner': self.merel})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LikeDetailViewTests(APITestCase):
    def setUp(self):
        self.merel = User.objects.create_user(
            username='merel', password='password')
        self.laura = User.objects.create_user(
            username='laura', password='password')
        self.recipe = Recipe.objects.create(
            owner=self.merel,
            title='a recipe',
            instructions="1. cook",
            cooking_time='23',
            prep_time='23'
        )
        self.like = Like.objects.create(
            owner=self.merel,
            recipe=self.recipe)

    def test_can_retreive_like(self):
        response = self.client.get('/likes/1/')
        self.assertEqual(response.data['owner'], 'merel')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_like_with_invalid_id(self):
        response = self.client.get('/likes/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
