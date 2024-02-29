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

from order.models.order_create_refund_transaction_request import OrderCreateRefundTransactionRequest

class TestOrderCreateRefundTransactionRequest(unittest.TestCase):
    """OrderCreateRefundTransactionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateRefundTransactionRequest:
        """Test OrderCreateRefundTransactionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateRefundTransactionRequest`
        """
        model = OrderCreateRefundTransactionRequest()
        if include_optional:
            return OrderCreateRefundTransactionRequest(
                tenant_id = '',
                refund_id = '',
                parent_transaction_id = '',
                type = 'UNKNOWN',
                additional_info = ''
            )
        else:
            return OrderCreateRefundTransactionRequest(
        )
        """

    def testOrderCreateRefundTransactionRequest(self):
        """Test OrderCreateRefundTransactionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
