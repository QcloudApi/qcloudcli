# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateTicketRequest(Request):

    def __init__(self):
        super(CreateTicketRequest, self).__init__(
            'ticket', 'qcloudcliV1', 'CreateTicket', 'ticket.api.qcloud.com')

    def get_language(self):
        return self.get_params().get('language')

    def set_language(self, language):
        self.add_param('language', language)

    def get_appId(self):
        return self.get_params().get('appId')

    def set_appId(self, appId):
        self.add_param('appId', appId)

    def get_content(self):
        return self.get_params().get('content')

    def set_content(self, content):
        self.add_param('content', content)

    def get_customfields(self):
        return self.get_params().get('customfields')

    def set_customfields(self, customfields):
        self.add_param('customfields', customfields)

    def get_email(self):
        return self.get_params().get('email')

    def set_email(self, email):
        self.add_param('email', email)

    def get_level1_id(self):
        return self.get_params().get('level1_id')

    def set_level1_id(self, level1_id):
        self.add_param('level1_id', level1_id)

    def get_level2_id(self):
        return self.get_params().get('level2_id')

    def set_level2_id(self, level2_id):
        self.add_param('level2_id', level2_id)

    def get_level3_id(self):
        return self.get_params().get('level3_id')

    def set_level3_id(self, level3_id):
        self.add_param('level3_id', level3_id)

    def get_national_code(self):
        return self.get_params().get('national_code')

    def set_national_code(self, national_code):
        self.add_param('national_code', national_code)

    def get_ownerUin(self):
        return self.get_params().get('ownerUin')

    def set_ownerUin(self, ownerUin):
        self.add_param('ownerUin', ownerUin)

    def get_phone(self):
        return self.get_params().get('phone')

    def set_phone(self, phone):
        self.add_param('phone', phone)

    def get_postUin(self):
        return self.get_params().get('postUin')

    def set_postUin(self, postUin):
        self.add_param('postUin', postUin)

    def get_queue(self):
        return self.get_params().get('queue')

    def set_queue(self, queue):
        self.add_param('queue', queue)

    def get_secret_content(self):
        return self.get_params().get('secret_content')

    def set_secret_content(self, secret_content):
        self.add_param('secret_content', secret_content)

    def get_serviceSceneCode(self):
        return self.get_params().get('serviceSceneCode')

    def set_serviceSceneCode(self, serviceSceneCode):
        self.add_param('serviceSceneCode', serviceSceneCode)

    def get_time_period(self):
        return self.get_params().get('time_period')

    def set_time_period(self, time_period):
        self.add_param('time_period', time_period)

    def get_titleId(self):
        return self.get_params().get('titleId')

    def set_titleId(self, titleId):
        self.add_param('titleId', titleId)
