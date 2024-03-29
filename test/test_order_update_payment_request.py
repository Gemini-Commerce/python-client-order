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

from order.models.order_update_payment_request import OrderUpdatePaymentRequest

class TestOrderUpdatePaymentRequest(unittest.TestCase):
    """OrderUpdatePaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderUpdatePaymentRequest:
        """Test OrderUpdatePaymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderUpdatePaymentRequest`
        """
        model = OrderUpdatePaymentRequest()
        if include_optional:
            return OrderUpdatePaymentRequest(
                tenant_id = '',
                payment_id = '',
                cc_info = order.models.payment_cc_info.PaymentCcInfo(
                    approval = '', 
                    exp_month = 56, 
                    exp_year = '', 
                    last4 = '', 
                    number_enc = '', 
                    owner = '', 
                    avs_status = '', 
                    type = '', )
            )
        else:
            return OrderUpdatePaymentRequest(
                tenant_id = '',
                payment_id = '',
        )
        """

    def testOrderUpdatePaymentRequest(self):
        """Test OrderUpdatePaymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
