# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeEipQuotaRequest(Request):

    def __init__(self):
        super(DescribeEipQuotaRequest, self).__init__(
            'eip', 'qcloudcliV1', 'DescribeEipQuota', 'eip.api.qcloud.com')
