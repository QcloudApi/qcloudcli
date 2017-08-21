#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class OnlineHostRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdn', 'qcloudcliV1', 'OnlineHost', 'cdn.api.qcloud.com')

	def get_hostId(self):
		return self.get_params().get('hostId')

	def set_hostId(self, hostId):
		self.add_param('hostId', hostId)

	def get_host(self):
		return self.get_params().get('host')

	def set_host(self, host):
		self.add_param('host', host)

