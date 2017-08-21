#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class MultipartUploadVodFileRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vod', 'qcloudcliV1', 'MultipartUploadVodFile', 'vod.api.qcloud.com')

	def get_fileName(self):
		return self.get_params().get('fileName')

	def set_fileName(self, fileName):
		self.add_param('fileName', fileName)

	def get_fileSha(self):
		return self.get_params().get('fileSha')

	def set_fileSha(self, fileSha):
		self.add_param('fileSha', fileSha)

	def get_fileSize(self):
		return self.get_params().get('fileSize')

	def set_fileSize(self, fileSize):
		self.add_param('fileSize', fileSize)

	def get_dataSize(self):
		return self.get_params().get('dataSize')

	def set_dataSize(self, dataSize):
		self.add_param('dataSize', dataSize)
		
	def get_offset(self):
		return self.get_params().get('offset')

	def set_offset(self, offset):
		self.add_param('offset', offset)
		
	def get_fileType(self):
		return self.get_params().get('fileType')

	def set_fileType(self, fileType):
		self.add_param('fileType', fileType)

	def get_tags(self):
		return self.get_params().get('tags')

	def set_tags(self, tags):
		self.add_param('tags', tags)

	def get_classId(self):
		return self.get_params().get('classId')

	def set_classId(self, classId):
		self.add_param('classId', classId)
		
	def get_isTranscode(self):
		return self.get_params().get('isTranscode')

	def set_isTranscode(self, isTranscode):
		self.add_param('isTranscode', isTranscode)
		
	def get_isScreenshot(self):
		return self.get_params().get('isScreenshot')

	def set_isScreenshot(self, isScreenshot):
		self.add_param('isScreenshot', isScreenshot)

	def get_isWatermark(self):
		return self.get_params().get('isWatermark')

	def set_isWatermark(self, isWatermark):
		self.add_param('isWatermark', isWatermark)
