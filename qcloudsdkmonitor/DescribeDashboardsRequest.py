# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeDashboardsRequest(Request):

    def __init__(self):
        super(DescribeDashboardsRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeDashboards', 'monitor.api.qcloud.com')
