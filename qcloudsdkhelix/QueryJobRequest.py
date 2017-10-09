#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class QueryJobRequest(Request):

	def __init__(self):
		Request.__init__(self, 'helix', 'qcloudcliV1', 'QueryJob', 'helix.api.qcloud.com')

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)

	def get_jobId(self):
		return self.get_params().get('jobId')

	def set_jobId(self, jobId):
		self.add_param('jobId', jobId)

