#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class StartLVBInsertContextNewRequest(Request):

	def __init__(self):
		Request.__init__(self, 'live', 'qcloudcliV1', 'StartLVBInsertContextNew', 'live.api.qcloud.com')

	def get_channelId(self):
		return self.get_params().get('channelId')

	def set_channelId(self, channelId):
		self.add_param('channelId', channelId)

	def get_insertType(self):
		return self.get_params().get('insertType')

	def set_insertType(self, insertType):
		self.add_param('insertType', insertType)

	def get_insertContent(self):
		return self.get_params().get('insertContent')

	def set_insertContent(self, insertContent):
		self.add_param('insertContent', insertContent)

	def get_locationX(self):
		return self.get_params().get('locationX')

	def set_locationX(self, locationX):
		self.add_param('locationX', locationX)

	def get_locationY(self):
		return self.get_params().get('locationY')

	def set_locationY(self, locationY):
		self.add_param('locationY', locationY)

	def get_width(self):
		return self.get_params().get('width')

	def set_width(self, width):
		self.add_param('width', width)

	def get_height(self):
		return self.get_params().get('height')

	def set_height(self, height):
		self.add_param('height', height)

