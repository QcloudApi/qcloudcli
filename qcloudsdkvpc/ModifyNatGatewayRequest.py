# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyNatGatewayRequest(Request):

    def __init__(self):
        super(ModifyNatGatewayRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyNatGateway', 'vpc.api.qcloud.com')

    def get_bandwidth(self):
        return self.get_params().get('bandwidth')

    def set_bandwidth(self, bandwidth):
        self.add_param('bandwidth', bandwidth)

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
