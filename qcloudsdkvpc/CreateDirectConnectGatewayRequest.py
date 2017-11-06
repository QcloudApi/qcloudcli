# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateDirectConnectGatewayRequest(Request):

    def __init__(self):
        super(CreateDirectConnectGatewayRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateDirectConnectGateway', 'vpc.api.qcloud.com')

    def get_directConnectGatewayName(self):
        return self.get_params().get('directConnectGatewayName')

    def set_directConnectGatewayName(self, directConnectGatewayName):
        self.add_param('directConnectGatewayName', directConnectGatewayName)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
