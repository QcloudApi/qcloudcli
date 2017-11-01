# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class QueryJobTaskRequest(Request):

    def __init__(self):
        super(QueryJobTaskRequest, self).__init__(
            'helix', 'qcloudcliV1', 'QueryJobTask', 'helix.api.qcloud.com')

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_taskId(self):
        return self.get_params().get('taskId')

    def set_taskId(self, taskId):
        self.add_param('taskId', taskId)
