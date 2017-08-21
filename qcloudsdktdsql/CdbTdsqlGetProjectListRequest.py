#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CdbTdsqlGetProjectListRequest(Request):

	def __init__(self):
		Request.__init__(self, 'tdsql', 'qcloudcliV1', 'CdbTdsqlGetProjectList', 'tdsql.api.qcloud.com')

