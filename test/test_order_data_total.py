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

from order.models.order_data_total import OrderDataTotal

class TestOrderDataTotal(unittest.TestCase):
    """OrderDataTotal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDataTotal:
        """Test OrderDataTotal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDataTotal`
        """
        model = OrderDataTotal()
        if include_optional:
            return OrderDataTotal(
                code = 'UNKNOWN',
                value = order.models.order_money.orderMoney(
                    units = '', 
                    micros = 56, )
            )
        else:
            return OrderDataTotal(
        )
        """

    def testOrderDataTotal(self):
        """Test OrderDataTotal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
