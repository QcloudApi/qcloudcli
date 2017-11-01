# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteDeviceRequest(Request):

    def __init__(self):
        super(DeleteDeviceRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'DeleteDevice', 'iiot.api.qcloud.com')

    def get_deviceName(self):
        return self.get_params().get('deviceName')

    def set_deviceName(self, deviceName):
        self.add_param('deviceName', deviceName)

    def get_expectedVersion(self):
        return self.get_params().get('expectedVersion')

    def set_expectedVersion(self, expectedVersion):
        self.add_param('expectedVersion', expectedVersion)
