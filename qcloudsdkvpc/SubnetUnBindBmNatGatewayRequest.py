# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SubnetUnBindBmNatGatewayRequest(Request):

    def __init__(self):
        super(SubnetUnBindBmNatGatewayRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'SubnetUnBindBmNatGateway', 'vpc.api.qcloud.com')

    def get_natId(self):
        return self.get_params().get('natId')

    def set_natId(self, natId):
        self.add_param('natId', natId)

    def get_subnetIds(self):
        return self.get_params().get('subnetIds')

    def set_subnetIds(self, subnetIds):
        self.add_param('subnetIds', subnetIds)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
