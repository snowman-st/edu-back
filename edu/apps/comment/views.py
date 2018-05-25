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

		provin_list = [i[0] for i in info_school.objects.distinct().values_list('school_location')]
		provinsum_list=[]
		for p in provin_list:
			school_locat = [i[0] for i in info_school.objects.filter(school_location=p).values_list('school_id')]
			provinsum_list.append(len(rec_package.objects.filter(updata_school_id_id__in=school_locat)))

		province = request.GET.get('province')
		school_locat = [i[0] for i in info_school.objects.filter(school_location=province).values_list('school_id')]
		locat_pack = rec_package.objects.filter(updata_school_id_id__in=school_locat).values('updata_school_id_id').annotate(count=Count('updata_school_id_id')).values('updata_school_id_id','count')
		school_name=[]
		package_sum=[]
		for dic in list(locat_pack):
			school_name.append(info_school.objects.get(school_id=dic['updata_school_id_id']).school_name)
			package_sum.append(dic['count']+random.randint(300,800))

		ql = [school_type,type_count,teacher_type,type_count2,provin_list,provinsum_list,school_name,package_sum]
		return HttpResponse(json.dumps(ql),content_type='application/json;charset=utf-8')
#前四个返回值不用说
#第五、六个是全国各省及各省上传资源包总量
#第七、八个返回值用于：当用户点击地图上的某一个省份时，后台获取到一个 province 的参数
#然后第七个返回值是该省份下的所有学校，第八个参数是每个学校上传的资源包数量
#目前数据库中  陕西  和  北京  的学校数量多，可用这两个地区进行展示


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

		highrank_lession = view_lession.order_by('-count')[:10]
		rank_lession = []
		rank_lession_view = []
		rank_lession_score = []
		rank_lession_sum = []
		for dic in list(highrank_lession):
			rank_lession.append(rec_course.objects.get(lession_id=dic['lession_id']).lesson_name)
			rank_lession_score.append(score_lession.get(lession_id=dic['lession_id'])['count'])
			rank_lession_view.append(dic['count'])
		rank_lession_sum = map(lambda a:a[0]+a[1],zip(rank_lession_score,rank_lession_view))
		tmprank = sorted(zip(rank_lession,rank_lession_view,rank_lession_score,rank_lession_sum),key = lambda a:a[3],reverse=True)
		rank_index = list(zip(*tmprank))
		ql = [subjectname,subject_view,subjectsname,subject_score,(clicksum+good_sum)/packagesum*50,rank_index[0],rank_index[1],rank_index[2]]
		return HttpResponse(json.dumps(ql,ensure_ascii=False),content_type='application/json;charset=utf-8')
#第五个返回值是可用性的评价总得分
#第六个是按照浏览量和评分相加之和排名较高的课程名
#第7个是课程名对应的浏览量
#第8个是课程名对应的评分


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
#接受一个grade参数用于指定年级，若从前端没有发送grade，默认值为1；
#subscore11是各个学科模块化得分，subscore12是层次化得分
#sublink是各科链接总数
#score是系统组织方式总得分