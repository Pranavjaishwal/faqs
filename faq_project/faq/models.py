from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG editor
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    answer_hi = models.TextField(blank=True, null=True)  # Hindi translation
    answer_bn = models.TextField(blank=True, null=True)  # Bengali translation

    def get_translated_question(self, lang="en"):
        return getattr(self, f"question_{lang}", self.question)

    def get_translated_answer(self, lang="en"):
        return getattr(self, f"answer_{lang}", self.answer)

    def _str_(self):
        return self.question

    def get_translated_question(self, lang="en"):
        cache_key = f"faq_{self.id}question{lang}"
        cached_value = cache.get(cache_key)
        if cached_value:
            return cached_value
        value = getattr(self, f"question_{lang}", self.question)
        cache.set(cache_key, value, timeout=60 * 60)  # Cache for 1 hour
        return value

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest="hi").text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest="bn").text
        super().save(*args, **kwargs)
