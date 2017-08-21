#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class AssumeRoleRequest(Request):

	def __init__(self):
		Request.__init__(self, 'sts', 'qcloudcliV1', 'AssumeRole', 'sts.api.qcloud.com')

