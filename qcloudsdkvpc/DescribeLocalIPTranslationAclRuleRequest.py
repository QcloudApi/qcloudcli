# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLocalIPTranslationAclRuleRequest(Request):

    def __init__(self):
        super(DescribeLocalIPTranslationAclRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeLocalIPTranslationAclRule', 'vpc.api.qcloud.com')

    def get_aclRuleIds(self):
        return self.get_params().get('aclRuleIds')

    def set_aclRuleIds(self, aclRuleIds):
        self.add_param('aclRuleIds', aclRuleIds)

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

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
