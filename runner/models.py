from django.db import models


class Check(models.Model):
    message = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message} at {self.created_at}"
