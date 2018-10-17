from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=120)
    score = models.IntegerField(max_length=120)
    score.default = 0

    def __str__(self):
        return self.name
    def introduce(self):
        print("Hello, my name is %s and my score is %d" %(self.name, self.score))

class Team(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
        related_name='leader_set',        
    )
    members = models.ManyToManyField(
        Hero,
        related_name='teams',
    )

    def __str__(self):
        return self.name
