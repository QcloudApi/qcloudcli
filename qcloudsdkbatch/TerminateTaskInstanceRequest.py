# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TerminateTaskInstanceRequest(Request):

    def __init__(self):
        super(TerminateTaskInstanceRequest, self).__init__(
            'batch', 'qcloudcliV1', 'TerminateTaskInstance', 'batch.api.qcloud.com')

    def get_JobId(self):
        return self.get_params().get('JobId')

    def set_JobId(self, JobId):
        self.add_param('JobId', JobId)

    def get_TaskInstanceIndex(self):
        return self.get_params().get('TaskInstanceIndex')

    def set_TaskInstanceIndex(self, TaskInstanceIndex):
        self.add_param('TaskInstanceIndex', TaskInstanceIndex)

    def get_TaskName(self):
        return self.get_params().get('TaskName')

    def set_TaskName(self, TaskName):
        self.add_param('TaskName', TaskName)

    def get_Version(self):
        return self.get_params().get('Version')

    def set_Version(self, Version):
        self.add_param('Version', Version)
