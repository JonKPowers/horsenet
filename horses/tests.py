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

    def test_horses_returns_correct_html(self):
        response = self.client.get('/horsenet/horses.html')
        self.assertTemplateUsed(response, 'horses.html')

    def test_races_returns_correct_html(self):
        response = self.client.get('/horsenet/races.html')
        self.assertTemplateUsed(response, 'races.html')

    def test_tracks_returns_correct_html(self):
        response = self.client.get('/horsenet/tracks.html')
        self.assertTemplateUsed(response, 'tracks.html')

    def test_deepnet_returns_correct_html(self):
        response = self.client.get('/horsenet/deepnet.html')
        self.assertTemplateUsed(response, 'deepnet.html')
