#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class AssumeRoleWithWebIdentityRequest(Request):

	def __init__(self):
		Request.__init__(self, 'sts', 'qcloudcliV1', 'AssumeRoleWithWebIdentity', 'sts.api.qcloud.com')

