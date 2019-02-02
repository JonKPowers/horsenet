from selenium import webdriver
import unittest

class PageSetupTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def testPageSetup(self):
        # Title should include HorseNet
        self.assertIn('HorseNet', self.browser.title)

        self.fail('Finish the tests!')

if __name__ == '__main__':
    unittest.main()
