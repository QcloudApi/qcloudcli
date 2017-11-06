# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AttachNetworkInterfaceRequest(Request):

    def __init__(self):
        super(AttachNetworkInterfaceRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'AttachNetworkInterface', 'vpc.api.qcloud.com')

    def get_instanceId(self):
        return self.get_params().get('instanceId')

    def set_instanceId(self, instanceId):
        self.add_param('instanceId', instanceId)

    def get_networkInterfaceId(self):
        return self.get_params().get('networkInterfaceId')

    def set_networkInterfaceId(self, networkInterfaceId):
        self.add_param('networkInterfaceId', networkInterfaceId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
