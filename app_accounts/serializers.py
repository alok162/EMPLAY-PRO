
from rest_framework import serializers
# from myapp.models import Users
from app_accounts.models import Account, Account_Risk
import json
from collections import defaultdict
from rest_framework.response import Response
import views

distinct_potential = defaultdict(int)
response = {}
class AccountSerializer(serializers.ModelSerializer):
	count=0
	def to_representation(self, obj):
		global distinct_potential, response
		if self.count==0:
			distinct_potential = defaultdict(int)
			response = {}
			response['totalChildAccount'] = 0
			response['totalAccountsWon'] = 0
			response['totalPotentials'] = 0
			response['totalPipelines'] = 0
			response['maxValueableId'] = 0
		self.count+=1
		temp_dict = {}
		d = json.dumps(obj)
		jsonObject = json.loads(d)
		for key in jsonObject:
			temp_dict[key] = jsonObject[key]
		if temp_dict['account_id'] not in distinct_potential and temp_dict['potential'] == 'HP':
			response['totalPotentials'] += 1
		if temp_dict['account_id'] not in distinct_potential and temp_dict['pipeline'] == 'HP':
			response['totalPipelines'] += 1
			response['totalChildAccount'] +=1
		if temp_dict['stage'] == 'Won':
			response['totalAccountsWon'] +=1

		if temp_dict['potential'] == 'HP':
			distinct_potential[temp_dict['account_id']] +=1
		if temp_dict['pipeline'] == 'HP':
			distinct_potential[temp_dict['account_id']] +=1
		for i in distinct_potential:
			if distinct_potential[i]>response['maxValueableId']:
				response['maxValueableId'] = i
		response['totalChildAccount']+=1

		if self.count == views.obj_len:
			self.count = 0
		return response


class AccountRiskSerializer(serializers.ModelSerializer):
	#model serializer inbuilt method with create() and update()
		class Meta:
			model = Account_Risk
			fields = '__all__'