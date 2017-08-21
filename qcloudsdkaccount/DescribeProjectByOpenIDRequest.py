#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeProjectByOpenIDRequest(Request):

	def __init__(self):
		Request.__init__(self, 'account', 'qcloudcliV1', 'DescribeProjectByOpenID', 'account.api.qcloud.com')

