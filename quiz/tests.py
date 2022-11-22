from django.test import TestCase
from .models import Question
from django.urls import reverse

# models test


class WhateverTest(TestCase):
    def create_whatever(
        self,
        question="models.CharField(max_length=250)",
        answer="models.CharField(max_length=100)",
        level="models.CharField(max_length=10)",
        points=3,
        option_one="models.CharField(max_length=100)",
        option_two="models.CharField(max_length=100)",
        option_three="models.CharField(max_length=100)",
        option_four="models.CharField(max_length=100)",
        option_five="models.CharField(max_length=100)",
        hint_one="models.CharField(max_length=200)",
        hint_two="models.CharField(max_length=200)",
    ):
        return Question.objects.create(
            question="models.CharField(max_length=250)",
            answer="models.CharField(max_length=100)",
            level="models.CharField(max_length=10)",
            points=3,
            option_one="models.CharField(max_length=100)",
            option_two="models.CharField(max_length=100)",
            option_three="models.CharField(max_length=100)",
            option_four="models.CharField(max_length=100)",
            option_five="models.CharField(max_length=100)",
            hint_one="models.CharField(max_length=200)",
            hint_two="models.CharField(max_length=200)",
        )

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, Question))
        self.assertEqual(w.__str__(), w.question)

    def test_index_page(self):
        w = self.create_whatever()
        url = reverse("index_page")
        resp = self.client.get(url)
        self.assertRedirects(
            resp,
            "/login/?next=/quiz/index-menu/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
