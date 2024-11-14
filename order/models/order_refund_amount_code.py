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


class OrderRefundAmountCode(str, Enum):
    """
    OrderRefundAmountCode
    """

    """
    allowed enum values
    """
    UNKNOWN = 'UNKNOWN'
    ORDERED = 'ORDERED'
    SHIPPING = 'SHIPPING'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OrderRefundAmountCode from a JSON string"""
        return cls(json.loads(json_str))


