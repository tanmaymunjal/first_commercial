from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.EmailField()
    first_name=models.CharField(max_length=122)
    last_name=models.CharField(max_length=122)
    feedback=models.TextField()
    date=models.DateTimeField()

    def __str__(self):
        return(self.first_name+" "+self.last_name)


    
