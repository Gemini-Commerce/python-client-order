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

from order.models.update_order_request_payload import UpdateOrderRequestPayload

class TestUpdateOrderRequestPayload(unittest.TestCase):
    """UpdateOrderRequestPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateOrderRequestPayload:
        """Test UpdateOrderRequestPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateOrderRequestPayload`
        """
        model = UpdateOrderRequestPayload()
        if include_optional:
            return UpdateOrderRequestPayload(
                billing_address = order.models.order_postal_address.orderPostalAddress(
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
                shipping_address = order.models.order_postal_address.orderPostalAddress(
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
                additional_info = None
            )
        else:
            return UpdateOrderRequestPayload(
        )
        """

    def testUpdateOrderRequestPayload(self):
        """Test UpdateOrderRequestPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
