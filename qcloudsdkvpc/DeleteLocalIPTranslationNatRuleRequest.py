# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteLocalIPTranslationNatRuleRequest(Request):

    def __init__(self):
        super(DeleteLocalIPTranslationNatRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DeleteLocalIPTranslationNatRule', 'vpc.api.qcloud.com')

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_localIPTranslation(self):
        return self.get_params().get('localIPTranslation')

    def set_localIPTranslation(self, localIPTranslation):
        self.add_param('localIPTranslation', localIPTranslation)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
