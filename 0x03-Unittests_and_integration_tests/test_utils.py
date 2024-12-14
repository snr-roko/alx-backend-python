#!/usr/bin/env python3

from unittest import TestCase
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