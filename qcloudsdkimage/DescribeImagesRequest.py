#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeImagesRequest(Request):

	def __init__(self):
		Request.__init__(self, 'image', 'qcloudcliV1', 'DescribeImages', 'image.api.qcloud.com')

	def get_imageIds(self):
		return self.get_params().get('imageIds')

	def set_imageIds(self, imageIds):
		self.add_param('imageIds', imageIds)
		
	def get_imageType(self):
		return self.get_params().get('imageType')

	def set_imageType(self, imageType):
		self.add_param('imageType', imageType)

	def get_status(self):
		return self.get_params().get('status')

	def set_status(self, status):
		self.add_param('status', status)
	
	def get_offset(self):
		return self.get_params().get('offset')

	def set_offset(self, offset):
		self.add_param('offset', offset)
		
	def get_limit(self):
		return self.get_params().get('limit')

	def set_limit(self, limit):
		self.add_param('limit', limit)

