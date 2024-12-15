#!/usr/bin/env python3

from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized

utils = __import__("utils")

class TestAccessNestedMap(TestCase):
    """
    Tests for utils.access_nested_map function
    @parameterized.expand() decorator used to test multiple inputs
 
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """
            A unit test for the utils.access_nested_map function.
            Purpose
            -------
            To check for correct return values

            Parameters
            ----------
            nested_map: Mapping
                A nested map
            path: Sequence
                a sequence of key representing a path to the value
            expected_value:
                a value to check result of function against

        """
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected_value)

    @parameterized.expand([
        ({}, ('a',), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_error_message):
        """
            A unit test for the utils.access_nested_map function.
            Purpose
            -------
            To check for exceptions

            Parameters
            ----------
            nested_map: Mapping
                A nested map
            path: Sequence
                a sequence of key representing a path to the value
            expected_error_message:
                Error message to receive after KeyError exception

        """
        with self.assertRaises(KeyError) as map_context:
            utils.access_nested_map(nested_map, path)

        self.assertEqual(str(map_context.exception), expected_error_message)


class TestGetJson(TestCase):
    """
    Testcase for testing the utils.get_json function
    """
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_request_get):
        """
            A unit test for the utils.get_json function.
            Purpose
            -------
            To mock request.get and make sure it is called as well as return a json object

            Parameters
            ----------
            test_url:
                Url to mock request to
            test_payload:
                a json object expected to be returned
            mock_request_get:
                mock object from the fake patched request.get

        """
        new_mock = Mock()
        new_mock.json.return_value = test_payload

        mock_request_get.return_value = new_mock
        result = utils.get_json(test_url)

        mock_request_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()
            
        test_object = TestClass()
        
        with patch.object(TestClass, 'a_method') as a_method_mock:
            a_method_mock.return_value = 42
            
            response1 = test_object.a_property
            response2 = test_object.a_property

            self.assertEqual(response1, 42)
            a_method_mock.assert_called_once()