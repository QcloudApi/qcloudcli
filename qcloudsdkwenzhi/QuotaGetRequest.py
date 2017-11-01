# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class QuotaGetRequest(Request):

    def __init__(self):
        super(QuotaGetRequest, self).__init__(
            'wenzhi', 'qcloudcliV1', 'QuotaGet', 'wenzhi.api.qcloud.com')
