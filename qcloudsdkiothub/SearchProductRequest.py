# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SearchProductRequest(Request):

    def __init__(self):
        super(SearchProductRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'SearchProduct', 'iothub.api.qcloud.com')

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)
