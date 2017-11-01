# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ClearCmemRequest(Request):

    def __init__(self):
        super(ClearCmemRequest, self).__init__(
            'cmem', 'qcloudcliV1', 'ClearCmem', 'cmem.api.qcloud.com')

    def get_cmemName(self):
        return self.get_params().get('cmemName')

    def set_cmemName(self, cmemName):
        self.add_param('cmemName', cmemName)
