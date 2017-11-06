# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateDeviceRequest(Request):

    def __init__(self):
        super(CreateDeviceRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'CreateDevice', 'iothub.api.qcloud.com')

    def get_attributePayload(self):
        return self.get_params().get('attributePayload')

    def set_attributePayload(self, attributePayload):
        self.add_param('attributePayload', attributePayload)

    def get_deviceName(self):
        return self.get_params().get('deviceName')

    def set_deviceName(self, deviceName):
        self.add_param('deviceName', deviceName)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)
