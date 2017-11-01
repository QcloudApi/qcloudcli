# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetDeviceShadowRequest(Request):

    def __init__(self):
        super(GetDeviceShadowRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'GetDeviceShadow', 'iiot.api.qcloud.com')

    def get_deviceName(self):
        return self.get_params().get('deviceName')

    def set_deviceName(self, deviceName):
        self.add_param('deviceName', deviceName)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)
