# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DetachLifeCycleHookIdRequest(Request):

    def __init__(self):
        super(DetachLifeCycleHookIdRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DetachLifeCycleHookId', 'scaling.api.qcloud.com')

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)
