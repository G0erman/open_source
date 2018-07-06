#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `open_source` package."""

# Local imports
from open_source import open_source


def test_palindrome():
    assert open_source.check_palindrome("oso") == True
    assert open_source.check_palindrome("Oso") == True
    assert open_source.check_palindrome("()()") == False
    assert open_source.check_palindrome(")(()") == True
    assert open_source.check_palindrome("Hola") == False

def test_random_int():
    open_source
    assert True


def test_random_letter():
    open_source
    assert True
