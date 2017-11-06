# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeEipBmRequest(Request):

    def __init__(self):
        super(DescribeEipBmRequest, self).__init__(
            'eip', 'qcloudcliV1', 'DescribeEipBm', 'eip.api.qcloud.com')

    def get_eipIds(self):
        return self.get_params().get('eipIds')

    def set_eipIds(self, eipIds):
        self.add_param('eipIds', eipIds)

    def get_eips(self):
        return self.get_params().get('eips')

    def set_eips(self, eips):
        self.add_param('eips', eips)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_orderBy(self):
        return self.get_params().get('orderBy')

    def set_orderBy(self, orderBy):
        self.add_param('orderBy', orderBy)

    def get_orderType(self):
        return self.get_params().get('orderType')

    def set_orderType(self, orderType):
        self.add_param('orderType', orderType)

    def get_payMode(self):
        return self.get_params().get('payMode')

    def set_payMode(self, payMode):
        self.add_param('payMode', payMode)

    def get_searchKey(self):
        return self.get_params().get('searchKey')

    def set_searchKey(self, searchKey):
        self.add_param('searchKey', searchKey)

    def get_status(self):
        return self.get_params().get('status')

    def set_status(self, status):
        self.add_param('status', status)

    def get_unInstanceIds(self):
        return self.get_params().get('unInstanceIds')

    def set_unInstanceIds(self, unInstanceIds):
        self.add_param('unInstanceIds', unInstanceIds)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
