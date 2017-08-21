#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeEipBmQuotaRequest(Request):

	def __init__(self):
		Request.__init__(self, 'bmeip', 'qcloudcliV1', 'DescribeEipBmQuota', 'bmeip.api.qcloud.com')

