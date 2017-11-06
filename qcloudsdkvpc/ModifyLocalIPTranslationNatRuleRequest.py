# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyLocalIPTranslationNatRuleRequest(Request):

    def __init__(self):
        super(ModifyLocalIPTranslationNatRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyLocalIPTranslationNatRule', 'vpc.api.qcloud.com')

    def get_description(self):
        return self.get_params().get('description')

    def set_description(self, description):
        self.add_param('description', description)

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_oldOriginalIP(self):
        return self.get_params().get('oldOriginalIP')

    def set_oldOriginalIP(self, oldOriginalIP):
        self.add_param('oldOriginalIP', oldOriginalIP)

    def get_oldTranslationIP(self):
        return self.get_params().get('oldTranslationIP')

    def set_oldTranslationIP(self, oldTranslationIP):
        self.add_param('oldTranslationIP', oldTranslationIP)

    def get_originalIP(self):
        return self.get_params().get('originalIP')

    def set_originalIP(self, originalIP):
        self.add_param('originalIP', originalIP)

    def get_translationIP(self):
        return self.get_params().get('translationIP')

    def set_translationIP(self, translationIP):
        self.add_param('translationIP', translationIP)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
