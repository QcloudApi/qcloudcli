#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeAppFlowRequest(Request):

	def __init__(self):
		Request.__init__(self, 'monitor', 'qcloudcliV1', 'DescribeAppFlow', 'monitor.api.qcloud.com')

	def get_startTime(self):
		return self.get_params().get('startTime')

	def set_startTime(self, startTime):
		self.add_param('startTime', startTime)

	def get_endTime(self):
		return self.get_params().get('endTime')

	def set_endTime(self, endTime):
		self.add_param('endTime', endTime)

