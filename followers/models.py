from django.db import models
from django.contrib.auth.models import User

# This code is based on the DRF Code Institute walkthrough video


class Follower(models.Model):
    """
    Follower model, related to 'followed' and 'owner'.
    An owner is a User instance that follows another user.
    'followed' is the User that is followed by the owner (another user)
    We need the related_name attribute so that django can differentiate.
    between 'owner' and 'followed' who both are User model instances.
    By unique_together it is ensured you cannot follow a user twice.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
