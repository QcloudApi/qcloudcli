# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteScheduledTaskRequest(Request):

    def __init__(self):
        super(DeleteScheduledTaskRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DeleteScheduledTask', 'scaling.api.qcloud.com')

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)

    def get_scalingScheduledTaskId(self):
        return self.get_params().get('scalingScheduledTaskId')

    def set_scalingScheduledTaskId(self, scalingScheduledTaskId):
        self.add_param('scalingScheduledTaskId', scalingScheduledTaskId)
