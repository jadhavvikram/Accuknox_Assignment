import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# A function to run in a separate thread
def handle_in_thread(instance):
    print("Signal handler in new thread:", threading.current_thread().name)

# Signal handler
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    # Create and start a new thread for signal handling
    thread = threading.Thread(target=handle_in_thread, args=(instance,))
    thread.start()
    print("Signal handler initiated in thread:", threading.current_thread().name)
