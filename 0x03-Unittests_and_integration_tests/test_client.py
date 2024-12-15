#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized

client = __import__('client')


class TestGithubOrgClient(unittest.TestCase):
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
