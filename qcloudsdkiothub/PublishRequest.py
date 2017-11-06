# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class PublishRequest(Request):

    def __init__(self):
        super(PublishRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'Publish', 'iothub.api.qcloud.com')

    def get_payload(self):
        return self.get_params().get('payload')

    def set_payload(self, payload):
        self.add_param('payload', payload)

    def get_topic(self):
        return self.get_params().get('topic')

    def set_topic(self, topic):
        self.add_param('topic', topic)
