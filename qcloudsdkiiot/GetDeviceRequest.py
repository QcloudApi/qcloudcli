# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetDeviceRequest(Request):

    def __init__(self):
        super(GetDeviceRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'GetDevice', 'iiot.api.qcloud.com')

    def get_deviceName(self):
        return self.get_params().get('deviceName')

    def set_deviceName(self, deviceName):
        self.add_param('deviceName', deviceName)
