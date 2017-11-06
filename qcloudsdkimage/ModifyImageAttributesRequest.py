# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyImageAttributesRequest(Request):

    def __init__(self):
        super(ModifyImageAttributesRequest, self).__init__(
            'image', 'qcloudcliV1', 'ModifyImageAttributes', 'image.api.qcloud.com')

    def get_imageDescription(self):
        return self.get_params().get('imageDescription')

    def set_imageDescription(self, imageDescription):
        self.add_param('imageDescription', imageDescription)

    def get_imageId(self):
        return self.get_params().get('imageId')

    def set_imageId(self, imageId):
        self.add_param('imageId', imageId)

    def get_imageName(self):
        return self.get_params().get('imageName')

    def set_imageName(self, imageName):
        self.add_param('imageName', imageName)
