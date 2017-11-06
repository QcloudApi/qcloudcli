# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteLifeCycleHookRequest(Request):

    def __init__(self):
        super(DeleteLifeCycleHookRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DeleteLifeCycleHook', 'scaling.api.qcloud.com')

    def get_lifeCycleHookId(self):
        return self.get_params().get('lifeCycleHookId')

    def set_lifeCycleHookId(self, lifeCycleHookId):
        self.add_param('lifeCycleHookId', lifeCycleHookId)

    def get_lifeCycleHookName(self):
        return self.get_params().get('lifeCycleHookName')

    def set_lifeCycleHookName(self, lifeCycleHookName):
        self.add_param('lifeCycleHookName', lifeCycleHookName)

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)
