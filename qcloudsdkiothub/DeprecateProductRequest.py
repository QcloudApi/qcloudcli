# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeprecateProductRequest(Request):

    def __init__(self):
        super(DeprecateProductRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'DeprecateProduct', 'iothub.api.qcloud.com')

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)

    def get_undoDeprecate(self):
        return self.get_params().get('undoDeprecate')

    def set_undoDeprecate(self, undoDeprecate):
        self.add_param('undoDeprecate', undoDeprecate)
