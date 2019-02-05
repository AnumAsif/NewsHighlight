import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(TechCrunch, ""http://techcrunch.com/2019/01/21/digital-garage-teams-up-with-blockstream-to-develop-blockchain-financial-services-in-japan/", "Jon Russell", ""https://techcrunch.com/wp-content/uploads/2017/03/bitcoin-on-gold.png?w=711", "The global crypto market may have tanked last year, but notable names have joined forces to develop Bitcoin and blockchain financial services in Japan, which has emerged as one of the world’s most crypto-friendly markets. Blockstream, a blockchain startup fou…", "The global crypto market may have tanked last year, but notable names have joined forces to develop Bitcoin and blockchain financial services in Japan, which has emerged as one of the world’s most crypto-friendly markets.\r\nBlockstream, a blockchain startup fo… [+1970 chars]", 20:21)

        def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
