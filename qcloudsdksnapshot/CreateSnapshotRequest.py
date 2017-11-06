# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateSnapshotRequest(Request):

    def __init__(self):
        super(CreateSnapshotRequest, self).__init__(
            'snapshot', 'qcloudcliV1', 'CreateSnapshot', 'snapshot.api.qcloud.com')

    def get_snapshotName(self):
        return self.get_params().get('snapshotName')

    def set_snapshotName(self, snapshotName):
        self.add_param('snapshotName', snapshotName)

    def get_storageId(self):
        return self.get_params().get('storageId')

    def set_storageId(self, storageId):
        self.add_param('storageId', storageId)
