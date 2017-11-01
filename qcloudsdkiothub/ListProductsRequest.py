# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListProductsRequest(Request):

    def __init__(self):
        super(ListProductsRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'ListProducts', 'iothub.api.qcloud.com')

    def get_pageNum(self):
        return self.get_params().get('pageNum')

    def set_pageNum(self, pageNum):
        self.add_param('pageNum', pageNum)

    def get_pageSize(self):
        return self.get_params().get('pageSize')

    def set_pageSize(self, pageSize):
        self.add_param('pageSize', pageSize)
