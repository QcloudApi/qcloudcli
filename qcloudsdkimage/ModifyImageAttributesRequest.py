#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifyImageAttributesRequest(Request):

	def __init__(self):
		Request.__init__(self, 'image', 'qcloudcliV1', 'ModifyImageAttributes', 'image.api.qcloud.com')

	def get_imageId(self):
		return self.get_params().get('imageId')

	def set_imageId(self, imageId):
		self.add_param('imageId', imageId)

	def get_imageName(self):
		return self.get_params().get('imageName')

	def set_imageName(self, imageName):
		self.add_param('imageName', imageName)

	def get_imageDescription(self):
		return self.get_params().get('imageDescription')

	def set_imageDescription(self, imageDescription):
		self.add_param('imageDescription', imageDescription)

