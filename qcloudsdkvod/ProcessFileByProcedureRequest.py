# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ProcessFileByProcedureRequest(Request):

    def __init__(self):
        super(ProcessFileByProcedureRequest, self).__init__(
            'vod', 'qcloudcliV1', 'ProcessFileByProcedure', 'vod.api.qcloud.com')

    def get_fileId(self):
        return self.get_params().get('fileId')

    def set_fileId(self, fileId):
        self.add_param('fileId', fileId)

    def get_procedure(self):
        return self.get_params().get('procedure')

    def set_procedure(self, procedure):
        self.add_param('procedure', procedure)
