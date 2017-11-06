# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeUsagePlansStatusRequest(Request):

    def __init__(self):
        super(DescribeUsagePlansStatusRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'DescribeUsagePlansStatus', 'apigateway.api.qcloud.com')

    def get_filter(self):
        return self.get_params().get('filter')

    def set_filter(self, filter):
        self.add_param('filter', filter)

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

    def get_searchId(self):
        return self.get_params().get('searchId')

    def set_searchId(self, searchId):
        self.add_param('searchId', searchId)

    def get_searchName(self):
        return self.get_params().get('searchName')

    def set_searchName(self, searchName):
        self.add_param('searchName', searchName)

    def get_usagePlanIds(self):
        return self.get_params().get('usagePlanIds')

    def set_usagePlanIds(self, usagePlanIds):
        self.add_param('usagePlanIds', usagePlanIds)
