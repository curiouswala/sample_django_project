from django.db import models

SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',)
        )

# Create your models here.
class Dog(models.Model):
	NAME = models.CharField(max_length=100)
	BREED = models.CharField(max_length=100)
	AGE = models.IntegerField()
	SEX = models.CharField(max_length=1, choices=SEX_CHOICES)

	def __str__(self):
		return f'{self.NAME}, {self.BREED}'