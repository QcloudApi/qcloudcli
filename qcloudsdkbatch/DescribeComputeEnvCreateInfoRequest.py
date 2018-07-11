# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeComputeEnvCreateInfoRequest(Request):

    def __init__(self):
        super(DescribeComputeEnvCreateInfoRequest, self).__init__(
            'batch', 'qcloudcliV1', 'DescribeComputeEnvCreateInfo', 'batch.api.qcloud.com')

    def get_EnvId(self):
        return self.get_params().get('EnvId')

    def set_EnvId(self, EnvId):
        self.add_param('EnvId', EnvId)

    def get_Version(self):
        return self.get_params().get('Version')

    def set_Version(self, Version):
        self.add_param('Version', Version)
