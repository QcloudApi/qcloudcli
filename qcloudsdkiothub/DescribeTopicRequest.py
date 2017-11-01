# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeTopicRequest(Request):

    def __init__(self):
        super(DescribeTopicRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'DescribeTopic', 'iothub.api.qcloud.com')

    def get_topic_id(self):
        return self.get_params().get('topic_id')

    def set_topic_id(self, topic_id):
        self.add_param('topic_id', topic_id)
