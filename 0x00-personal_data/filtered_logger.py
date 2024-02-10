#!/usr/bin/env python
"""This module is a filter logger module
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ returns the log message obfuscated
    """
    for field in fields:
        log_message = re.sub(f'{f}=.*?{separator}',
                             f'{f}={redaction}{separator}', message)
    return log_message
