from django.db import models


class Notes(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    unique_count = models.IntegerField()

    class Meta:
        ordering = ['-unique_count']

    def short_text(self):
        text = self.text
        return text[:50]
