# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateClassRequest(Request):

    def __init__(self):
        super(CreateClassRequest, self).__init__(
            'vod', 'qcloudcliV1', 'CreateClass', 'vod.api.qcloud.com')

    def get_className(self):
        return self.get_params().get('className')

    def set_className(self, className):
        self.add_param('className', className)

    def get_parentId(self):
        return self.get_params().get('parentId')

    def set_parentId(self, parentId):
        self.add_param('parentId', parentId)
