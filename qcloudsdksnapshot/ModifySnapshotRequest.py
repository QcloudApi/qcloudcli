# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifySnapshotRequest(Request):

    def __init__(self):
        super(ModifySnapshotRequest, self).__init__(
            'snapshot', 'qcloudcliV1', 'ModifySnapshot', 'snapshot.api.qcloud.com')

    def get_isPermanent(self):
        return self.get_params().get('isPermanent')

    def set_isPermanent(self, isPermanent):
        self.add_param('isPermanent', isPermanent)

    def get_snapshotId(self):
        return self.get_params().get('snapshotId')

    def set_snapshotId(self, snapshotId):
        self.add_param('snapshotId', snapshotId)

    def get_snapshotName(self):
        return self.get_params().get('snapshotName')

    def set_snapshotName(self, snapshotName):
        self.add_param('snapshotName', snapshotName)
