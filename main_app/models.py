
# Create your models here.
from django.db import models
from django.urls import reverse 

# Create your models here.
STORES = (
    ('FL','FootLocker'),
    ('G','GOAT'),
    ('STX','STOCKX'),
    ('FL','Finish-line'),
    ('C','Champs'),
    ('N','Nike.com')
)

# Created our Model
class Kick(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    release = models.IntegerField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
      return reverse('detail', kwargs={'kick_id': self.id})

class Stock(models.Model):
    store = models.CharField(
        max_length =5,
        choices = STORES,
        default= STORES[0]
    )
    in_stock = models.BooleanField()
    no_instock = models.IntegerField()
    
    kick = models.ForeignKey(Kick, on_delete=models.CASCADE)
    
    #Come back to this line of code.
    
    #def __str__(self):
        #return f'{self.name()} in {self.store}'
    
    
    