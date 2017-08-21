#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeResourceRecordDetailRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cns', 'qcloudcliV1', 'DescribeResourceRecordDetail', 'cns.api.qcloud.com')

	def get_attachId(self):
		return self.get_params().get('attachId')

	def set_attachId(self, attachId):
		self.add_param('attachId', attachId)	