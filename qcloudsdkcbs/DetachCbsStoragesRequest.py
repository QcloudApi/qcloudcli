# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DetachCbsStoragesRequest(Request):

    def __init__(self):
        super(DetachCbsStoragesRequest, self).__init__(
            'cbs', 'qcloudcliV1', 'DetachCbsStorages', 'cbs.api.qcloud.com')

    def get_storageIds(self):
        return self.get_params().get('storageIds')

    def set_storageIds(self, storageIds):
        self.add_param('storageIds', storageIds)
