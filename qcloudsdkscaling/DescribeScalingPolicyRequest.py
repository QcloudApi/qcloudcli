# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeScalingPolicyRequest(Request):

    def __init__(self):
        super(DescribeScalingPolicyRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DescribeScalingPolicy', 'scaling.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)

    def get_scalingPolicyIds(self):
        return self.get_params().get('scalingPolicyIds')

    def set_scalingPolicyIds(self, scalingPolicyIds):
        self.add_param('scalingPolicyIds', scalingPolicyIds)

    def get_scalingPolicyName(self):
        return self.get_params().get('scalingPolicyName')

    def set_scalingPolicyName(self, scalingPolicyName):
        self.add_param('scalingPolicyName', scalingPolicyName)
