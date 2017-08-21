#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CreateScalingNotificationRequest(Request):

	def __init__(self):
		Request.__init__(self, 'scaling', 'qcloudcliV1', 'CreateScalingNotification', 'scaling.api.qcloud.com')

	def get_scalingGroupId(self):
		return self.get_params().get('scalingGroupId')

	def set_scalingGroupId(self, scalingGroupId):
		self.add_param('scalingGroupId', scalingGroupId)

	def get_notificationTypes(self):
		return self.get_params().get('notificationTypes')

	def set_notificationTypes(self, notificationTypes):
		self.add_param('notificationTypes', notificationTypes)

	def get_receiversIds(self):
		return self.get_params().get('receiversIds')

	def set_receiversIds(self, receiversIds):
		self.add_param('receiversIds', receiversIds)

	def get_notificationName(self):
		return self.get_params().get('notificationName')

	def set_notificationName(self, notificationName):
		self.add_param('notificationName', notificationName)

