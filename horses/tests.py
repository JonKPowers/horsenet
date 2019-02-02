from django.test import TestCase
from django.urls import resolve
from horses.views import index

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/horsenet/')
        self.assertEqual(found.func, index)

    def test_index_returns_correct_html(self):
        response = self.client.get('/horsenet/')
        self.assertTemplateUsed(response, 'index.html')
