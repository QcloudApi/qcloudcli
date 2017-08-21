#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeCdnHostInfoRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdn', 'qcloudcliV1', 'DescribeCdnHostInfo', 'cdn.api.qcloud.com')

	def get_startDate(self):
		return self.get_params().get('startDate')

	def set_startDate(self, startDate):
		self.add_param('startDate', startDate)

	def get_endDate(self):
		return self.get_params().get('endDate')

	def set_endDate(self, endDate):
		self.add_param('endDate', endDate)

	def get_statType(self):
		return self.get_params().get('statType')

	def set_statType(self, statType):
		self.add_param('statType', statType)

	def get_projects(self):
		return self.get_params().get('projects')

	def set_projects(self, projects):
		self.add_param('projects', projects)

	def get_hosts(self):
		return self.get_params().get('hosts')

	def set_hosts(self, hosts):
		self.add_param('hosts', hosts)

