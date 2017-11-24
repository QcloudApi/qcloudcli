# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyTaskTemplateRequest(Request):

    def __init__(self):
        super(ModifyTaskTemplateRequest, self).__init__(
            'batch', 'qcloudcliV1', 'ModifyTaskTemplate', 'batch.api.qcloud.com')

    def get_TaskTemplateDescription(self):
        return self.get_params().get('TaskTemplateDescription')

    def set_TaskTemplateDescription(self, TaskTemplateDescription):
        self.add_param('TaskTemplateDescription', TaskTemplateDescription)

    def get_TaskTemplateId(self):
        return self.get_params().get('TaskTemplateId')

    def set_TaskTemplateId(self, TaskTemplateId):
        self.add_param('TaskTemplateId', TaskTemplateId)

    def get_TaskTemplateInfo(self):
        return self.get_params().get('TaskTemplateInfo')

    def set_TaskTemplateInfo(self, TaskTemplateInfo):
        self.add_param('TaskTemplateInfo', TaskTemplateInfo)

    def get_TaskTemplateName(self):
        return self.get_params().get('TaskTemplateName')

    def set_TaskTemplateName(self, TaskTemplateName):
        self.add_param('TaskTemplateName', TaskTemplateName)

    def get_Version(self):
        return self.get_params().get('Version')

    def set_Version(self, Version):
        self.add_param('Version', Version)
