from django.test import TestCase, Client
from django.urls import reverse
from account.models import UserBase
from blog.models import PostModel, Comment, Profile
from unittest.mock import patch


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = UserBase.objects.create_user(
            user_name="testuser", password="testpass123", email="test@gmail.com"
        )
        self.user.save()

        self.post = PostModel.objects.create(
            title="Test post title", content="Test post content", author=self.user
        )

        self.comment = Comment.objects.create(
            content="Test comment", user=self.user, post=self.post
        )

        self.profile = Profile.objects.create(
            user=self.user,
            firstname="Test",
            lastname="User",
            age=25,
            gender="M",
            website="http://test.com",
        )

    # def test_index_view(self):
    #     response = self.client.get(reverse("blog:blog-index"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "home.html")

    def test_add_post_view(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("blog:blog-post-add"),
            {"title": "New post", "content": "New post content"},
        )
        self.assertEqual(response.status_code, 302)

    @patch('blog.views.PostModel.objects.create')
    def test_add_post_view_w_mock(self, mock_post_create):
        mock_post_create.return_value = self.post
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("blog:blog-post-add"),
            {"title": "New post", "content": "New post content"},
        )
        self.assertEqual(response.status_code, 302)

    # def test_post_detail_view(self):
    #     response = self.client.get(
    #         reverse("blog:blog-post-detail", args=[self.post.id])
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "blog/post_detail.html")


    def test_post_edit_view(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("blog:blog-post-edit", args=[self.post.id]),
            {"title": "Updated post title", "content": "Updated post content"},
        )
        self.assertEqual(response.status_code, 302)

    def test_profile_edit_view(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("blog:profile_edit", args=[self.user.id]),
            {
                "firstname": "New Firstname",
                "lastname": "New Lastname",
                "age": 30,
                "gender": "F",
                "website": "http://newtest.com",
            },
        )
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        self.post.delete()
        self.user.delete()
        self.comment.delete()
        self.profile.delete()
