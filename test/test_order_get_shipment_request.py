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

from order.models.order_get_shipment_request import OrderGetShipmentRequest

class TestOrderGetShipmentRequest(unittest.TestCase):
    """OrderGetShipmentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderGetShipmentRequest:
        """Test OrderGetShipmentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderGetShipmentRequest`
        """
        model = OrderGetShipmentRequest()
        if include_optional:
            return OrderGetShipmentRequest(
                tenant_id = '',
                id = ''
            )
        else:
            return OrderGetShipmentRequest(
        )
        """

    def testOrderGetShipmentRequest(self):
        """Test OrderGetShipmentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
