# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteSnapshotRequest(Request):

    def __init__(self):
        super(DeleteSnapshotRequest, self).__init__(
            'snapshot', 'qcloudcliV1', 'DeleteSnapshot', 'snapshot.api.qcloud.com')

    def get_snapshotIds(self):
        return self.get_params().get('snapshotIds')

    def set_snapshotIds(self, snapshotIds):
        self.add_param('snapshotIds', snapshotIds)
