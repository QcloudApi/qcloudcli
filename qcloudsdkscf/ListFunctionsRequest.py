# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListFunctionsRequest(Request):

    def __init__(self):
        super(ListFunctionsRequest, self).__init__(
            'scf', 'qcloudcliV1', 'ListFunctions', 'scf.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_order(self):
        return self.get_params().get('order')

    def set_order(self, order):
        self.add_param('order', order)

    def get_orderby(self):
        return self.get_params().get('orderby')

    def set_orderby(self, orderby):
        self.add_param('orderby', orderby)

    def get_searchKey(self):
        return self.get_params().get('searchKey')

    def set_searchKey(self, searchKey):
        self.add_param('searchKey', searchKey)
