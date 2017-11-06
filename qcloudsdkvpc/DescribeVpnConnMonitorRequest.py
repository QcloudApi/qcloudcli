# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeVpnConnMonitorRequest(Request):

    def __init__(self):
        super(DescribeVpnConnMonitorRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeVpnConnMonitor', 'vpc.api.qcloud.com')

    def get_endtime(self):
        return self.get_params().get('endtime')

    def set_endtime(self, endtime):
        self.add_param('endtime', endtime)

    def get_metricName(self):
        return self.get_params().get('metricName')

    def set_metricName(self, metricName):
        self.add_param('metricName', metricName)

    def get_starttime(self):
        return self.get_params().get('starttime')

    def set_starttime(self, starttime):
        self.add_param('starttime', starttime)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)

    def get_vpnConnId(self):
        return self.get_params().get('vpnConnId')

    def set_vpnConnId(self, vpnConnId):
        self.add_param('vpnConnId', vpnConnId)

    def get_vpnGwId(self):
        return self.get_params().get('vpnGwId')

    def set_vpnGwId(self, vpnGwId):
        self.add_param('vpnGwId', vpnGwId)
