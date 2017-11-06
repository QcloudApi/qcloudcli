# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateImageRequest(Request):

    def __init__(self):
        super(CreateImageRequest, self).__init__(
            'image', 'qcloudcliV1', 'CreateImage', 'image.api.qcloud.com')

    def get_ForcePoweroff(self):
        return self.get_params().get('ForcePoweroff')

    def set_ForcePoweroff(self, ForcePoweroff):
        self.add_param('ForcePoweroff', ForcePoweroff)

    def get_ImageDescription(self):
        return self.get_params().get('ImageDescription')

    def set_ImageDescription(self, ImageDescription):
        self.add_param('ImageDescription', ImageDescription)

    def get_ImageName(self):
        return self.get_params().get('ImageName')

    def set_ImageName(self, ImageName):
        self.add_param('ImageName', ImageName)

    def get_InstanceId(self):
        return self.get_params().get('InstanceId')

    def set_InstanceId(self, InstanceId):
        self.add_param('InstanceId', InstanceId)

    def get_Reboot(self):
        return self.get_params().get('Reboot')

    def set_Reboot(self, Reboot):
        self.add_param('Reboot', Reboot)

    def get_Sysprep(self):
        return self.get_params().get('Sysprep')

    def set_Sysprep(self, Sysprep):
        self.add_param('Sysprep', Sysprep)
