# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyLocalDestinationIPPortTranslationNatRuleRequest(Request):

    def __init__(self):
        super(ModifyLocalDestinationIPPortTranslationNatRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyLocalDestinationIPPortTranslationNatRule', 'vpc.api.qcloud.com')

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

    def get_oldOriginalPort(self):
        return self.get_params().get('oldOriginalPort')

    def set_oldOriginalPort(self, oldOriginalPort):
        self.add_param('oldOriginalPort', oldOriginalPort)

    def get_oldProto(self):
        return self.get_params().get('oldProto')

    def set_oldProto(self, oldProto):
        self.add_param('oldProto', oldProto)

    def get_oldTranslationIP(self):
        return self.get_params().get('oldTranslationIP')

    def set_oldTranslationIP(self, oldTranslationIP):
        self.add_param('oldTranslationIP', oldTranslationIP)

    def get_oldTranslationPort(self):
        return self.get_params().get('oldTranslationPort')

    def set_oldTranslationPort(self, oldTranslationPort):
        self.add_param('oldTranslationPort', oldTranslationPort)

    def get_originalIP(self):
        return self.get_params().get('originalIP')

    def set_originalIP(self, originalIP):
        self.add_param('originalIP', originalIP)

    def get_originalPort(self):
        return self.get_params().get('originalPort')

    def set_originalPort(self, originalPort):
        self.add_param('originalPort', originalPort)

    def get_proto(self):
        return self.get_params().get('proto')

    def set_proto(self, proto):
        self.add_param('proto', proto)

    def get_translationIP(self):
        return self.get_params().get('translationIP')

    def set_translationIP(self, translationIP):
        self.add_param('translationIP', translationIP)

    def get_translationPort(self):
        return self.get_params().get('translationPort')

    def set_translationPort(self, translationPort):
        self.add_param('translationPort', translationPort)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
