# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyScalingGroupRequest(Request):

    def __init__(self):
        super(ModifyScalingGroupRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'ModifyScalingGroup', 'scaling.api.qcloud.com')

    def get_desiredCapacity(self):
        return self.get_params().get('desiredCapacity')

    def set_desiredCapacity(self, desiredCapacity):
        self.add_param('desiredCapacity', desiredCapacity)

    def get_forwardLBInfos(self):
        return self.get_params().get('forwardLBInfos')

    def set_forwardLBInfos(self, forwardLBInfos):
        self.add_param('forwardLBInfos', forwardLBInfos)

    def get_healthyCheckType(self):
        return self.get_params().get('healthyCheckType')

    def set_healthyCheckType(self, healthyCheckType):
        self.add_param('healthyCheckType', healthyCheckType)

    def get_loadBalancerIds(self):
        return self.get_params().get('loadBalancerIds')

    def set_loadBalancerIds(self, loadBalancerIds):
        self.add_param('loadBalancerIds', loadBalancerIds)

    def get_maxSize(self):
        return self.get_params().get('maxSize')

    def set_maxSize(self, maxSize):
        self.add_param('maxSize', maxSize)

    def get_minSize(self):
        return self.get_params().get('minSize')

    def set_minSize(self, minSize):
        self.add_param('minSize', minSize)

    def get_removePolicy(self):
        return self.get_params().get('removePolicy')

    def set_removePolicy(self, removePolicy):
        self.add_param('removePolicy', removePolicy)

    def get_scalingConfigurationId(self):
        return self.get_params().get('scalingConfigurationId')

    def set_scalingConfigurationId(self, scalingConfigurationId):
        self.add_param('scalingConfigurationId', scalingConfigurationId)

    def get_scalingGroupId(self):
        return self.get_params().get('scalingGroupId')

    def set_scalingGroupId(self, scalingGroupId):
        self.add_param('scalingGroupId', scalingGroupId)

    def get_scalingGroupName(self):
        return self.get_params().get('scalingGroupName')

    def set_scalingGroupName(self, scalingGroupName):
        self.add_param('scalingGroupName', scalingGroupName)

    def get_subnetIds(self):
        return self.get_params().get('subnetIds')

    def set_subnetIds(self, subnetIds):
        self.add_param('subnetIds', subnetIds)

    def get_zoneIds(self):
        return self.get_params().get('zoneIds')

    def set_zoneIds(self, zoneIds):
        self.add_param('zoneIds', zoneIds)
