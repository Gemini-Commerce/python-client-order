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
from enum import Enum
from typing_extensions import Self


class OrderTransactionType(str, Enum):
    """
    OrderTransactionType
    """

    """
    allowed enum values
    """
    UNKNOWN = 'UNKNOWN'
    AUTHORIZATION = 'AUTHORIZATION'
    CAPTURE = 'CAPTURE'
    SALE = 'SALE'
    REFUND = 'REFUND'
    VOID = 'VOID'
    FAILED = 'FAILED'
    PENDING = 'PENDING'
    FRAUD = 'FRAUD'
    NOOP = 'NOOP'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OrderTransactionType from a JSON string"""
        return cls(json.loads(json_str))


