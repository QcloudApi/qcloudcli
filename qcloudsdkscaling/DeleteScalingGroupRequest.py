# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteScalingGroupRequest(Request):

    def __init__(self):
        super(DeleteScalingGroupRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DeleteScalingGroup', 'scaling.api.qcloud.com')

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)
