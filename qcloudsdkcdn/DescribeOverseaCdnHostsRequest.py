# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeOverseaCdnHostsRequest(Request):

    def __init__(self):
        super(DescribeOverseaCdnHostsRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'DescribeOverseaCdnHosts', 'cdn.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_projects(self):
        return self.get_params().get('projects')

    def set_projects(self, projects):
        self.add_param('projects', projects)
