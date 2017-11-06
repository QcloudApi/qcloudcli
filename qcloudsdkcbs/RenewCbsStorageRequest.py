# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class RenewCbsStorageRequest(Request):

    def __init__(self):
        super(RenewCbsStorageRequest, self).__init__(
            'cbs', 'qcloudcliV1', 'RenewCbsStorage', 'cbs.api.qcloud.com')

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)

    def get_storageId(self):
        return self.get_params().get('storageId')

    def set_storageId(self, storageId):
        self.add_param('storageId', storageId)
