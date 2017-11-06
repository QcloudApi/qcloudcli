# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreatePeerIPTranslationNatRuleRequest(Request):

    def __init__(self):
        super(CreatePeerIPTranslationNatRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreatePeerIPTranslationNatRule', 'vpc.api.qcloud.com')

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_peerIPTranslation(self):
        return self.get_params().get('peerIPTranslation')

    def set_peerIPTranslation(self, peerIPTranslation):
        self.add_param('peerIPTranslation', peerIPTranslation)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
