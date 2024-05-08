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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from order.models.order_order_by import OrderOrderBy
from order.models.order_payment_filter import OrderPaymentFilter
from order.models.order_status_filter import OrderStatusFilter
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderSearchOrdersRequest(BaseModel):
    """
    OrderSearchOrdersRequest
    """ # noqa: E501
    tenant_id: StrictStr = Field(alias="tenantId")
    search_query: Optional[StrictStr] = Field(default=None, alias="searchQuery")
    page_size: Optional[StrictInt] = Field(default=None, description="The maximum number of orders to return. The service may return fewer than this value. If unspecified, at most 10 orders will be returned. The maximum value is 100; values above 100 will be coerced to 100.", alias="pageSize")
    page_token: Optional[StrictStr] = Field(default=None, description="A page token, received from a previous `ListOrders` call. Provide this to retrieve the subsequent page.   When paginating, all other parameters provided to `ListOrders` must match the call that provided the page token.", alias="pageToken")
    order_by: Optional[List[OrderOrderBy]] = Field(default=None, alias="orderBy")
    status_filter: Optional[OrderStatusFilter] = Field(default=None, alias="statusFilter")
    from_date: Optional[datetime] = Field(default=None, alias="fromDate")
    to_date: Optional[datetime] = Field(default=None, alias="toDate")
    payment_filter: Optional[OrderPaymentFilter] = Field(default=None, alias="paymentFilter")
    agent_grn: Optional[StrictStr] = Field(default=None, alias="agentGrn")
    updated_at_from: Optional[datetime] = Field(default=None, alias="updatedAtFrom")
    updated_at_to: Optional[datetime] = Field(default=None, alias="updatedAtTo")
    __properties: ClassVar[List[str]] = ["tenantId", "searchQuery", "pageSize", "pageToken", "orderBy", "statusFilter", "fromDate", "toDate", "paymentFilter", "agentGrn", "updatedAtFrom", "updatedAtTo"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OrderSearchOrdersRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in order_by (list)
        _items = []
        if self.order_by:
            for _item in self.order_by:
                if _item:
                    _items.append(_item.to_dict())
            _dict['orderBy'] = _items
        # override the default output from pydantic by calling `to_dict()` of status_filter
        if self.status_filter:
            _dict['statusFilter'] = self.status_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_filter
        if self.payment_filter:
            _dict['paymentFilter'] = self.payment_filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderSearchOrdersRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "searchQuery": obj.get("searchQuery"),
            "pageSize": obj.get("pageSize"),
            "pageToken": obj.get("pageToken"),
            "orderBy": [OrderOrderBy.from_dict(_item) for _item in obj.get("orderBy")] if obj.get("orderBy") is not None else None,
            "statusFilter": OrderStatusFilter.from_dict(obj.get("statusFilter")) if obj.get("statusFilter") is not None else None,
            "fromDate": obj.get("fromDate"),
            "toDate": obj.get("toDate"),
            "paymentFilter": OrderPaymentFilter.from_dict(obj.get("paymentFilter")) if obj.get("paymentFilter") is not None else None,
            "agentGrn": obj.get("agentGrn"),
            "updatedAtFrom": obj.get("updatedAtFrom"),
            "updatedAtTo": obj.get("updatedAtTo")
        })
        return _obj


