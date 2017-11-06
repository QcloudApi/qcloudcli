# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteLocalSourceIPPortTranslationNatRuleRequest(Request):

    def __init__(self):
        super(DeleteLocalSourceIPPortTranslationNatRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DeleteLocalSourceIPPortTranslationNatRule', 'vpc.api.qcloud.com')

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_localSourceIPPortTranslation(self):
        return self.get_params().get('localSourceIPPortTranslation')

    def set_localSourceIPPortTranslation(self, localSourceIPPortTranslation):
        self.add_param('localSourceIPPortTranslation', localSourceIPPortTranslation)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
