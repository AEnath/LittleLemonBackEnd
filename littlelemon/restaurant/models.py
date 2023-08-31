from django.db import models

# Create your models here.
class Menu(models.Model):
    # ID = models.SmallIntegerField(max_length=5)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.SmallIntegerField(max_length=5)

    def __str__(self) -> str:
        return f'{self.Title} : {self.Price}'

class Booking(models.Model):
    # ID = models.SmallIntegerField(max_length=11)
    Name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField(max_length=6)
    BookingDate = models.DateTimeField()

    def __str__(self) -> str:
        return self.Name