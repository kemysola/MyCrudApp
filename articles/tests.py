#from django.test import TestCase

# Create your tests here.
'''
from django.test import SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Article


# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='',
        )
        self.post = Article.objects.create(
            title='A good title',
            body='A nice body content',
            author='self.user'
        )
        
        
    def test_string_representation(self):
        post = Article(title='A new tile')
        self.assertEqual(str(post),post.title)
'''
'''
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'A nice body content')

    def test_articles_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.TemplateUsed(response, '/articles/articles.html')

    def test_articles_detail_view(self):
        response = self.client.get('/post/1/')
        no_response =self.client.get('/post/100000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response,  'A good title')
        self.assertTemplateUsed(response, 'articles/article_detail.html')
        
        '''









