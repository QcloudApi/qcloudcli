# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeInstancesOfSecurityGroupRequest(Request):

    def __init__(self):
        super(DescribeInstancesOfSecurityGroupRequest, self).__init__(
            'dfw', 'qcloudcliV1', 'DescribeInstancesOfSecurityGroup', 'dfw.api.qcloud.com')

    def get_alias(self):
        return self.get_params().get('alias')

    def set_alias(self, alias):
        self.add_param('alias', alias)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_sgId(self):
        return self.get_params().get('sgId')

    def set_sgId(self, sgId):
        self.add_param('sgId', sgId)

    def get_vagueIp(self):
        return self.get_params().get('vagueIp')

    def set_vagueIp(self, vagueIp):
        self.add_param('vagueIp', vagueIp)
