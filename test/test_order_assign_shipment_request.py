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

from order.models.order_assign_shipment_request import OrderAssignShipmentRequest

class TestOrderAssignShipmentRequest(unittest.TestCase):
    """OrderAssignShipmentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderAssignShipmentRequest:
        """Test OrderAssignShipmentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderAssignShipmentRequest`
        """
        model = OrderAssignShipmentRequest()
        if include_optional:
            return OrderAssignShipmentRequest(
                tenant_id = '',
                shipment_id = ''
            )
        else:
            return OrderAssignShipmentRequest(
        )
        """

    def testOrderAssignShipmentRequest(self):
        """Test OrderAssignShipmentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()