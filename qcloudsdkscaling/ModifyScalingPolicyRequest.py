# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyScalingPolicyRequest(Request):

    def __init__(self):
        super(ModifyScalingPolicyRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'ModifyScalingPolicy', 'scaling.api.qcloud.com')

    def get_adjustmentType(self):
        return self.get_params().get('adjustmentType')

    def set_adjustmentType(self, adjustmentType):
        self.add_param('adjustmentType', adjustmentType)

    def get_adjustmentValue(self):
        return self.get_params().get('adjustmentValue')

    def set_adjustmentValue(self, adjustmentValue):
        self.add_param('adjustmentValue', adjustmentValue)

    def get_cooldown(self):
        return self.get_params().get('cooldown')

    def set_cooldown(self, cooldown):
        self.add_param('cooldown', cooldown)

    def get_metric(self):
        return self.get_params().get('metric')

    def set_metric(self, metric):
        self.add_param('metric', metric)

    def get_notifyIds(self):
        return self.get_params().get('notifyIds')

    def set_notifyIds(self, notifyIds):
        self.add_param('notifyIds', notifyIds)

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)

    def get_scalingPolicyId(self):
        return self.get_params().get('scalingPolicyId')

    def set_scalingPolicyId(self, scalingPolicyId):
        self.add_param('scalingPolicyId', scalingPolicyId)

    def get_scalingPolicyName(self):
        return self.get_params().get('scalingPolicyName')

    def set_scalingPolicyName(self, scalingPolicyName):
        self.add_param('scalingPolicyName', scalingPolicyName)
