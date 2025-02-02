from django.test import TestCase
from .models import FAQ


class FAQModelTest(TestCase):
    def test_translation(self):
        faq = FAQ.objects.create(question="What is Django?", answer="A web framework.")
        self.assertEqual(faq.get_translated_question("hi"), faq.question_hi)
