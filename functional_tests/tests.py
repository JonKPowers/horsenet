from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import SimpleTestCase
import time

class PageSetupTest(SimpleTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.test_url = 'http://localhost:8000/horsenet/'

    def tearDown(self):
        self.browser.quit()

    def testHomePageSetup(self):
        self.browser.get(self.test_url)
        # Title should include HorseNet
        self.assertIn('HorseNet', self.browser.title)

        # Should have menu items at the top for:

        # Home
        menu_link_home = self.browser.find_element_by_id('menu_link_home')
        self.assertIn('HorseNet', menu_link_home.text)
        # Horses
        menu_link_horses = self.browser.find_element_by_id('menu_link_horses')
        self.assertIn('Horses', menu_link_horses.text) 
        # Races
        menu_link_races = self.browser.find_element_by_id('menu_link_races')
        self.assertIn('Races', menu_link_races.text)
        # Tracks
        menu_link_tracks = self.browser.find_element_by_id('menu_link_tracks')
        self.assertIn('Tracks', menu_link_tracks.text)
        # DeepNet
        menu_link_deepnet = self.browser.find_element_by_id('menu_link_deepnet')
        self.assertIn('DeepNet', menu_link_deepnet.text)
        # [Reserved]
        menu_link_reserved = self.browser.find_element_by_id('menu_link_reserved')
        self.assertIn('[Reserved]', menu_link_reserved.text)

        # Check that links work
        links = {
            'menu_link_home': 'Home',
            'menu_link_horses': 'Horses',
            'menu_link_races': 'Races',
            'menu_link_tracks': 'Tracks',
            'menu_link_deepnet': 'DeepNet',
            }

        for link, title in links.items():
            self.browser.get(self.test_url)
            link = self.browser.find_element_by_id(link)                    
            link.click()
            self.assertIn(title, self.browser.title)


        self.fail('Finish the tests!')

