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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from order.models.item_product_configuration_step import ItemProductConfigurationStep
from order.models.order_money import OrderMoney
from typing import Optional, Set
from typing_extensions import Self

class OrderOrderDataItem(BaseModel):
    """
    OrderOrderDataItem
    """ # noqa: E501
    id: Optional[StrictStr] = None
    product_grn: Optional[StrictStr] = Field(default=None, alias="productGrn")
    qty_ordered: Optional[StrictInt] = Field(default=None, alias="qtyOrdered")
    free_qty: Optional[StrictInt] = Field(default=None, alias="freeQty")
    qty_committed: Optional[StrictInt] = Field(default=None, alias="qtyCommitted")
    unit_sale_price: Optional[OrderMoney] = Field(default=None, alias="unitSalePrice")
    unit_list_price: Optional[OrderMoney] = Field(default=None, alias="unitListPrice")
    unit_base_price: Optional[OrderMoney] = Field(default=None, alias="unitBasePrice")
    unit_vat_amount: Optional[OrderMoney] = Field(default=None, alias="unitVatAmount")
    row_sale_price: Optional[OrderMoney] = Field(default=None, alias="rowSalePrice")
    row_list_price: Optional[OrderMoney] = Field(default=None, alias="rowListPrice")
    row_vat_amount: Optional[OrderMoney] = Field(default=None, alias="rowVatAmount")
    discount_amount: Optional[OrderMoney] = Field(default=None, alias="discountAmount")
    row_base_price: Optional[OrderMoney] = Field(default=None, alias="rowBasePrice")
    unit_custom_price: Optional[OrderMoney] = Field(default=None, alias="unitCustomPrice")
    row_custom_price: Optional[OrderMoney] = Field(default=None, alias="rowCustomPrice")
    vat_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="vatPercentage")
    vat_inaccurate: Optional[StrictBool] = Field(default=None, alias="vatInaccurate")
    vat_calculated: Optional[StrictBool] = Field(default=None, alias="vatCalculated")
    product_name: Optional[StrictStr] = Field(default=None, alias="productName")
    product_code: Optional[StrictStr] = Field(default=None, alias="productCode")
    product_sku: Optional[StrictStr] = Field(default=None, alias="productSku")
    product_options: Optional[StrictStr] = Field(default=None, alias="productOptions")
    product_img: Optional[StrictStr] = Field(default=None, alias="productImg")
    product_data: Optional[StrictStr] = Field(default=None, alias="productData")
    shipment_info_reference: Optional[StrictStr] = Field(default=None, alias="shipmentInfoReference")
    promotion_grn: Optional[List[StrictStr]] = Field(default=None, alias="promotionGrn")
    product_is_virtual: Optional[StrictBool] = Field(default=None, alias="productIsVirtual")
    product_configuration: Optional[List[ItemProductConfigurationStep]] = Field(default=None, alias="productConfiguration")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "productGrn", "qtyOrdered", "freeQty", "qtyCommitted", "unitSalePrice", "unitListPrice", "unitBasePrice", "unitVatAmount", "rowSalePrice", "rowListPrice", "rowVatAmount", "discountAmount", "rowBasePrice", "unitCustomPrice", "rowCustomPrice", "vatPercentage", "vatInaccurate", "vatCalculated", "productName", "productCode", "productSku", "productOptions", "productImg", "productData", "shipmentInfoReference", "promotionGrn", "productIsVirtual", "productConfiguration"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OrderOrderDataItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of unit_sale_price
        if self.unit_sale_price:
            _dict['unitSalePrice'] = self.unit_sale_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unit_list_price
        if self.unit_list_price:
            _dict['unitListPrice'] = self.unit_list_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unit_base_price
        if self.unit_base_price:
            _dict['unitBasePrice'] = self.unit_base_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unit_vat_amount
        if self.unit_vat_amount:
            _dict['unitVatAmount'] = self.unit_vat_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of row_sale_price
        if self.row_sale_price:
            _dict['rowSalePrice'] = self.row_sale_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of row_list_price
        if self.row_list_price:
            _dict['rowListPrice'] = self.row_list_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of row_vat_amount
        if self.row_vat_amount:
            _dict['rowVatAmount'] = self.row_vat_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount_amount
        if self.discount_amount:
            _dict['discountAmount'] = self.discount_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of row_base_price
        if self.row_base_price:
            _dict['rowBasePrice'] = self.row_base_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unit_custom_price
        if self.unit_custom_price:
            _dict['unitCustomPrice'] = self.unit_custom_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of row_custom_price
        if self.row_custom_price:
            _dict['rowCustomPrice'] = self.row_custom_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in product_configuration (list)
        _items = []
        if self.product_configuration:
            for _item_product_configuration in self.product_configuration:
                if _item_product_configuration:
                    _items.append(_item_product_configuration.to_dict())
            _dict['productConfiguration'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderOrderDataItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "productGrn": obj.get("productGrn"),
            "qtyOrdered": obj.get("qtyOrdered"),
            "freeQty": obj.get("freeQty"),
            "qtyCommitted": obj.get("qtyCommitted"),
            "unitSalePrice": OrderMoney.from_dict(obj["unitSalePrice"]) if obj.get("unitSalePrice") is not None else None,
            "unitListPrice": OrderMoney.from_dict(obj["unitListPrice"]) if obj.get("unitListPrice") is not None else None,
            "unitBasePrice": OrderMoney.from_dict(obj["unitBasePrice"]) if obj.get("unitBasePrice") is not None else None,
            "unitVatAmount": OrderMoney.from_dict(obj["unitVatAmount"]) if obj.get("unitVatAmount") is not None else None,
            "rowSalePrice": OrderMoney.from_dict(obj["rowSalePrice"]) if obj.get("rowSalePrice") is not None else None,
            "rowListPrice": OrderMoney.from_dict(obj["rowListPrice"]) if obj.get("rowListPrice") is not None else None,
            "rowVatAmount": OrderMoney.from_dict(obj["rowVatAmount"]) if obj.get("rowVatAmount") is not None else None,
            "discountAmount": OrderMoney.from_dict(obj["discountAmount"]) if obj.get("discountAmount") is not None else None,
            "rowBasePrice": OrderMoney.from_dict(obj["rowBasePrice"]) if obj.get("rowBasePrice") is not None else None,
            "unitCustomPrice": OrderMoney.from_dict(obj["unitCustomPrice"]) if obj.get("unitCustomPrice") is not None else None,
            "rowCustomPrice": OrderMoney.from_dict(obj["rowCustomPrice"]) if obj.get("rowCustomPrice") is not None else None,
            "vatPercentage": obj.get("vatPercentage"),
            "vatInaccurate": obj.get("vatInaccurate"),
            "vatCalculated": obj.get("vatCalculated"),
            "productName": obj.get("productName"),
            "productCode": obj.get("productCode"),
            "productSku": obj.get("productSku"),
            "productOptions": obj.get("productOptions"),
            "productImg": obj.get("productImg"),
            "productData": obj.get("productData"),
            "shipmentInfoReference": obj.get("shipmentInfoReference"),
            "promotionGrn": obj.get("promotionGrn"),
            "productIsVirtual": obj.get("productIsVirtual"),
            "productConfiguration": [ItemProductConfigurationStep.from_dict(_item) for _item in obj["productConfiguration"]] if obj.get("productConfiguration") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


