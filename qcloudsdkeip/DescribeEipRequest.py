# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeEipRequest(Request):

    def __init__(self):
        super(DescribeEipRequest, self).__init__(
            'eip', 'qcloudcliV1', 'DescribeEip', 'eip.api.qcloud.com')

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

    def get_mode(self):
        return self.get_params().get('mode')

    def set_mode(self, mode):
        self.add_param('mode', mode)

    def get_networkInterfaceIds(self):
        return self.get_params().get('networkInterfaceIds')

    def set_networkInterfaceIds(self, networkInterfaceIds):
        self.add_param('networkInterfaceIds', networkInterfaceIds)

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

    def get_privateIpAddress(self):
        return self.get_params().get('privateIpAddress')

    def set_privateIpAddress(self, privateIpAddress):
        self.add_param('privateIpAddress', privateIpAddress)

    def get_searchKey(self):
        return self.get_params().get('searchKey')

    def set_searchKey(self, searchKey):
        self.add_param('searchKey', searchKey)

    def get_status(self):
        return self.get_params().get('status')

    def set_status(self, status):
        self.add_param('status', status)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)

    def get_unInstanceIds(self):
        return self.get_params().get('unInstanceIds')

    def set_unInstanceIds(self, unInstanceIds):
        self.add_param('unInstanceIds', unInstanceIds)
