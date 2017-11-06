# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeScalingConfigurationRequest(Request):

    def __init__(self):
        super(DescribeScalingConfigurationRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DescribeScalingConfiguration', 'scaling.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_scalingConfigurationIds(self):
        return self.get_params().get('scalingConfigurationIds')

    def set_scalingConfigurationIds(self, scalingConfigurationIds):
        self.add_param('scalingConfigurationIds', scalingConfigurationIds)

    def get_scalingConfigurationName(self):
        return self.get_params().get('scalingConfigurationName')

    def set_scalingConfigurationName(self, scalingConfigurationName):
        self.add_param('scalingConfigurationName', scalingConfigurationName)
