#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class StartJobRequest(Request):

	def __init__(self):
		Request.__init__(self, 'helix', 'qcloudcliV1', 'StartJob', 'helix.api.qcloud.com')

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)

	def get_secretId(self):
		return self.get_params().get('secretId')

	def set_secretId(self, secretId):
		self.add_param('secretId', secretId)

	def get_secretKey(self):
		return self.get_params().get('secretKey')

	def set_secretKey(self, secretKey):
		self.add_param('secretKey', secretKey)

	def get_jobDesc(self):
		return self.get_params().get('jobDesc')

	def set_jobDesc(self, jobDesc):
		self.add_param('jobDesc', jobDesc)

	def get_jobName(self):
		return self.get_params().get('jobName')

	def set_jobName(self, jobName):
		self.add_param('jobName', jobName)

	def get_timeout(self):
		return self.get_params().get('timeout')

	def set_timeout(self, timeout):
		self.add_param('timeout', timeout)

	def get_imgId(self):
		return self.get_params().get('imgId')

	def set_imgId(self, imgId):
		self.add_param('imgId', imgId)

	def get_cmd(self):
		return self.get_params().get('cmd')

	def set_cmd(self, cmd):
		self.add_param('cmd', cmd)

	def get_instanceType(self):
		return self.get_params().get('instanceType')

	def set_instanceType(self, instanceType):
		self.add_param('instanceType', instanceType)

	def get_rootPassword(self):
		return self.get_params().get('rootPassword')

	def set_rootPassword(self, rootPassword):
		self.add_param('rootPassword', rootPassword)

	def get_dataDiskSize(self):
		return self.get_params().get('dataDiskSize')

	def set_dataDiskSize(self, dataDiskSize):
		self.add_param('dataDiskSize', dataDiskSize)

	def get_vpcid(self):
		return self.get_params().get('vpcid')

	def set_vpcid(self, vpcid):
		self.add_param('vpcid', vpcid)

	def get_subnetid(self):
		return self.get_params().get('subnetid')

	def set_subnetid(self, subnetid):
		self.add_param('subnetid', subnetid)

	def get_extMountPathMap(self):
		return self.get_params().get('extMountPathMap')

	def set_extMountPathMap(self, extMountPathMap):
		self.add_param('extMountPathMap', extMountPathMap)

	def get_extOutputPathMap(self):
		return self.get_params().get('extOutputPathMap')

	def set_extOutputPathMap(self, extOutputPathMap):
		self.add_param('extOutputPathMap', extOutputPathMap)

	def get_taskName(self):
		return self.get_params().get('taskName')

	def set_taskName(self, taskName):
		self.add_param('taskName', taskName)

	def get_priority(self):
		return self.get_params().get('priority')

	def set_priority(self, priority):
		self.add_param('priority', priority)

	def get_zone(self):
		return self.get_params().get('zone')

	def set_zone(self, zone):
		self.add_param('zone', zone)

	def get_dataDiskPath(self):
		return self.get_params().get('dataDiskPath')

	def set_dataDiskPath(self, dataDiskPath):
		self.add_param('dataDiskPath', dataDiskPath)

	def get_projectLocalPath(self):
		return self.get_params().get('projectLocalPath')

	def set_projectLocalPath(self, projectLocalPath):
		self.add_param('projectLocalPath', projectLocalPath)

	def get_tasks(self):
		return self.get_params().get('tasks')

	def set_tasks(self, tasks):
		self.add_param('tasks', tasks)

	def get_depend(self):
		return self.get_params().get('depend')

	def set_depend(self, depend):
		self.add_param('depend', depend)

