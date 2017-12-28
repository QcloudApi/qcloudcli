# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeClassRequest(Request):

    def __init__(self):
        super(DescribeClassRequest, self).__init__(
            'vod', 'qcloudcliV1', 'DescribeClass', 'vod.api.qcloud.com')

    def get_SubAppId(self):
        return self.get_params().get('SubAppId')

    def set_SubAppId(self, SubAppId):
        self.add_param('SubAppId', SubAppId)
