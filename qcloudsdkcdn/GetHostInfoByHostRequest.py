#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetHostInfoByHostRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdn', 'qcloudcliV1', 'GetHostInfoByHost', 'cdn.api.qcloud.com')

	def get_hosts(self):
		return self.get_params().get('hosts')

	def set_hosts(self, hosts):
		self.add_param('hosts', hosts)

