# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeRecordPlayInfoRequest(Request):

    def __init__(self):
        super(DescribeRecordPlayInfoRequest, self).__init__(
            'vod', 'qcloudcliV1', 'DescribeRecordPlayInfo', 'vod.api.qcloud.com')

    def get_SubAppId(self):
        return self.get_params().get('SubAppId')

    def set_SubAppId(self, SubAppId):
        self.add_param('SubAppId', SubAppId)

    def get_notifyUrl(self):
        return self.get_params().get('notifyUrl')

    def set_notifyUrl(self, notifyUrl):
        self.add_param('notifyUrl', notifyUrl)

    def get_vid(self):
        return self.get_params().get('vid')

    def set_vid(self, vid):
        self.add_param('vid', vid)
