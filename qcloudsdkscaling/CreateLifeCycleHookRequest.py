# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateLifeCycleHookRequest(Request):

    def __init__(self):
        super(CreateLifeCycleHookRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'CreateLifeCycleHook', 'scaling.api.qcloud.com')

    def get_defaultResult(self):
        return self.get_params().get('defaultResult')

    def set_defaultResult(self, defaultResult):
        self.add_param('defaultResult', defaultResult)

    def get_lifeCycleHookName(self):
        return self.get_params().get('lifeCycleHookName')

    def set_lifeCycleHookName(self, lifeCycleHookName):
        self.add_param('lifeCycleHookName', lifeCycleHookName)

    def get_lifeCycleHookTimeout(self):
        return self.get_params().get('lifeCycleHookTimeout')

    def set_lifeCycleHookTimeout(self, lifeCycleHookTimeout):
        self.add_param('lifeCycleHookTimeout', lifeCycleHookTimeout)

    def get_notifyIds(self):
        return self.get_params().get('notifyIds')

    def set_notifyIds(self, notifyIds):
        self.add_param('notifyIds', notifyIds)

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)

    def get_transition(self):
        return self.get_params().get('transition')

    def set_transition(self, transition):
        self.add_param('transition', transition)
