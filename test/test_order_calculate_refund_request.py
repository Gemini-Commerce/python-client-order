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

from order.models.order_calculate_refund_request import OrderCalculateRefundRequest

class TestOrderCalculateRefundRequest(unittest.TestCase):
    """OrderCalculateRefundRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCalculateRefundRequest:
        """Test OrderCalculateRefundRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCalculateRefundRequest`
        """
        model = OrderCalculateRefundRequest()
        if include_optional:
            return OrderCalculateRefundRequest(
                tenant_id = '',
                payment_id = '',
                items = [
                    order.models.order_refund_item.orderRefundItem(
                        order_item_id = '', 
                        qty = 56, )
                    ],
                shipping = True
            )
        else:
            return OrderCalculateRefundRequest(
                tenant_id = '',
                payment_id = '',
        )
        """

    def testOrderCalculateRefundRequest(self):
        """Test OrderCalculateRefundRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
