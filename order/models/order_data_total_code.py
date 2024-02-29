# coding: utf-8

"""
    order Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class OrderDataTotalCode(str, Enum):
    """
    OrderDataTotalCode
    """

    """
    allowed enum values
    """
    UNKNOWN = 'UNKNOWN'
    ORDERED = 'ORDERED'
    PAID = 'PAID'
    REFUNDED = 'REFUNDED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OrderDataTotalCode from a JSON string"""
        return cls(json.loads(json_str))


