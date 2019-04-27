from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


class ProfileModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(username="user1", password="123123")
        user2 = User.objects.create(email="user2", password="123123")
        cls.profile1 = Profile.objects.get(user=user1)
        cls.profile2 = Profile.objects.get(user=user2)

    def test_empty_followers(self):
        self.assertIs(self.profile1.followers.all().count(), 0)

    def test_add_followers(self):
        self.profile1.followers.add(self.profile2)
        self.assertIs(self.profile2.followings.all().count(), 1)

    def test_empty_followings(self):
        self.assertIs(self.profile1.followings.all().count(), 0)
