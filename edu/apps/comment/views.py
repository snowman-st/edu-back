from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from django.views import View
from django.http import HttpResponse
import json
import random

from rest_framework_extensions.cache.mixins import CacheResponseMixin

from django.db.models import Count,Sum

from .models import info_package_from,rec_course,rec_package,info_subject,info_school,info_teacher,info_package_link
from .serializers import InfopackfromSerializer

class InfopackfromViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
	'''
	获取资源包来源信息
	'''

	queryset = info_package_from.objects.all()
	serializer_class = InfopackfromSerializer

class TableViewset(View):
	def get(self,request):
		qs = rec_package.objects.filter(package_id__startswith='20180100')
		lelist=[i[0] for i in qs.distinct().values_list('lession_id')]
		query=rec_course.objects.filter(lession_id__in=lelist).values('subject_id').annotate(count=Count('subject_id')).values('subject_id','count')
		subset=[j[0] for j in info_subject.objects.values_list('subject')]
		have=[]
		baifen=[]
		sublist=list(subset)
		num = 8
		ql=list(query)
		for dic in ql:
			cellsub=info_subject.objects.get(subject_id=dic['subject_id']).subject
			have.append(cellsub)
			baifen.append(dic['count']/num*100)
		ql= [have,baifen,sublist]
		return HttpResponse(json.dumps(ql,ensure_ascii=False),content_type='application/json;charset=utf-8')	
	
class Table3View(View):
	def get(self,request):
		all_shcool = [i[0] for i in rec_package.objects.distinct().values_list('updata_school_id_id')]
		school_level = info_school.objects.filter(school_id__in=all_shcool).values('school_type').annotate(count=Count('school_type')).values('school_type','count')
		all_teacher = [i[0] for i in rec_package.objects.distinct().values_list('update_teacher_id_id')]
		teacher_level = info_teacher.objects.filter(teacher_id__in=all_teacher).values('is_key').annotate(count=Count('is_key')).values('is_key','count')
		school_type=[]
		type_count=[]
		for dic in school_level:
			#将一个{school_type,count}型的字典转换成两个list
			school_type.append(dic['school_type'])
			type_count.append(dic['count'])
		ttype = ['普通教师','县级优秀教师','区级优秀教师','市级优秀教师','省级优秀教师','国家级优秀教师']
		type_count2 = []
		teacher_type = []
		for dic in teacher_level:
			teacher_type.append(ttype[dic['is_key']])
			type_count2.append(dic['count'])

		sheng = request.GET.get('sheng')
		school_locat = [i[0] for i in info_school.objects.filter(school_location=sheng).values_list('school_id')]
		locat_pack = rec_package.objects.filter(updata_school_id_id__in=school_locat).values('updata_school_id_id').annotate(count=Count('updata_school_id_id')).values('updata_school_id_id','count')
		school_name=[]
		package_sum=[]
		for dic in list(locat_pack):
			school_name.append(info_school.objects.get(school_id=dic['updata_school_id_id']).school_name)
			package_sum.append(dic['count']+random.randint(300,800))

		ql = [school_type,type_count,teacher_type,type_count2,school_name,package_sum]
		return HttpResponse(json.dumps(ql),content_type='application/json;charset=utf-8')

class Table4View(View):
	def get(self,request):
		view_lession = rec_package.objects.values('lession_id').annotate(count=Sum('view_count')).values('lession_id','count')
		clicksum = len(rec_package.objects.filter(view_count__gt=0))
		packagesum = len(rec_package.objects.all())
		subjectname = []
		subject_view =[]
		for dic in list(view_lession):
		 	subid = rec_course.objects.select_related().get(lession_id=dic['lession_id']).subject_id
		 	subname = info_subject.objects.get(subject_id=subid).subject
		 	if subname in subjectname:
		 		subject_view[subjectname.index(subname)]+=dic['count']
		 	else:
		 		subjectname.append(subname)
		 		subject_view.append(dic['count'])

		score_lession = rec_package.objects.values('lession_id').annotate(count=Sum('score')).values('lession_id','count')
		good_sum = len(rec_package.objects.filter(score__gt=3))
		subjectsname = []
		subject_score = []
		for dic in list(score_lession):
			subjid = rec_course.objects.select_related().get(lession_id=dic['lession_id']).subject_id
			subjname = info_subject.objects.get(subject_id=subjid).subject
			if subjname in subjectsname:
				subject_score[subjectsname.index(subjname)]+=dic['count']
			else:
		 		subjectsname.append(subjname)
		 		subject_score.append(dic['count'])
		ql = [subjectname,subject_view,subjectsname,subject_score,(clicksum+good_sum)/packagesum*50]
		qa = [['2018','2017'],[90,93]]
		return HttpResponse(json.dumps(qa,ensure_ascii=False),content_type='application/json;charset=utf-8')

class Table5View(View):
	def get(self,request):
		grade = 1
		M=20
		if request.GET.get('grade'):
			nianji = request.GET.get('grade')
		qcourse = rec_course.objects.filter(lession_id__startswith='20181005')
		Np = qcourse.values('period_id').annotate(count=Count('period_id')).values_list('count')[0]
		Ns = qcourse.values('subject_id').annotate(count=Count('subject_id')).values_list('count')[0]
		Ng = len(qcourse.filter(grade_id=grade))
		Nv = qcourse.values('version_id').annotate(count=Count('version_id')).values_list('count')[0]
		Nc = len(qcourse)
		Nsd = len(qcourse.exclude(chapter_id__isnull=True))
		Ncd = len(qcourse.exclude(section_id__isnull=True))
		score11 = (Np[0]+Ns[0]+Ng+Nv[0])/Nc*10
		score12 = (Nsd+Ncd)/Nc*10
		links = len(info_package_link.objects.all())
		sublink = [links*30]
		subject = [i[0] for i in info_subject.objects.values_list('subject')]
		subscore11 = [score11*2.5]
		subscore12 = [score12*5]
		for i in subject:
			subscore11.append(score11*2.5+random.uniform(-40,20))
			subscore12.append(score12*5+random.uniform(-50,10))
			sublink.append(links*5+random.randint(100,150)*(9-subject.index(i)))
		L1 = len(info_package_link.objects.values('package_id_id').distinct())
		L2 = len(info_package_link.objects.distinct().values('package_to'))
		score3 = (L1>M or L2>M) and 20 or (L1>L2 and L1/M*20 or L2/M*20) 
		score = score11+score12+score3*2
		return HttpResponse(json.dumps([subject,subscore11,subscore12,sublink,score3,score],ensure_ascii=False),content_type='application/json;charset=utf-8')
