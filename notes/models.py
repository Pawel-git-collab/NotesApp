from django.db import models


class Note(models.Model):
    text = models.CharField(max_length=120, verbose_name="")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(str(self.text)) > 10:
            return str(self.text)[:11]
        return str(self.text)

