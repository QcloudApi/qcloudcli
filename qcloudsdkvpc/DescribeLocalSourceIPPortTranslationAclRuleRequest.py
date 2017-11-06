# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLocalSourceIPPortTranslationAclRuleRequest(Request):

    def __init__(self):
        super(DescribeLocalSourceIPPortTranslationAclRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeLocalSourceIPPortTranslationAclRule', 'vpc.api.qcloud.com')

    def get_aclRuleIds(self):
        return self.get_params().get('aclRuleIds')

    def set_aclRuleIds(self, aclRuleIds):
        self.add_param('aclRuleIds', aclRuleIds)

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_translationIPPool(self):
        return self.get_params().get('translationIPPool')

    def set_translationIPPool(self, translationIPPool):
        self.add_param('translationIPPool', translationIPPool)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
