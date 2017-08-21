#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetCdnHostsDetailStatisticsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdn', 'qcloudcliV1', 'GetCdnHostsDetailStatistics', 'cdn.api.qcloud.com')

	def get_startTime(self):
		return self.get_params().get('startTime')

	def set_startTime(self, startTime):
		self.add_param('startTime', startTime)

	def get_endTime(self):
		return self.get_params().get('endTime')

	def set_endTime(self, endTime):
		self.add_param('endTime', endTime)

	def get_statType(self):
		return self.get_params().get('statType')

	def set_statType(self, statType):
		self.add_param('statType', statType)

	def get_hosts(self):
		return self.get_params().get('hosts')

	def set_hosts(self, hosts):
		self.add_param('hosts', hosts)

	def get_detail(self):
		return self.get_params().get('detail')

	def set_detail(self, detail):
		self.add_param('detail', detail)

