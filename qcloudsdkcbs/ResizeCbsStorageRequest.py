# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ResizeCbsStorageRequest(Request):

    def __init__(self):
        super(ResizeCbsStorageRequest, self).__init__(
            'cbs', 'qcloudcliV1', 'ResizeCbsStorage', 'cbs.api.qcloud.com')

    def get_storageId(self):
        return self.get_params().get('storageId')

    def set_storageId(self, storageId):
        self.add_param('storageId', storageId)

    def get_storageSize(self):
        return self.get_params().get('storageSize')

    def set_storageSize(self, storageSize):
        self.add_param('storageSize', storageSize)
