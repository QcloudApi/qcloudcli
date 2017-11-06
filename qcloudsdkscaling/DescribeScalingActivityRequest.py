# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeScalingActivityRequest(Request):

    def __init__(self):
        super(DescribeScalingActivityRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DescribeScalingActivity', 'scaling.api.qcloud.com')

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_scalingActivityIds(self):
        return self.get_params().get('scalingActivityIds')

    def set_scalingActivityIds(self, scalingActivityIds):
        self.add_param('scalingActivityIds', scalingActivityIds)

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)
