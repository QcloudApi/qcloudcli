# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateProductPolicyRequest(Request):

    def __init__(self):
        super(UpdateProductPolicyRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'UpdateProductPolicy', 'iothub.api.qcloud.com')

    def get_defaultPolicyName(self):
        return self.get_params().get('defaultPolicyName')

    def set_defaultPolicyName(self, defaultPolicyName):
        self.add_param('defaultPolicyName', defaultPolicyName)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)
