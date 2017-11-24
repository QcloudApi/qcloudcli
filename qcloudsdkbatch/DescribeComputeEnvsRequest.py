# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeComputeEnvsRequest(Request):

    def __init__(self):
        super(DescribeComputeEnvsRequest, self).__init__(
            'batch', 'qcloudcliV1', 'DescribeComputeEnvs', 'batch.api.qcloud.com')

    def get_EnvIds(self):
        return self.get_params().get('EnvIds')

    def set_EnvIds(self, EnvIds):
        self.add_param('EnvIds', EnvIds)

    def get_Filters(self):
        return self.get_params().get('Filters')

    def set_Filters(self, Filters):
        self.add_param('Filters', Filters)

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
