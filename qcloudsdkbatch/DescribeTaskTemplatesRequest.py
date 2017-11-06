# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeTaskTemplatesRequest(Request):

    def __init__(self):
        super(DescribeTaskTemplatesRequest, self).__init__(
            'batch', 'qcloudcliV1', 'DescribeTaskTemplates', 'batch.api.qcloud.com')

    def get_Filters(self):
        return self.get_params().get('Filters')

    def set_Filters(self, Filters):
        self.add_param('Filters', Filters)

    def get_Limit(self):
        return self.get_params().get('Limit')

    def set_Limit(self, Limit):
        self.add_param('Limit', Limit)

    def get_Offset(self):
        return self.get_params().get('Offset')

    def set_Offset(self, Offset):
        self.add_param('Offset', Offset)

    def get_TaskTemplateIds(self):
        return self.get_params().get('TaskTemplateIds')

    def set_TaskTemplateIds(self, TaskTemplateIds):
        self.add_param('TaskTemplateIds', TaskTemplateIds)

    def get_Version(self):
        return self.get_params().get('Version')

    def set_Version(self, Version):
        self.add_param('Version', Version)
