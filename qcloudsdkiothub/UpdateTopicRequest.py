# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateTopicRequest(Request):

    def __init__(self):
        super(UpdateTopicRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'UpdateTopic', 'iothub.api.qcloud.com')

    def get_action_name(self):
        return self.get_params().get('action_name')

    def set_action_name(self, action_name):
        self.add_param('action_name', action_name)

    def get_privilege(self):
        return self.get_params().get('privilege')

    def set_privilege(self, privilege):
        self.add_param('privilege', privilege)

    def get_topic_id(self):
        return self.get_params().get('topic_id')

    def set_topic_id(self, topic_id):
        self.add_param('topic_id', topic_id)
