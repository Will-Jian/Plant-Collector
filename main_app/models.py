from django.db import models
from django.urls import reverse

WATERED = (
    ('M', 'Morning'),
    ('N', 'Night')
)
class Fertilizer(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('fertilizers_detail', kwargs={'pk': self.id})

class Plant(models.Model): 
    species = models.CharField(max_length=100)
    hardiness = models.CharField(max_length=100) 
    description = models.TextField(max_length=250)
    fertilizers = models.ManyToManyField(Fertilizer)

    def __str__(self):
        return f'{self.species}({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

class Watering(models.Model):
    date = models.DateField('watering date')
    watered = models.CharField(max_length=1, choices=WATERED, default=WATERED[0][0])
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE
    )


    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_watered_display()} on {self.date}"
    class Meta:
        ordering = ['-date']

