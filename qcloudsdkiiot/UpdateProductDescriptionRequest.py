# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateProductDescriptionRequest(Request):

    def __init__(self):
        super(UpdateProductDescriptionRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'UpdateProductDescription', 'iiot.api.qcloud.com')

    def get_description(self):
        return self.get_params().get('description')

    def set_description(self, description):
        self.add_param('description', description)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)
