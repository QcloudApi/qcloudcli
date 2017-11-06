# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateSubnetRequest(Request):

    def __init__(self):
        super(CreateSubnetRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateSubnet', 'vpc.api.qcloud.com')

    def get_subnetSet(self):
        return self.get_params().get('subnetSet')

    def set_subnetSet(self, subnetSet):
        self.add_param('subnetSet', subnetSet)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
