# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlAssignToProjectRequest(Request):

    def __init__(self):
        super(CdbTdsqlAssignToProjectRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlAssignToProject', 'tdsql.api.qcloud.com')

    def get_cdbInstanceIds(self):
        return self.get_params().get('cdbInstanceIds')

    def set_cdbInstanceIds(self, cdbInstanceIds):
        self.add_param('cdbInstanceIds', cdbInstanceIds)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)
