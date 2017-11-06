# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateDeviceRequest(Request):

    def __init__(self):
        super(UpdateDeviceRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'UpdateDevice', 'iiot.api.qcloud.com')

    def get_attributePayload(self):
        return self.get_params().get('attributePayload')

    def set_attributePayload(self, attributePayload):
        self.add_param('attributePayload', attributePayload)

    def get_deviceName(self):
        return self.get_params().get('deviceName')

    def set_deviceName(self, deviceName):
        self.add_param('deviceName', deviceName)

    def get_expectedVersion(self):
        return self.get_params().get('expectedVersion')

    def set_expectedVersion(self, expectedVersion):
        self.add_param('expectedVersion', expectedVersion)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)

    def get_removeProduct(self):
        return self.get_params().get('removeProduct')

    def set_removeProduct(self, removeProduct):
        self.add_param('removeProduct', removeProduct)
