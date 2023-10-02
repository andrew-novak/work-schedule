from django.db import models

class Shift(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return f"{self.date} - {self.user} - {self.start} - {self.end}" 