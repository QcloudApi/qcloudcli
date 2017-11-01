# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CancelShareImageRequest(Request):

    def __init__(self):
        super(CancelShareImageRequest, self).__init__(
            'image', 'qcloudcliV1', 'CancelShareImage', 'image.api.qcloud.com')

    def get_imageId(self):
        return self.get_params().get('imageId')

    def set_imageId(self, imageId):
        self.add_param('imageId', imageId)

    def get_uinList(self):
        return self.get_params().get('uinList')

    def set_uinList(self, uinList):
        self.add_param('uinList', uinList)
