from django.db.models.signals import post_save 
from django.dispatch import receiver 
from django.contrib.auth.models import User 
import time 
# Signal handler 
@receiver(post_save, sender=User) 
def my_signal_handler(sender, instance, **kwargs): 
    print("Signal received") 

time.sleep(5)  # Simulate a time-consuming task 
print("Signal handler finished") 

