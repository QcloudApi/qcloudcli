# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyLocalSourceIPPortTranslationNatRuleRequest(Request):

    def __init__(self):
        super(ModifyLocalSourceIPPortTranslationNatRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyLocalSourceIPPortTranslationNatRule', 'vpc.api.qcloud.com')

    def get_description(self):
        return self.get_params().get('description')

    def set_description(self, description):
        self.add_param('description', description)

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_oldTranslationIPPool(self):
        return self.get_params().get('oldTranslationIPPool')

    def set_oldTranslationIPPool(self, oldTranslationIPPool):
        self.add_param('oldTranslationIPPool', oldTranslationIPPool)

    def get_translationIPPool(self):
        return self.get_params().get('translationIPPool')

    def set_translationIPPool(self, translationIPPool):
        self.add_param('translationIPPool', translationIPPool)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
