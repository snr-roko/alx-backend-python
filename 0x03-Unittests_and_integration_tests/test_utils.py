#!/usr/bin/env python3
"""Module for testing utility functions."""

from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
import unittest

utils = __import__("utils")
memoize = utils.memoize


class TestAccessNestedMap(TestCase):
    """Tests for utils.access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """Test access_nested_map returns correct values.

        Parameters
        ----------
        nested_map : Mapping
            A nested map
        path : Sequence
            A sequence of keys representing a path to the value
        expected_value : Any
            Expected return value from the function
        """
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected_value)

    @parameterized.expand([
        ({}, ('a',), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(
        self, nested_map, path, expected_error_message):
        """Test access_nested_map raises correct exceptions.

        Parameters
        ----------
        nested_map : Mapping
            A nested map
        path : Sequence
            A sequence of keys representing a path to the value
        expected_error_message : str
            Expected error message from KeyError exception
        """
        with self.assertRaises(KeyError) as map_context:
            utils.access_nested_map(nested_map, path)

        self.assertEqual(str(map_context.exception), expected_error_message)


class TestGetJson(TestCase):
    """Tests for utils.get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_request_get):
        """Test get_json returns correct JSON payload.

        Parameters
        ----------
        test_url : str
            URL to mock request to
        test_payload : dict
            Expected JSON response
        mock_request_get : Mock
            Mock object for patched request.get
        """
        new_mock = Mock()
        new_mock.json.return_value = test_payload

        mock_request_get.return_value = new_mock
        result = utils.get_json(test_url)

        mock_request_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for utils.memoize decorator."""

    def test_memoize(self):
        """Test memoize decorator caches method results correctly.

        Verifies that the decorated method is called only once
        and its result is properly cached.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_object = TestClass()

        with patch.object(TestClass, 'a_method') as a_method_mock:
            a_method_mock.return_value = 42

            response1 = test_object.a_property
            response2 = test_object.a_property

            self.assertEqual(response1, 42)
            a_method_mock.assert_called_once()
