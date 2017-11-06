# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeUserGwRequest(Request):

    def __init__(self):
        super(DescribeUserGwRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeUserGw', 'vpc.api.qcloud.com')

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

    def get_userGwId(self):
        return self.get_params().get('userGwId')

    def set_userGwId(self, userGwId):
        self.add_param('userGwId', userGwId)

    def get_userGwName(self):
        return self.get_params().get('userGwName')

    def set_userGwName(self, userGwName):
        self.add_param('userGwName', userGwName)
