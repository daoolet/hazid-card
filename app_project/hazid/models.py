from django.db import models

# Create your models here.

class Survey(models.Model):
    SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large")
    ]
    title = models.CharField(max_length=60)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    jeans = models.CharField(max_length=1, choices=SIZES)
    created_at = models.DateField(auto_now=True)


    class Meta:
        verbose_name = "survey"
        verbose_name_plural = "surveys"
    
    def __str__(self):
        return self.title
