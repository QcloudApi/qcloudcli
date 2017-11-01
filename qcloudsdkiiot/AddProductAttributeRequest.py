# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AddProductAttributeRequest(Request):

    def __init__(self):
        super(AddProductAttributeRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'AddProductAttribute', 'iiot.api.qcloud.com')

    def get_attribute(self):
        return self.get_params().get('attribute')

    def set_attribute(self, attribute):
        self.add_param('attribute', attribute)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)
