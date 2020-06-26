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
from openlattice-rundeck.models.job_execution_delete import JobExecutionDelete  # noqa: E501
from openlattice-rundeck.rest import ApiException

class TestJobExecutionDelete(unittest.TestCase):
    """JobExecutionDelete unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobExecutionDelete
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openlattice-rundeck.models.job_execution_delete.JobExecutionDelete()  # noqa: E501
        if include_optional :
            return JobExecutionDelete(
                failed_count = 1.337, 
                success_count = 1.337, 
                allsuccessful = True, 
                request_count = 1.337, 
                failures = [
                    openlattice-rundeck.models.job_execution_delete_failures.JobExecutionDelete_failures(
                        id = '0', 
                        message = '0', )
                    ]
            )
        else :
            return JobExecutionDelete(
        )

    def testJobExecutionDelete(self):
        """Test JobExecutionDelete"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()