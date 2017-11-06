# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AddYYCdnHostRequest(Request):

    def __init__(self):
        super(AddYYCdnHostRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'AddYYCdnHost', 'cdn.api.qcloud.com')

    def get_antiStealingLink(self):
        return self.get_params().get('antiStealingLink')

    def set_antiStealingLink(self, antiStealingLink):
        self.add_param('antiStealingLink', antiStealingLink)

    def get_cacheRule(self):
        return self.get_params().get('cacheRule')

    def set_cacheRule(self, cacheRule):
        self.add_param('cacheRule', cacheRule)

    def get_ctcBackupCnc(self):
        return self.get_params().get('ctcBackupCnc')

    def set_ctcBackupCnc(self, ctcBackupCnc):
        self.add_param('ctcBackupCnc', ctcBackupCnc)

    def get_domain(self):
        return self.get_params().get('domain')

    def set_domain(self, domain):
        self.add_param('domain', domain)

    def get_expectedBandwidth(self):
        return self.get_params().get('expectedBandwidth')

    def set_expectedBandwidth(self, expectedBandwidth):
        self.add_param('expectedBandwidth', expectedBandwidth)

    def get_haveDynamicResource(self):
        return self.get_params().get('haveDynamicResource')

    def set_haveDynamicResource(self, haveDynamicResource):
        self.add_param('haveDynamicResource', haveDynamicResource)

    def get_httpsCrt(self):
        return self.get_params().get('httpsCrt')

    def set_httpsCrt(self, httpsCrt):
        self.add_param('httpsCrt', httpsCrt)

    def get_httpsKey(self):
        return self.get_params().get('httpsKey')

    def set_httpsKey(self, httpsKey):
        self.add_param('httpsKey', httpsKey)

    def get_remark(self):
        return self.get_params().get('remark')

    def set_remark(self, remark):
        self.add_param('remark', remark)

    def get_schemeMode(self):
        return self.get_params().get('schemeMode')

    def set_schemeMode(self, schemeMode):
        self.add_param('schemeMode', schemeMode)

    def get_src(self):
        return self.get_params().get('src')

    def set_src(self, src):
        self.add_param('src', src)

    def get_srcMethod(self):
        return self.get_params().get('srcMethod')

    def set_srcMethod(self, srcMethod):
        self.add_param('srcMethod', srcMethod)

    def get_testUrl(self):
        return self.get_params().get('testUrl')

    def set_testUrl(self, testUrl):
        self.add_param('testUrl', testUrl)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
