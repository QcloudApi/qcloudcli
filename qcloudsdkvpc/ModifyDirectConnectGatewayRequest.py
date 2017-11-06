# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyDirectConnectGatewayRequest(Request):

    def __init__(self):
        super(ModifyDirectConnectGatewayRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyDirectConnectGateway', 'vpc.api.qcloud.com')

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_directConnectGatewayName(self):
        return self.get_params().get('directConnectGatewayName')

    def set_directConnectGatewayName(self, directConnectGatewayName):
        self.add_param('directConnectGatewayName', directConnectGatewayName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
