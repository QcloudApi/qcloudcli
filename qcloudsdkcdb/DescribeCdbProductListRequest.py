# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCdbProductListRequest(Request):

    def __init__(self):
        super(DescribeCdbProductListRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'DescribeCdbProductList', 'cdb.api.qcloud.com')
