# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyLoadBalancerListenerRequest(Request):

    def __init__(self):
        super(ModifyLoadBalancerListenerRequest, self).__init__(
            'lb', 'qcloudcliV1', 'ModifyLoadBalancerListener', 'lb.api.qcloud.com')

    def get_healthNum(self):
        return self.get_params().get('healthNum')

    def set_healthNum(self, healthNum):
        self.add_param('healthNum', healthNum)

    def get_healthSwitch(self):
        return self.get_params().get('healthSwitch')

    def set_healthSwitch(self, healthSwitch):
        self.add_param('healthSwitch', healthSwitch)

    def get_httpHash(self):
        return self.get_params().get('httpHash')

    def set_httpHash(self, httpHash):
        self.add_param('httpHash', httpHash)

    def get_intervalTime(self):
        return self.get_params().get('intervalTime')

    def set_intervalTime(self, intervalTime):
        self.add_param('intervalTime', intervalTime)

    def get_listenerId(self):
        return self.get_params().get('listenerId')

    def set_listenerId(self, listenerId):
        self.add_param('listenerId', listenerId)

    def get_listenerName(self):
        return self.get_params().get('listenerName')

    def set_listenerName(self, listenerName):
        self.add_param('listenerName', listenerName)

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)

    def get_sessionExpire(self):
        return self.get_params().get('sessionExpire')

    def set_sessionExpire(self, sessionExpire):
        self.add_param('sessionExpire', sessionExpire)

    def get_timeOut(self):
        return self.get_params().get('timeOut')

    def set_timeOut(self, timeOut):
        self.add_param('timeOut', timeOut)

    def get_unhealthNum(self):
        return self.get_params().get('unhealthNum')

    def set_unhealthNum(self, unhealthNum):
        self.add_param('unhealthNum', unhealthNum)
