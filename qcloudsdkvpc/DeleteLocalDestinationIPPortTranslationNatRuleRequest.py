# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteLocalDestinationIPPortTranslationNatRuleRequest(Request):

    def __init__(self):
        super(DeleteLocalDestinationIPPortTranslationNatRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DeleteLocalDestinationIPPortTranslationNatRule', 'vpc.api.qcloud.com')

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_localDestinationIPPortTranslation(self):
        return self.get_params().get('localDestinationIPPortTranslation')

    def set_localDestinationIPPortTranslation(self, localDestinationIPPortTranslation):
        self.add_param('localDestinationIPPortTranslation', localDestinationIPPortTranslation)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
