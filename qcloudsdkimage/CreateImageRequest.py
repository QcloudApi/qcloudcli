# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateImageRequest(Request):

    def __init__(self):
        super(CreateImageRequest, self).__init__(
            'image', 'qcloudcliV1', 'CreateImage', 'image.api.qcloud.com')

    def get_autoPowerOffFlag(self):
        return self.get_params().get('autoPowerOffFlag')

    def set_autoPowerOffFlag(self, autoPowerOffFlag):
        self.add_param('autoPowerOffFlag', autoPowerOffFlag)

    def get_hardFlag(self):
        return self.get_params().get('hardFlag')

    def set_hardFlag(self, hardFlag):
        self.add_param('hardFlag', hardFlag)

    def get_imageDescription(self):
        return self.get_params().get('imageDescription')

    def set_imageDescription(self, imageDescription):
        self.add_param('imageDescription', imageDescription)

    def get_imageName(self):
        return self.get_params().get('imageName')

    def set_imageName(self, imageName):
        self.add_param('imageName', imageName)

    def get_instanceId(self):
        return self.get_params().get('instanceId')

    def set_instanceId(self, instanceId):
        self.add_param('instanceId', instanceId)

    def get_rebootFlag(self):
        return self.get_params().get('rebootFlag')

    def set_rebootFlag(self, rebootFlag):
        self.add_param('rebootFlag', rebootFlag)

    def get_sysprep(self):
        return self.get_params().get('sysprep')

    def set_sysprep(self, sysprep):
        self.add_param('sysprep', sysprep)
