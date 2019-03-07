from django.db import models

class Customer(models.Model):
    email = models.CharField(max_length=100)
    mailing_address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# order in this case is the "many" side
class Order(models.Model):
    order_number = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return str(self.order_number)
