# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCdnHostsRequest(Request):

    def __init__(self):
        super(DescribeCdnHostsRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'DescribeCdnHosts', 'cdn.api.qcloud.com')

    def get_detail(self):
        return self.get_params().get('detail')

    def set_detail(self, detail):
        self.add_param('detail', detail)

    def get_keyword(self):
        return self.get_params().get('keyword')

    def set_keyword(self, keyword):
        self.add_param('keyword', keyword)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_mode(self):
        return self.get_params().get('mode')

    def set_mode(self, mode):
        self.add_param('mode', mode)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_projects(self):
        return self.get_params().get('projects')

    def set_projects(self, projects):
        self.add_param('projects', projects)
