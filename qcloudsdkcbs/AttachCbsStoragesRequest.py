# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AttachCbsStoragesRequest(Request):

    def __init__(self):
        super(AttachCbsStoragesRequest, self).__init__(
            'cbs', 'qcloudcliV1', 'AttachCbsStorages', 'cbs.api.qcloud.com')

    def get_storageIds(self):
        return self.get_params().get('storageIds')

    def set_storageIds(self, storageIds):
        self.add_param('storageIds', storageIds)

    def get_uInstanceId(self):
        return self.get_params().get('uInstanceId')

    def set_uInstanceId(self, uInstanceId):
        self.add_param('uInstanceId', uInstanceId)
