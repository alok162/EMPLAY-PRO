
from rest_framework import serializers
# from myapp.models import Users
from app_accounts.models import Account, Account_Risk
import json
from collections import defaultdict
from rest_framework.response import Response
import views

distinct_potential = defaultdict(int)
class AccountSerializer(serializers.ModelSerializer):
	# distinct_potential = defaultdict(int)
	response = {}
	response['totalChildAccount'] = 0
	response['totalAccountsWon'] = 0
	response['totalPotentials'] = 0
	response['totalPipelines'] = 0
	response['maxValueableId'] = 0
	count=0
	def to_representation(self, obj):
		global distinct_potential
		if self.count==0:
			distinct_potential = defaultdict(int)
		self.count+=1
		temp_dict = {}
		d = json.dumps(obj)
		jsonObject = json.loads(d)
		for key in jsonObject:
			temp_dict[key] = jsonObject[key]
		if temp_dict['account_id'] not in distinct_potential and temp_dict['potential'] == 'HP':
			self.response['totalPotentials'] += 1
		if temp_dict['account_id'] not in distinct_potential and temp_dict['pipeline'] == 'HP':
			self.response['totalPipelines'] += 1
			self.response['totalChildAccount'] +=1
		if temp_dict['stage'] == 'Won':
			self.response['totalAccountsWon'] +=1

		if temp_dict['potential'] == 'HP':
			distinct_potential[temp_dict['account_id']] +=1
		if temp_dict['pipeline'] == 'HP':
			distinct_potential[temp_dict['account_id']] +=1
		for i in distinct_potential:
			if distinct_potential[i]>self.response['maxValueableId']:
				self.response['maxValueableId'] = i
		self.response['totalChildAccount']+=1
		print temp_dict

		if self.count == views.obj_len:
			print 'alok kumar', distinct_potential, self.count, temp_dict
			distinct_potential = defaultdict(int)
			self.count = 0
			return self.response
		# print views.obj_len, self.distinct_potential

    	
	
	# model serializer inbuilt method with create() and update()
		# class Meta:
		# 	model = Account
		# 	fields = '__all__'


class AccountRiskSerializer(serializers.ModelSerializer):
	#model serializer inbuilt method with create() and update()
		class Meta:
			model = Account_Risk
			fields = '__all__'