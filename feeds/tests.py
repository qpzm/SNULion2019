from django.test import TestCase

# import datetime

from django.test import TestCase
# from django.utils import timezone

from .models import Profile, Follow
from django.contrib.auth.models import User


class ProfileModelTests(TestCase):

    def test_follows(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        profile_without_follow = Profile
        self.assertIs(future_question.was_published_recently(), False)
