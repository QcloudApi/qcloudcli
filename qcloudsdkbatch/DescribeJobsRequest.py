# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeJobsRequest(Request):

    def __init__(self):
        super(DescribeJobsRequest, self).__init__(
            'batch', 'qcloudcliV1', 'DescribeJobs', 'batch.api.qcloud.com')

    def get_Filters(self):
        return self.get_params().get('Filters')

    def set_Filters(self, Filters):
        self.add_param('Filters', Filters)

    def get_JobIds(self):
        return self.get_params().get('JobIds')

    def set_JobIds(self, JobIds):
        self.add_param('JobIds', JobIds)

    def get_Limit(self):
        return self.get_params().get('Limit')

    def set_Limit(self, Limit):
        self.add_param('Limit', Limit)

    def get_Offset(self):
        return self.get_params().get('Offset')

    def set_Offset(self, Offset):
        self.add_param('Offset', Offset)

    def get_Version(self):
        return self.get_params().get('Version')

    def set_Version(self, Version):
        self.add_param('Version', Version)
