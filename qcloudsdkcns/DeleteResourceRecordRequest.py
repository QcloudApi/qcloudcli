#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteResourceRecordRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cns', 'qcloudcliV1', 'DeleteResourceRecord', 'cns.api.qcloud.com')

	def get_domain(self):
		return self.get_params().get('domain')

	def set_domain(self, domain):
		self.add_param('domain', domain)
		
	def get_subDomain(self):
		return self.get_params().get('subDomain')

	def set_subDomain(self, subDomain):
		self.add_param('subDomain', subDomain)

	def get_recordId(self):
		return self.get_params().get('recordId')

	def set_recordId(self, recordId):
		self.add_param('recordId', recordId)

	def get_resourceType(self):
		return self.get_params().get('resourceType')

	def set_resourceType(self, resourceType):
		self.add_param('resourceType', resourceType)

	def get_attachId(self):
		return self.get_params().get('attachId')

	def set_attachId(self, attachId):
		self.add_param('attachId', attachId)

	
