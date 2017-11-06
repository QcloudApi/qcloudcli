# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeScheduledTaskRequest(Request):

    def __init__(self):
        super(DescribeScheduledTaskRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DescribeScheduledTask', 'scaling.api.qcloud.com')

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

    def get_scalingScheduledTaskIds(self):
        return self.get_params().get('scalingScheduledTaskIds')

    def set_scalingScheduledTaskIds(self, scalingScheduledTaskIds):
        self.add_param('scalingScheduledTaskIds', scalingScheduledTaskIds)

    def get_scalingScheduledTaskName(self):
        return self.get_params().get('scalingScheduledTaskName')

    def set_scalingScheduledTaskName(self, scalingScheduledTaskName):
        self.add_param('scalingScheduledTaskName', scalingScheduledTaskName)
