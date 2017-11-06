# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyImageAttributeRequest(Request):

    def __init__(self):
        super(ModifyImageAttributeRequest, self).__init__(
            'image', 'qcloudcliV1', 'ModifyImageAttribute', 'image.api.qcloud.com')

    def get_ImageDescription(self):
        return self.get_params().get('ImageDescription')

    def set_ImageDescription(self, ImageDescription):
        self.add_param('ImageDescription', ImageDescription)

    def get_ImageId(self):
        return self.get_params().get('ImageId')

    def set_ImageId(self, ImageId):
        self.add_param('ImageId', ImageId)

    def get_ImageName(self):
        return self.get_params().get('ImageName')

    def set_ImageName(self, ImageName):
        self.add_param('ImageName', ImageName)
