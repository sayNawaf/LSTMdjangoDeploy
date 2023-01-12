from django.db import models

# Create your models here.
class Prediction2(models.Model):
    
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    text = models.TextField()
    Predicted_Class = models.CharField(max_length = 5)
    confidance_score = models.FloatField()
