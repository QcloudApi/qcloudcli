# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ApplySnapshotRequest(Request):

    def __init__(self):
        super(ApplySnapshotRequest, self).__init__(
            'snapshot', 'qcloudcliV1', 'ApplySnapshot', 'snapshot.api.qcloud.com')

    def get_snapshotId(self):
        return self.get_params().get('snapshotId')

    def set_snapshotId(self, snapshotId):
        self.add_param('snapshotId', snapshotId)

    def get_storageId(self):
        return self.get_params().get('storageId')

    def set_storageId(self, storageId):
        self.add_param('storageId', storageId)
