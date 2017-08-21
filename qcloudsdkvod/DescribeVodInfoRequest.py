#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeVodInfoRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vod', 'qcloudcliV1', 'DescribeVodInfo', 'vod.api.qcloud.com')

	def get_fileIds(self):
		return self.get_params().get('fileIds')

	def set_fileIds(self, fileIds):
		self.add_param('fileIds', fileIds)

	def get_param_from(self):
		return self.get_params().get('param_from')

	def set_param_from(self, param_from):
		self.add_param('param_from', param_from)

	def get_to(self):
		return self.get_params().get('to')

	def set_to(self, to):
		self.add_param('to', to)

	def get_status(self):
		return self.get_params().get('status')

	def set_status(self, status):
		self.add_param('status', status)

	def get_orderby(self):
		return self.get_params().get('orderby')

	def set_orderby(self, orderby):
		self.add_param('orderby', orderby)

	def get_pageNo(self):
		return self.get_params().get('pageNo')

	def set_pageNo(self, pageNo):
		self.add_param('pageNo', pageNo)

	def get_pageSize(self):
		return self.get_params().get('pageSize')

	def set_pageSize(self, pageSize):
		self.add_param('pageSize', pageSize)

	def get_classId(self):
		return self.get_params().get('classId')

	def set_classId(self, classId):
		self.add_param('classId', classId)

	def get_orderkey(self):
		return self.get_params().get('orderkey')

	def set_orderkey(self, orderkey):
		self.add_param('orderkey', orderkey)

