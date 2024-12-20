#!/usr/bin/env python3
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

client = __import__('client')


class TestGithubOrgClient(TestCase):
    """
    Test case for GithubOrgClient class.
    """
    @parameterized.expand([
        ('google', {"payload": True}),
        ('abc', {"payload": False})
    ])
    @patch('client.get_json')
    def test_org(self, org, test_payload, mock_get_json):
        """
        Tests for the memoized org method of the GithubOrgClient class.
        Purpose
        -------
        To mock get_json function.
        To make sure org method returns the proper value(dict).
        
        Arguments
        ---------
        org:
            org_name argument passed into mocked function.
        test_payload:
            expected dict return value.
        mock_get_json:
            mock object of the get_json function.
        """
        mock_get_json.return_value = test_payload

        github_org_client_object = client.GithubOrgClient(org)

        result = github_org_client_object.org

        mock_get_json.assert_called_once_with(client.GithubOrgClient.ORG_URL.format(org=org))

        self.assertEqual(result, test_payload)
    
    @parameterized.expand([
    ('google', {"repos_url": "google"}),
    ('abc', {"repos_url": "abc"})
])
    def test_public_repos_url(self, org, test_payload):
        """
        Tests for the _public_repos_url property of the GithubOrgClient class.
        Purpose
        -------
        To mock org memoized method.
        To make sure property returns the proper value(str).
        
        Arguments
        ---------
        org:
            org_name argument passed into mocked function.
        test_payload:
            expected dict return value.
        """
        github_org_client_object = client.GithubOrgClient(org)

        with patch.object(client.GithubOrgClient, 'org', return_value=test_payload):
            result = github_org_client_object._public_repos_url

            self.assertEqual(result, test_payload['repos_url'])

