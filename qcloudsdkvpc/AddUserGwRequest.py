#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class AddUserGwRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vpc', 'qcloudcliV1', 'AddUserGw', 'vpc.api.qcloud.com')

	def get_userGwName(self):
		return self.get_params().get('userGwName')

	def set_userGwName(self, userGwName):
		self.add_param('userGwName', userGwName)

	def get_userGwAddr(self):
		return self.get_params().get('userGwAddr')

	def set_userGwAddr(self, userGwAddr):
		self.add_param('userGwAddr', userGwAddr)

