#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetAccountSettingsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'scf', 'qcloudcliV1', 'GetAccountSettings', 'scf.api.qcloud.com')

