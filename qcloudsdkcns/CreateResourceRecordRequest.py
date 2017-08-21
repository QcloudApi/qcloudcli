#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CreateResourceRecordRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cns', 'qcloudcliV1', 'CreateResourceRecord', 'cns.api.qcloud.com')

	def get_domain(self):
		return self.get_params().get('domain')

	def set_domain(self, domain):
		self.add_param('domain', domain)
		
	def get_type(self):
		return self.get_params().get('type')

	def set_type(self, type):
		self.add_param('type', type)
	
	def get_subDomain(self):
		return self.get_params().get('subDomain')

	def set_subDomain(self, subDomain):
		self.add_param('subDomain', subDomain)
	
	def get_recordType(self):
		return self.get_params().get('recordType')

	def set_recordType(self, recordType):
		self.add_param('recordType', recordType)

	def get_recordLine(self):
		return self.get_params().get('recordLine')

	def set_recordLine(self, recordLine):
		self.add_param('recordLine', recordLine)

	def get_recordValue(self):
		return self.get_params().get('recordValue')

	def set_recordValue(self, recordValue):
		self.add_param('recordValue', recordValue)
		
	def get_ttl(self):
		return self.get_params().get('ttl')

	def set_ttl(self, ttl):
		self.add_param('ttl', ttl)
		
	def get_mxLevel(self):
		return self.get_params().get('mxLevel')

	def set_mxLevel(self, mxLevel):
		self.add_param('mxLevel', mxLevel)

	def get_instanceIds(self):
		return self.get_params().get('instanceIds')

	def set_instanceIds(self, instanceIds):
		self.add_param('instanceIds', instanceIds)
		



