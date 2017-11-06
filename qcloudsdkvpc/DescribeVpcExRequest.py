# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeVpcExRequest(Request):

    def __init__(self):
        super(DescribeVpcExRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeVpcEx', 'vpc.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

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

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)

    def get_vpcName(self):
        return self.get_params().get('vpcName')

    def set_vpcName(self, vpcName):
        self.add_param('vpcName', vpcName)
