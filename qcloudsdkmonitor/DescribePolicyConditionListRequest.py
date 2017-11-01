# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribePolicyConditionListRequest(Request):

    def __init__(self):
        super(DescribePolicyConditionListRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribePolicyConditionList', 'monitor.api.qcloud.com')
