from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class PageSetupTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def testHomePageSetup(self):
        self.browser.get('http://localhost:8000/horsenet')
        # Title should include HorseNet
        self.assertIn('HorseNet', self.browser.title)

        # Should have links at the top for:

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
        self.assertIn('DeepNet', menu_link_tracks.text)

        # [Reserved]
        menu_link_reserved = self.browser.find_element_by_id('menu_link_reserved')
        self.assertIn('[Reserved]', menu_link_reserved.text)


        self.fail('Finish the tests!')

if __name__ == '__main__':
    unittest.main()
