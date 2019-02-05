import unittest
from app.models import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        self.new_source = NewsSource('abc-news','ABC News', "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com","general",'en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,NewsSource))    
