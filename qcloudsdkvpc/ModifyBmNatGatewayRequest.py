# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyBmNatGatewayRequest(Request):

    def __init__(self):
        super(ModifyBmNatGatewayRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyBmNatGateway', 'vpc.api.qcloud.com')

    def get_natId(self):
        return self.get_params().get('natId')

    def set_natId(self, natId):
        self.add_param('natId', natId)

    def get_natName(self):
        return self.get_params().get('natName')

    def set_natName(self, natName):
        self.add_param('natName', natName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
