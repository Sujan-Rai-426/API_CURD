from django.db import models


# Create your models here.

# Model for the Note
class Note(models.Model):
    title = models.CharField(max_length=100, null=False, default=False)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
# Model for the transactions
class Transaction(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=100, choices=(("DEBIT","DEBIT"),("CREDIT", "CREDIT")))
    
    def save(self,*args, **kwargs):
        if(self.transaction_type == "DEBIT"):
            self.amount = self.amount * -1
        return super().save()
    def __str__(self):
        return self.title