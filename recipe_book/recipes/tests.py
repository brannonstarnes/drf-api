from unittest import TestCase
from .models import Recipe
from django.contrib.auth import get_user_model

class RecipeTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = get_user_model().objects.create_user(username='test_user1', password='password')
        test_user1.save()

        test_recipe = Recipe.objects.create(
            author = test_user1,
            title = "Huevos Rancheros",
            body = "A delicious egg breafast!"
        )
        test_recipe.save()
    
    def test_recipe_book_content(self):
        recipe = Recipe.objects.get(id=1)
        actual_author = str(recipe.author)
        actual_title = str(recipe.title)
        actual_body = str(recipe.body)
        self.assertEqual(actual_author, "test_user1")
        self.assertEqual(actual_title, "Huevos Rancheros")
        self.assertEqual(actual_body, "A delicious egg breakfast!")