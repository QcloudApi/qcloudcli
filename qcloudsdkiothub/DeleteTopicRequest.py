#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteTopicRequest(Request):

	def __init__(self):
		Request.__init__(self, 'iothub', 'qcloudcliV1', 'DeleteTopic', 'iothub.api.qcloud.com')

	def get_instanceId(self):
		return self.get_params().get('instanceId')

	def set_instanceId(self, instanceId):
		self.add_param('instanceId', instanceId)

	def get_topicName(self):
		return self.get_params().get('topicName')

	def set_topicName(self, topicName):
		self.add_param('topicName', topicName)

	def get_topic_id(self):
		return self.get_params().get('topic_id')

	def set_topic_id(self, topic_id):
		self.add_param('topic_id', topic_id)

