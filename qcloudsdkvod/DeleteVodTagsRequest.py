#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteVodTagsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vod', 'qcloudcliV1', 'DeleteVodTags', 'vod.api.qcloud.com')

	def get_fileId(self):
		return self.get_params().get('fileId')

	def set_fileId(self, fileId):
		self.add_param('fileId', fileId)

	def get_tags(self):
		return self.get_params().get('tags')

	def set_tags(self, tags):
		self.add_param('tags', tags)

