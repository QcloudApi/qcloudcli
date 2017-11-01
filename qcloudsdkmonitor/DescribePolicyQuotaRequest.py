# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribePolicyQuotaRequest(Request):

    def __init__(self):
        super(DescribePolicyQuotaRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribePolicyQuota', 'monitor.api.qcloud.com')
