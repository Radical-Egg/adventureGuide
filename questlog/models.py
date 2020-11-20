from django.db import models


class Questlog(models.Model):
    createdOn = models.DateTimeField(auto_now_add=True)
    questTitle = models.CharField(max_length=200, verbose_name="Quest Title")
    questContent = models.TextField(verbose_name="Quest Content")

    def __str__(self):
        return self.questTitle

    class Meta:
        ordering = ['createdOn']




    
