# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyProductAttributeRequest(Request):

    def __init__(self):
        super(ModifyProductAttributeRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'ModifyProductAttribute', 'iothub.api.qcloud.com')

    def get_attribute(self):
        return self.get_params().get('attribute')

    def set_attribute(self, attribute):
        self.add_param('attribute', attribute)

    def get_attributeTo(self):
        return self.get_params().get('attributeTo')

    def set_attributeTo(self, attributeTo):
        self.add_param('attributeTo', attributeTo)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)
