#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class UpdateCertificateRequest(Request):

	def __init__(self):
		Request.__init__(self, 'iiot', 'qcloudcliV1', 'UpdateCertificate', 'iiot.api.qcloud.com')

	def get_newStatus(self):
		return self.get_params().get('newStatus')

	def set_newStatus(self, newStatus):
		self.add_param('newStatus', newStatus)

	def get_certificateId(self):
		return self.get_params().get('certificateId')

	def set_certificateId(self, certificateId):
		self.add_param('certificateId', certificateId)

