# coding: utf-8

"""
    Rundeck

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openlattice-rundeck
from openlattice-rundeck.models.takeover_schedule_request import TakeoverScheduleRequest  # noqa: E501
from openlattice-rundeck.rest import ApiException

class TestTakeoverScheduleRequest(unittest.TestCase):
    """TakeoverScheduleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TakeoverScheduleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openlattice-rundeck.models.takeover_schedule_request.TakeoverScheduleRequest()  # noqa: E501
        if include_optional :
            return TakeoverScheduleRequest(
                server = None, 
                project = '0', 
                job = None
            )
        else :
            return TakeoverScheduleRequest(
        )

    def testTakeoverScheduleRequest(self):
        """Test TakeoverScheduleRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()