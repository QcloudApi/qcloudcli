# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetEventPolicyConfigRequest(Request):

    def __init__(self):
        super(GetEventPolicyConfigRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'GetEventPolicyConfig', 'monitor.api.qcloud.com')

    def get_products(self):
        return self.get_params().get('products')

    def set_products(self, products):
        self.add_param('products', products)

    def get_viewName(self):
        return self.get_params().get('viewName')

    def set_viewName(self, viewName):
        self.add_param('viewName', viewName)
