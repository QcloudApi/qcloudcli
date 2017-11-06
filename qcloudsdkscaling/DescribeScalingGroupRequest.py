# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeScalingGroupRequest(Request):

    def __init__(self):
        super(DescribeScalingGroupRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DescribeScalingGroup', 'scaling.api.qcloud.com')

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

    def get_scalingConfigurationId(self):
        return self.get_params().get('scalingConfigurationId')

    def set_scalingConfigurationId(self, scalingConfigurationId):
        self.add_param('scalingConfigurationId', scalingConfigurationId)

    def get_scalingGroupIds(self):
        return self.get_params().get('scalingGroupIds')

    def set_scalingGroupIds(self, scalingGroupIds):
        self.add_param('scalingGroupIds', scalingGroupIds)

    def get_scalingGroupName(self):
        return self.get_params().get('scalingGroupName')

    def set_scalingGroupName(self, scalingGroupName):
        self.add_param('scalingGroupName', scalingGroupName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
