# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeVpcClassicLinkRequest(Request):

    def __init__(self):
        super(DescribeVpcClassicLinkRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeVpcClassicLink', 'vpc.api.qcloud.com')

    def get_classicLinkId(self):
        return self.get_params().get('classicLinkId')

    def set_classicLinkId(self, classicLinkId):
        self.add_param('classicLinkId', classicLinkId)

    def get_lanIp(self):
        return self.get_params().get('lanIp')

    def set_lanIp(self, lanIp):
        self.add_param('lanIp', lanIp)

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
