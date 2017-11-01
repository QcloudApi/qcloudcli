# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeProductRequest(Request):

    def __init__(self):
        super(DescribeProductRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'DescribeProduct', 'iothub.api.qcloud.com')

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)
