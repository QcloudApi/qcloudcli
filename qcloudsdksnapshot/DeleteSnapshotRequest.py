#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteSnapshotRequest(Request):

	def __init__(self):
		Request.__init__(self, 'snapshot', 'qcloudcliV1', 'DeleteSnapshot', 'snapshot.api.qcloud.com')

	def get_snapshotIds(self):
		return self.get_params().get('snapshotIds')

	def set_snapshotIds(self, snapshotIds):
		self.add_param('snapshotIds', snapshotIds)

