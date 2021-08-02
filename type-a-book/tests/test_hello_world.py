from unittest import TestCase

class TestHelloWorld(TestCase):

    def test_hello_world_pass(self):
        assert "hello" != "world"

    def test_hello_world_fail(self):
        self.assertEqual("hello", "hello")
