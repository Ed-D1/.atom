from django.db import models


class Pizza(models.Model):
    """Model for pizza"""
    name = models.CharField(max_length=20)

    def __str__(self):
        """returns a text of pizza"""
        return self.name


class Topping(models.Model):
    """The toppings for the pizza"""
    pizza = models.ForeignKe(Pizza, on_delete=models.CASCADE)
    name = models.charField(max_length=50)
