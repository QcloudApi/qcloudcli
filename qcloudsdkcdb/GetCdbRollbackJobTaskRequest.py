# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCdbRollbackJobTaskRequest(Request):

    def __init__(self):
        super(GetCdbRollbackJobTaskRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'GetCdbRollbackJobTask', 'cdb.api.qcloud.com')

    def get_jobId(self):
        return self.get_params().get('jobId')

    def set_jobId(self, jobId):
        self.add_param('jobId', jobId)
