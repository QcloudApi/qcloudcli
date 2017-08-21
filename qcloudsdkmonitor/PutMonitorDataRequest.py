#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class PutMonitorDataRequest(Request):

	def __init__(self):
		Request.__init__(self, 'monitor', 'qcloudcliV1', 'PutMonitorData', 'receiver.monitor.tencentyun.com:8080')

	def get_Namespace(self):
		return self.get_params().get('Namespace')

	def set_Namespace(self, Namespace):
		self.add_param('Namespace', Namespace)

	def get_Data(self):
		return self.get_params().get('Data')

	def set_Data(self, Data):
		self.add_param('Data', Data)

