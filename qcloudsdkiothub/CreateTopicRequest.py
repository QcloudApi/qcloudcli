# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateTopicRequest(Request):

    def __init__(self):
        super(CreateTopicRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'CreateTopic', 'iothub.api.qcloud.com')

    def get_action_name(self):
        return self.get_params().get('action_name')

    def set_action_name(self, action_name):
        self.add_param('action_name', action_name)

    def get_privilege(self):
        return self.get_params().get('privilege')

    def set_privilege(self, privilege):
        self.add_param('privilege', privilege)

    def get_thingtype_name(self):
        return self.get_params().get('thingtype_name')

    def set_thingtype_name(self, thingtype_name):
        self.add_param('thingtype_name', thingtype_name)
