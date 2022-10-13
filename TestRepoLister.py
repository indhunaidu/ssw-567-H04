import unittest

#from RepoLister import countCommits, getRepoNames
import RepoLister
from unittest import mock

class TestCommitCounter(unittest.TestCase):

    @mock.patch("RepoLister.getRepoNames")
    def test_indhunaidu(self, mock_repoNames):
        mock_repoNames.return_value.names = ['SSW-567', 'SSW-567-WS', 'helloworld']
        response = RepoLister.getRepoNames('indhunaidu')
        self.assertNotEqual(response.names, [])
    @mock.patch("RepoLister.getRepoNames")
    def test_Repo1(self, mock_repoNames):
        mock_repoNames.return_value.names = ['SSW-567', 'SSW-567-WS', 'helloworld']
        response = RepoLister.getRepoNames('indhunaidu')
        self.assertIn('SSW-567-WS', response.names)
    @mock.patch("RepoLister.countCommits")
    def test_SSW567(self, mock_countCommits):
        mock_countCommits.return_value.commits = 11
        response = RepoLister.countCommits('indhunaidu', 'SSW-567')
        self.assertEqual(response.commits, 11)
    @mock.patch("RepoLister.countCommits")
    def test_SSW567WS(self, mock_countCommits):
        mock_countCommits.return_value.commits = 5
        response = RepoLister.countCommits('indhunaidu', 'SSW-567-WS')
        self.assertEqual(response.commits, 5)
    @mock.patch("RepoLister.countCommits")
    def test_helloworld(self, mock_countCommits):
        mock_countCommits.return_value.commits = 2
        response = RepoLister.countCommits('indhunaidu', 'helloworld')
        self.assertEqual(response.commits, 2)
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
    @mock.patch("RepoLister.getRepoNames")
    def mock_getRepoNames(mock_repoNames):
        mock_repoNames.return_value.ok = True
        response = RepoLister.getRepoNames('indhunaidu')
        print(response)
        print(mock_repoNames.return_value)

    mock_getRepoNames()