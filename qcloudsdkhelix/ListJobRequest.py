# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListJobRequest(Request):

    def __init__(self):
        super(ListJobRequest, self).__init__(
            'helix', 'qcloudcliV1', 'ListJob', 'helix.api.qcloud.com')

    def get_count(self):
        return self.get_params().get('count')

    def set_count(self, count):
        self.add_param('count', count)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_startIndex(self):
        return self.get_params().get('startIndex')

    def set_startIndex(self, startIndex):
        self.add_param('startIndex', startIndex)
