#!/usr/bin/env python3
""" Auth class to manage the API authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    Authentication Class Template
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Placeholder method for authentication requirement.

        Args:
        - path (str): The path to check authentication for.
        - excluded_paths (List[str]): List of paths to
            exclude from authentication.

        Returns:
        - bool: True if authentication is required, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Placeholder method for obtaining the authorization header.

        Args:
        - request (Request): Flask request object.

        Returns:
        - str: Authorization header string.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder method for obtaining the current user.

        Args:
        - request (Request): Flask request object.

        Returns:
        - TypeVar('User'): Current user object.
        """
        return None
