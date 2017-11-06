# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListPoliciesRequest(Request):

    def __init__(self):
        super(ListPoliciesRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'ListPolicies', 'iothub.api.qcloud.com')

    def get_isAscendingOrder(self):
        return self.get_params().get('isAscendingOrder')

    def set_isAscendingOrder(self, isAscendingOrder):
        self.add_param('isAscendingOrder', isAscendingOrder)

    def get_marker(self):
        return self.get_params().get('marker')

    def set_marker(self, marker):
        self.add_param('marker', marker)

    def get_pageSize(self):
        return self.get_params().get('pageSize')

    def set_pageSize(self, pageSize):
        self.add_param('pageSize', pageSize)
