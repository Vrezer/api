from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    question_date=models.DateField(auto_now=True)
    object=models.Manager()
    def __str__(self):
        return self.question_text
    def ostatnio_opublikowane(self):
        return self.question_date >=timezone.now() - datetime.timedelta(days=-1)  

    class Meta:
        verbose_name='Pytanie'    
        verbose_name_plural='Pytania

class Answer(models.Model):
    question= models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=200)
    glosy=models.IntegerField(default=0)
    object=models.Manager()
    def __str__(self):
        return self.text_odpowiedzi

    class Meta:
        verbose_name='Odpowiedz'    
        verbose_name_plural='Odpowiedzi'