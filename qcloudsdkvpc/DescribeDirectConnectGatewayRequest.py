# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeDirectConnectGatewayRequest(Request):

    def __init__(self):
        super(DescribeDirectConnectGatewayRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeDirectConnectGateway', 'vpc.api.qcloud.com')

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_directConnectGatewayName(self):
        return self.get_params().get('directConnectGatewayName')

    def set_directConnectGatewayName(self, directConnectGatewayName):
        self.add_param('directConnectGatewayName', directConnectGatewayName)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_orderDirection(self):
        return self.get_params().get('orderDirection')

    def set_orderDirection(self, orderDirection):
        self.add_param('orderDirection', orderDirection)

    def get_orderField(self):
        return self.get_params().get('orderField')

    def set_orderField(self, orderField):
        self.add_param('orderField', orderField)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
