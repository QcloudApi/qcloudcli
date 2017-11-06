# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeScalingInstanceRequest(Request):

    def __init__(self):
        super(DescribeScalingInstanceRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DescribeScalingInstance', 'scaling.api.qcloud.com')

    def get_creationType(self):
        return self.get_params().get('creationType')

    def set_creationType(self, creationType):
        self.add_param('creationType', creationType)

    def get_healthStatus(self):
        return self.get_params().get('healthStatus')

    def set_healthStatus(self, healthStatus):
        self.add_param('healthStatus', healthStatus)

    def get_instanceIds(self):
        return self.get_params().get('instanceIds')

    def set_instanceIds(self, instanceIds):
        self.add_param('instanceIds', instanceIds)

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
