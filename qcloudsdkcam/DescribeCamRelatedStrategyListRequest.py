# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCamRelatedStrategyListRequest(Request):

    def __init__(self):
        super(DescribeCamRelatedStrategyListRequest, self).__init__(
            'cam', 'qcloudcliV1', 'DescribeCamRelatedStrategyList', 'cam.api.qcloud.com')
