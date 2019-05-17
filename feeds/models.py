from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Feed(models.Model):
    # id 자동 추가
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    likers = models.ManyToManyField(User,
                                    blank=True,
                                    related_name='liked_feeds',
                                    through='Like')
    photo = models.ImageField(blank=True, upload_to='feed_photos')
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
            Feed.objects.create(title=fake.bs(), content=fake.text())


class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    # followers -> Follow -> User & User -> Follow -> followings
    followings = models.ManyToManyField('self',
                                     through='Follow',
                                     through_fields=('sender', 'receiver'),
                                     blank=True,
                                     related_name='followers',
                                     symmetrical=False)

    def __str__(self):
        return 'id=%d, user id=%d, college=%s, major=%s' % \
            (self.id, self.user.id, self.college, self.major)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        else:
            instance.profile.save()


class Follow(models.Model):
    sender = models.ForeignKey(Profile, related_name='sent_follows', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name='received_follows', on_delete=models.CASCADE)

    def __str__(self):
        return '%s follows %s' % (self.sender, self.receiver)
