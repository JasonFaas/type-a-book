import unittest
import requests
import os

class TestAwsLambda(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        current_user_home_dir = os.path.expanduser('~')
        with open('%s/.aws/lambda_url.txt' % current_user_home_dir, 'r') as file:
            cls.aws_url = file.read()[:-1]

    def test_ping(self):
        requests.get("%s/transactionStage/transactions/?transactionId=5&type=PURCHASE&amount=300" % self.aws_url)
