import unittest
import requests

class TestAwsLambda(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('/Users/jasonoclaf/.aws/lambda_url.txt', 'r') as file:
            cls.aws_url = file.read()[:-1]

    def test_ping(self):
        requests.get("%s/transactionStage/transactions/?transactionId=5&type=PURCHASE&amount=300" % self.aws_url)
