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

from order.models.order_list_fulfillments_response import OrderListFulfillmentsResponse

class TestOrderListFulfillmentsResponse(unittest.TestCase):
    """OrderListFulfillmentsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderListFulfillmentsResponse:
        """Test OrderListFulfillmentsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderListFulfillmentsResponse`
        """
        model = OrderListFulfillmentsResponse()
        if include_optional:
            return OrderListFulfillmentsResponse(
                fulfillments = [
                    order.models.order_fulfillment.orderFulfillment(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        order_id = '', 
                        id = '', 
                        status = '', 
                        items = [
                            order.models.order_fulfillment_item.orderFulfillmentItem(
                                order_item_id = '', 
                                qty = 56, )
                            ], )
                    ]
            )
        else:
            return OrderListFulfillmentsResponse(
        )
        """

    def testOrderListFulfillmentsResponse(self):
        """Test OrderListFulfillmentsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()