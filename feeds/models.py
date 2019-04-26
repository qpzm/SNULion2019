from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User

from django.db.models.signals import post_save  # 추가
from django.dispatch import receiver   # 추가

# Create your models here.
class Feed(models.Model):
    # id 자동 추가
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.update_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def seed(n):
        fake = Faker('ko_kr')
        for _ in range(n):
            Feed.objects.create(
                title= fake.bs(),
                content= fake.text()
            )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return 'id=%d, user id=%d, college=%s, major=%s' % \
            (self.id, self.user.id, self.college, self.major)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        else:
            instance.profile.save()
