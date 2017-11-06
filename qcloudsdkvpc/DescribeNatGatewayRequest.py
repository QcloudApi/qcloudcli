# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeNatGatewayRequest(Request):

    def __init__(self):
        super(DescribeNatGatewayRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeNatGateway', 'vpc.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_natId(self):
        return self.get_params().get('natId')

    def set_natId(self, natId):
        self.add_param('natId', natId)

    def get_natName(self):
        return self.get_params().get('natName')

    def set_natName(self, natName):
        self.add_param('natName', natName)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)

    def get_vpcName(self):
        return self.get_params().get('vpcName')

    def set_vpcName(self, vpcName):
        self.add_param('vpcName', vpcName)
