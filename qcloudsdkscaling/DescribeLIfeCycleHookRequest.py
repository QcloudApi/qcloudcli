# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLIfeCycleHookRequest(Request):

    def __init__(self):
        super(DescribeLIfeCycleHookRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'DescribeLIfeCycleHook', 'scaling.api.qcloud.com')

    def get_defaultResult(self):
        return self.get_params().get('defaultResult')

    def set_defaultResult(self, defaultResult):
        self.add_param('defaultResult', defaultResult)

    def get_lifeCycleHookId(self):
        return self.get_params().get('lifeCycleHookId')

    def set_lifeCycleHookId(self, lifeCycleHookId):
        self.add_param('lifeCycleHookId', lifeCycleHookId)

    def get_lifeCycleHookName(self):
        return self.get_params().get('lifeCycleHookName')

    def set_lifeCycleHookName(self, lifeCycleHookName):
        self.add_param('lifeCycleHookName', lifeCycleHookName)

    def get_lifeCycleHookTimeout(self):
        return self.get_params().get('lifeCycleHookTimeout')

    def set_lifeCycleHookTimeout(self, lifeCycleHookTimeout):
        self.add_param('lifeCycleHookTimeout', lifeCycleHookTimeout)

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

    def get_transition(self):
        return self.get_params().get('transition')

    def set_transition(self, transition):
        self.add_param('transition', transition)
