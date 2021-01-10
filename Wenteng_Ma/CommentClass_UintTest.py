import unittest
from comment import Comment
comm = Comment(10, 20210111, '666')


class MyTestCase(unittest.TestCase):

    def test_post_comment(self):
        print('test_post_comment')
        self.assertEqual(comm.postComment(),True)

    def test_delete_owned_comment(self):
        print("test_delete_owned_comment")
        self.assertEqual(comm.deleteOwnedComment(),True)

if __name__ =='__main__':
    unittest.main()