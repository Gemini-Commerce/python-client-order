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

from order.models.print_orders_labels_response_failed_order import PrintOrdersLabelsResponseFailedOrder

class TestPrintOrdersLabelsResponseFailedOrder(unittest.TestCase):
    """PrintOrdersLabelsResponseFailedOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrintOrdersLabelsResponseFailedOrder:
        """Test PrintOrdersLabelsResponseFailedOrder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrintOrdersLabelsResponseFailedOrder`
        """
        model = PrintOrdersLabelsResponseFailedOrder()
        if include_optional:
            return PrintOrdersLabelsResponseFailedOrder(
                order_number = '',
                error_message = '',
                error_code = ''
            )
        else:
            return PrintOrdersLabelsResponseFailedOrder(
        )
        """

    def testPrintOrdersLabelsResponseFailedOrder(self):
        """Test PrintOrdersLabelsResponseFailedOrder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
