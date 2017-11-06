# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SyncCvmImageRequest(Request):

    def __init__(self):
        super(SyncCvmImageRequest, self).__init__(
            'image', 'qcloudcliV1', 'SyncCvmImage', 'image.api.qcloud.com')

    def get_dstRegion(self):
        return self.get_params().get('dstRegion')

    def set_dstRegion(self, dstRegion):
        self.add_param('dstRegion', dstRegion)

    def get_imgIdList(self):
        return self.get_params().get('imgIdList')

    def set_imgIdList(self, imgIdList):
        self.add_param('imgIdList', imgIdList)

    def get_srcRegion(self):
        return self.get_params().get('srcRegion')

    def set_srcRegion(self, srcRegion):
        self.add_param('srcRegion', srcRegion)
