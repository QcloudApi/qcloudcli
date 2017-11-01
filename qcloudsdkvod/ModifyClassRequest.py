# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyClassRequest(Request):

    def __init__(self):
        super(ModifyClassRequest, self).__init__(
            'vod', 'qcloudcliV1', 'ModifyClass', 'vod.api.qcloud.com')

    def get_classId(self):
        return self.get_params().get('classId')

    def set_classId(self, classId):
        self.add_param('classId', classId)

    def get_className(self):
        return self.get_params().get('className')

    def set_className(self, className):
        self.add_param('className', className)
