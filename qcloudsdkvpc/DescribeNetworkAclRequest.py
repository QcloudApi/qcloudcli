# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeNetworkAclRequest(Request):

    def __init__(self):
        super(DescribeNetworkAclRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeNetworkAcl', 'vpc.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_networkAclId(self):
        return self.get_params().get('networkAclId')

    def set_networkAclId(self, networkAclId):
        self.add_param('networkAclId', networkAclId)

    def get_networkAclName(self):
        return self.get_params().get('networkAclName')

    def set_networkAclName(self, networkAclName):
        self.add_param('networkAclName', networkAclName)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_orderDirection(self):
        return self.get_params().get('orderDirection')

    def set_orderDirection(self, orderDirection):
        self.add_param('orderDirection', orderDirection)

    def get_orderField(self):
        return self.get_params().get('orderField')

    def set_orderField(self, orderField):
        self.add_param('orderField', orderField)

    def get_ruleDirection(self):
        return self.get_params().get('ruleDirection')

    def set_ruleDirection(self, ruleDirection):
        self.add_param('ruleDirection', ruleDirection)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
