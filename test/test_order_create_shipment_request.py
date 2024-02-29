# coding: utf-8

"""
    order Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from order.models.order_create_shipment_request import OrderCreateShipmentRequest

class TestOrderCreateShipmentRequest(unittest.TestCase):
    """OrderCreateShipmentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateShipmentRequest:
        """Test OrderCreateShipmentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateShipmentRequest`
        """
        model = OrderCreateShipmentRequest()
        if include_optional:
            return OrderCreateShipmentRequest(
                tenant_id = '',
                order_id = '',
                items = [
                    order.models.order_shipment_item.orderShipmentItem(
                        order_item_id = '', 
                        qty = 56, 
                        row_weight = '', )
                    ],
                address = order.models.order_postal_address.orderPostalAddress(
                    revision = 56, 
                    region_code = '', 
                    language_code = '', 
                    postal_code = '', 
                    sorting_code = '', 
                    administrative_area = '', 
                    locality = '', 
                    sublocality = '', 
                    address_lines = [
                        ''
                        ], 
                    recipients = [
                        ''
                        ], 
                    organization = '', 
                    phone_number = '', 
                    additional_info = order.models.additional_info.additionalInfo(), ),
                from_address = order.models.order_postal_address.orderPostalAddress(
                    revision = 56, 
                    region_code = '', 
                    language_code = '', 
                    postal_code = '', 
                    sorting_code = '', 
                    administrative_area = '', 
                    locality = '', 
                    sublocality = '', 
                    address_lines = [
                        ''
                        ], 
                    recipients = [
                        ''
                        ], 
                    organization = '', 
                    phone_number = '', 
                    additional_info = order.models.additional_info.additionalInfo(), ),
                return_address = order.models.order_postal_address.orderPostalAddress(
                    revision = 56, 
                    region_code = '', 
                    language_code = '', 
                    postal_code = '', 
                    sorting_code = '', 
                    administrative_area = '', 
                    locality = '', 
                    sublocality = '', 
                    address_lines = [
                        ''
                        ], 
                    recipients = [
                        ''
                        ], 
                    organization = '', 
                    phone_number = '', 
                    additional_info = order.models.additional_info.additionalInfo(), ),
                code = '',
                method = ''
            )
        else:
            return OrderCreateShipmentRequest(
        )
        """

    def testOrderCreateShipmentRequest(self):
        """Test OrderCreateShipmentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()