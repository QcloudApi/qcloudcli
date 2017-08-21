#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifyAlarmCallbackRequest(Request):

	def __init__(self):
		Request.__init__(self, 'monitor', 'qcloudcliV1', 'ModifyAlarmCallback', 'monitor.api.qcloud.com')

	def get_groupId(self):
		return self.get_params().get('groupId')

	def set_groupId(self, groupId):
		self.add_param('groupId', groupId)

	def get_url(self):
		return self.get_params().get('url')

	def set_url(self, url):
		self.add_param('url', url)

	def get_action(self):
		return self.get_params().get('action')

	def set_action(self, action):
		self.add_param('action', action)

