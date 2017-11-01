# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TextDependencyRequest(Request):

    def __init__(self):
        super(TextDependencyRequest, self).__init__(
            'wenzhi', 'qcloudcliV1', 'TextDependency', 'wenzhi.api.qcloud.com')

    def get_content(self):
        return self.get_params().get('content')

    def set_content(self, content):
        self.add_param('content', content)
