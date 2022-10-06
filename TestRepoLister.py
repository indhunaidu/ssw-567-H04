import unittest

from RepoLister import countCommits, getRepoNames

class TestCommitCounter(unittest.TestCase):

    def test_indhunaidu(self):
        self.assertNotEqual(getRepoNames('indhunaidu'), [])
    def test_SSW567(self):
        self.assertEqual(countCommits('indhunaidu', 'SSW-567'), 11)
    def test_SSW567WS(self):
        self.assertEqual(countCommits('indhunaidu', 'SSW-567-WS'), 5)
    def test_helloworld(self):
        self.assertEqual(countCommits('indhunaidu', 'helloworld'), 2)
   
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()