# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateDeviceShadowRequest(Request):

    def __init__(self):
        super(UpdateDeviceShadowRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'UpdateDeviceShadow', 'iothub.api.qcloud.com')

    def get_deviceName(self):
        return self.get_params().get('deviceName')

    def set_deviceName(self, deviceName):
        self.add_param('deviceName', deviceName)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)

    def get_state(self):
        return self.get_params().get('state')

    def set_state(self, state):
        self.add_param('state', state)

    def get_version(self):
        return self.get_params().get('version')

    def set_version(self, version):
        self.add_param('version', version)
