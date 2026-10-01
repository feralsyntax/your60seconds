import unittest
from app.models import Comment


class CommentTest(unittest.TestCase):
    """
    test behavior of Pitch class
    """

    def setUp(self):
        """
        runs before every test
        """

        self.new_comment = Comment(comment_message='Such a pitch!')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))
