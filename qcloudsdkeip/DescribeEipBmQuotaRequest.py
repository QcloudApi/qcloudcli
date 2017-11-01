# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeEipBmQuotaRequest(Request):

    def __init__(self):
        super(DescribeEipBmQuotaRequest, self).__init__(
            'eip', 'qcloudcliV1', 'DescribeEipBmQuota', 'eip.api.qcloud.com')
