import pytest
from mixer.backend.django import mixer
from account.models import UserBase

from django.test import TestCase
from django.utils import timezone

from blog.models import Comment, PostModel, Profile


class PostModelTestCase(TestCase):

    def setUp(self):
        self.user = UserBase.objects.create_user(
            user_name='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.post = PostModel.objects.create(
            title='Test Post',
            content='This is a test post',
            author=self.user,
        )
        self.comment = Comment.objects.create(
            user=self.user,
            post=self.post,
            content='This is a comment'
        )

    def test_post_model_creation(self):
        post_count = PostModel.objects.count()
        self.assertEqual(post_count, 1)

    def test_post_model_str(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_post_model_comment_count(self):
        self.assertEqual(self.post.comment_count(), 1)

    def test_post_model_comments(self):
        self.assertQuerySetEqual(self.post.comments(), Comment.objects.all())

    def tearDown(self):
        self.post.delete()
        self.user.delete()
        self.comment.delete()


class CommentModelTest(TestCase):

    def setUp(self):
        self.user = UserBase.objects.create_user(
            email='test@test.com',
            user_name='test_user',
            password='testpass123'
        )
        self.post = PostModel.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user,
            date_created=timezone.now(),
        )
        self.comment = Comment.objects.create(
            user=self.user,
            post=self.post,
            content='This is a test comment content.',
        )

    def test_comment_model(self):
        comment = Comment.objects.get(id=self.comment.id)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.content, 'This is a test comment content.')

    def test_comment_string_representation(self):
        comment = Comment.objects.get(id=self.comment.id)
        expected_string = f'{comment.content}'
        self.assertEqual(str(comment), expected_string)

    def tearDown(self):
        self.post.delete()
        self.user.delete()
        self.comment.delete()


class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a test user
        test_user = UserBase.objects.create_user(
            email='testuser@test.com',
            user_name='testuser',
            password='testpass123'
        )
        test_user.save()

        # Create a test profile
        test_profile = Profile.objects.create(
            user=test_user,
            firstname='Test',
            lastname='User',
            age=25,
            gender='M',
            address='Test Address',
            website='http://test.com'
        )
        test_profile.save()

    def test_profile_string_representation(self):
        profile = Profile.objects.get(id=1)
        expected_string = f'{profile.user.user_name}'
        self.assertEqual(str(profile), expected_string)

    def test_profile_age_blank(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.age, 25)

    def test_profile_gender_blank(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.gender, 'M')

    def test_profile_address_blank(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.address, 'Test Address')

    def test_profile_website_blank(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.website, 'http://test.com')

    def test_profile_user_foreign_key(self):
        profile = Profile.objects.get(id=1)
        user = UserBase.objects.get(id=1)
        self.assertEqual(profile.user, user)

