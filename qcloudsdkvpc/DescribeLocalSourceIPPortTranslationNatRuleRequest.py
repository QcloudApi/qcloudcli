# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLocalSourceIPPortTranslationNatRuleRequest(Request):

    def __init__(self):
        super(DescribeLocalSourceIPPortTranslationNatRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeLocalSourceIPPortTranslationNatRule', 'vpc.api.qcloud.com')

    def get_description(self):
        return self.get_params().get('description')

    def set_description(self, description):
        self.add_param('description', description)

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
