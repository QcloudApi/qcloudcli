# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyCbsStorageAttributesRequest(Request):

    def __init__(self):
        super(ModifyCbsStorageAttributesRequest, self).__init__(
            'cbs', 'qcloudcliV1', 'ModifyCbsStorageAttributes', 'cbs.api.qcloud.com')

    def get_portable(self):
        return self.get_params().get('portable')

    def set_portable(self, portable):
        self.add_param('portable', portable)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_storageId(self):
        return self.get_params().get('storageId')

    def set_storageId(self, storageId):
        self.add_param('storageId', storageId)

    def get_storageIds(self):
        return self.get_params().get('storageIds')

    def set_storageIds(self, storageIds):
        self.add_param('storageIds', storageIds)

    def get_storageName(self):
        return self.get_params().get('storageName')

    def set_storageName(self, storageName):
        self.add_param('storageName', storageName)
