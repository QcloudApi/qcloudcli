# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateMultiDeviceRequest(Request):

    def __init__(self):
        super(CreateMultiDeviceRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'CreateMultiDevice', 'iothub.api.qcloud.com')

    def get_listDeviceName(self):
        return self.get_params().get('listDeviceName')

    def set_listDeviceName(self, listDeviceName):
        self.add_param('listDeviceName', listDeviceName)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)
