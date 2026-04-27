from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length= 150 )
    last_name = models.CharField(max_length= 150 )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length= 25, blank=True, null=True)

def __str__(self):
    return f"{self.first_name} {self.last_name}"

class Order(models.Model):
     STATUS_CHOICES = [
         ('pending', 'Pending')
         ('processing', 'Processing')
         ('shipped' 'Shipped')
        ('delivered' 'Delivered')
        ('cancelled' 'Cancelled')
     ]
 
client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
order_date = models.DateTimeField(auto_now_add=True)
status = models.CharField(max_length= 25 , choices=STATUS_CHOICES, default= '5')
delivery_address =  models.TextField()
notes = models.TextField(blank=True, null=True)
total_price = models.DecimalField(max_digits= 15, decimal place=3)

def __str__(self):
   return f"Order #{self.id} - {self.client}"


from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length= 150 )
    last_name = models.CharField(max_length= 150 )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length= 25, blank=True, null=True)

def __str__(self):
    return f"{self.first_name} {self.last_name}"

class Order(models.Model):
     STATUS_CHOICES = [
         ('car', 'Car')
         ('drone', 'Drone')
         ('bike' 'Bike')
        ('locker' 'Locker')
        ('truck' 'Truck')
     ]
 
client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
order_date = models.DateTimeField(auto_now_add=True)
status = models.CharField(max_length= 25 , choices=STATUS_CHOICES, default= '5')
delivery_address =  models.TextField()
notes = models.TextField(blank=True, null=True)
total_price = models.DecimalField(max_digits= 15, decimal place=3)

def __str__(self):
   return f"Order #{self.id} - {self.client}"
