# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteTaskTemplatesRequest(Request):

    def __init__(self):
        super(DeleteTaskTemplatesRequest, self).__init__(
            'batch', 'qcloudcliV1', 'DeleteTaskTemplates', 'batch.api.qcloud.com')

    def get_TaskTemplateIds(self):
        return self.get_params().get('TaskTemplateIds')

    def set_TaskTemplateIds(self, TaskTemplateIds):
        self.add_param('TaskTemplateIds', TaskTemplateIds)

    def get_Version(self):
        return self.get_params().get('Version')

    def set_Version(self, Version):
        self.add_param('Version', Version)
