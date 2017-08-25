import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, parent_dir)

class UserInfo:
	def __init__(self, secret_id, secret_key, method, region_id, auto_retry=True, max_retry_time=3, user_agent=None,port = 80):
		pass
	def set_user_info(self,secret_id, secret_key, method, region_id, auto_retry=True, max_retry_time=3, user_agent=None,port = 80):
		self.secret_id = secret_id
		self.secret_key = secret_key
		self.request_method = method
		self.region_id = region_id
		self.auto_retry = auto_retry
		self.max_retry_num = max_retry_time
		self.user_agent = user_agent
		self.port = port


	def get_region_id(self):

		return self.__region_id

	def get_secretkey(self):

		return self.__secret_key

	def get_access_secret(self):

		return self.__secret_id

	def is_auto_retry(self):

		return self.__auto_retry

	def get_max_retry_num(self):

		return self.__max_retry_num

	def get_user_agent(self):

		return self.__user_agent

	def set_region_id(self, region):
		self.__region_id = region

	def set_secret_key(self, secret_key):
		self.__secret_key = secret_key

	def set_secret_id(self, secret_id):
		self.__secret_id = secret_id

	def set_max_retry_num(self, num):

		self.__max_retry_num = num

	def set_auto_retry(self, flag):

		self.__auto_retry = flag

	def set_user_agent(self, agent):

		self.__user_agent = agent

