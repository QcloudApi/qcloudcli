#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CreateTopicRequest(Request):

	def __init__(self):
		Request.__init__(self, 'iothub', 'qcloudcliV1', 'CreateTopic', 'iothub.api.qcloud.com')

	def get_instanceId(self):
		return self.get_params().get('instanceId')

	def set_instanceId(self, instanceId):
		self.add_param('instanceId', instanceId)

	def get_topicName(self):
		return self.get_params().get('topicName')

	def set_topicName(self, topicName):
		self.add_param('topicName', topicName)

	def get_partitionNum(self):
		return self.get_params().get('partitionNum')

	def set_partitionNum(self, partitionNum):
		self.add_param('partitionNum', partitionNum)

	def get_replicaNum(self):
		return self.get_params().get('replicaNum')

	def set_replicaNum(self, replicaNum):
		self.add_param('replicaNum', replicaNum)

	def get_enableWhiteList(self):
		return self.get_params().get('enableWhiteList')

	def set_enableWhiteList(self, enableWhiteList):
		self.add_param('enableWhiteList', enableWhiteList)

	def get_ipWhiteList(self):
		return self.get_params().get('ipWhiteList')

	def set_ipWhiteList(self, ipWhiteList):
		self.add_param('ipWhiteList', ipWhiteList)

	def get_thingtype_name(self):
		return self.get_params().get('thingtype_name')

	def set_thingtype_name(self, thingtype_name):
		self.add_param('thingtype_name', thingtype_name)

	def get_action_name(self):
		return self.get_params().get('action_name')

	def set_action_name(self, action_name):
		self.add_param('action_name', action_name)

	def get_privilege(self):
		return self.get_params().get('privilege')

	def set_privilege(self, privilege):
		self.add_param('privilege', privilege)

