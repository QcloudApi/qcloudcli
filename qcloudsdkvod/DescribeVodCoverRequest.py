#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeVodCoverRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vod', 'qcloudcliV1', 'DescribeVodCover', 'vod.api.qcloud.com')

	def get_fileId(self):
		return self.get_params().get('fileId')

	def set_fileId(self, fileId):
		self.add_param('fileId', fileId)

	def get_type(self):
		return self.get_params().get('type')

	def set_type(self, type):
		self.add_param('type', type)

	def get_para(self):
		return self.get_params().get('para')

	def set_para(self, para):
		self.add_param('para', para)

	def get_imageData(self):
		return self.get_params().get('imageData')

	def set_imageData(self, imageData):
		self.add_param('imageData', imageData)

