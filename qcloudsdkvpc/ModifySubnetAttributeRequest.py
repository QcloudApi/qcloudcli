# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifySubnetAttributeRequest(Request):

    def __init__(self):
        super(ModifySubnetAttributeRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifySubnetAttribute', 'vpc.api.qcloud.com')

    def get_broadcast(self):
        return self.get_params().get('broadcast')

    def set_broadcast(self, broadcast):
        self.add_param('broadcast', broadcast)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_subnetName(self):
        return self.get_params().get('subnetName')

    def set_subnetName(self, subnetName):
        self.add_param('subnetName', subnetName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
