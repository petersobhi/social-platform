from django.dispatch import receiver
from django.db.models.signals import post_save

from core.models import Like

@receiver(post_save, sender=Like)
def update_likes_count(sender, instance, **kwargs):
    post = instance.post
    post.likes_count += 1
    post.save()