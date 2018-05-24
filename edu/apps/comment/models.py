# encoding:utf-8
from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class info_package_from(models.Model):
    package_id = models.CharField(max_length=20, primary_key=True)
    package_from = models.CharField(max_length=20)

    class Meta:
        verbose_name = "资源包来源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.package_from





class info_school_type(models.Model):
    school_type_id = models.CharField(max_length=20, primary_key=True)
    school_type = models.CharField(max_length=20)

    class Meta:
        verbose_name = "学校类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.school_type


class info_school(models.Model):
    school_id = models.CharField(max_length=20, primary_key=True)
    school_name = models.CharField(max_length=20)
    school_type = models.CharField(max_length=20)
    school_type_id = models.ForeignKey(info_school_type, on_delete=models.CASCADE)
    school_location = models.CharField(max_length=20)
    is_key = models.SmallIntegerField()

    class Meta:
        verbose_name = "学校"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.school_name


class info_teacher(models.Model):
    teacher_id = models.CharField(max_length=20, primary_key=True)
    teacher_name = models.CharField(max_length=20)
    teacher_user_name = models.CharField(max_length=20)
    is_key = models.SmallIntegerField()

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher_name


class info_period(models.Model):
    period_id = models.CharField(max_length=20, primary_key=True)
    period = models.CharField(max_length=20)

    class Meta:
        verbose_name = "学段"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.period_id


class info_subject(models.Model):
    subject_id = models.CharField(max_length=20, primary_key=True)
    subject = models.CharField(max_length=20)

    class Meta:
        verbose_name = "学科"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class info_version(models.Model):
    version_id = models.CharField(max_length=20, primary_key=True)
    version = models.CharField(max_length=20)

    class Meta:
        verbose_name = "教科书版本"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.version_id


class info_grade(models.Model):
    grade_id = models.CharField(max_length=10, primary_key=True)
    grade = models.CharField(max_length=20)

    class Meta:
        verbose_name = "年级"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.grade_id


class rec_course(models.Model):
    lession_id = models.CharField(max_length=20, primary_key=True)
    period = models.ForeignKey(info_period, null=True,blank=True,on_delete=models.CASCADE)
    subject = models.ForeignKey(info_subject,null=True,blank=True, on_delete=models.CASCADE)
    version= models.ForeignKey(info_version,null=True,blank=True, on_delete=models.CASCADE)
    grade = models.ForeignKey(info_grade,null=True,blank=True, on_delete=models.CASCADE)
    chapter_id = models.SmallIntegerField(null=True,blank=True)
    section_id = models.SmallIntegerField(null=True,blank=True)
    lesson_name = models.CharField(max_length=30,null=True,blank=True)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.lession_id


class rec_package(models.Model):
    package_id = models.CharField(max_length=20, primary_key=True)
    package_from_id = models.ForeignKey(info_package_from,null=True,blank=True, on_delete=models.CASCADE)
    updata_school_id = models.ForeignKey(info_school,null=True,blank=True, on_delete=models.CASCADE)
    update_teacher_id = models.ForeignKey(info_teacher,null=True,blank=True, on_delete=models.CASCADE)
    lession_id = models.ForeignKey(rec_course,null=True,blank=True, on_delete=models.CASCADE)
    update_time = models.DateField(null=True,blank=True)
    view_count = models.BigIntegerField()
    comment_count = models.BigIntegerField()
    score = models.PositiveIntegerField()
    edu_design_id = models.CharField(max_length=20)
    edu_video_id = models.CharField(max_length=20)
    edu_resource = models.CharField(max_length=20)
    good_level = models.SmallIntegerField()

    class Meta:
        verbose_name = "资源包"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.package_id

class info_package_link(models.Model):
    linkid = models.CharField(max_length=10,primary_key=True)
    package_id = models.ForeignKey(rec_package,on_delete=models.CASCADE)
    package_to = models.CharField(max_length=20)

    class Meta:
        verbose_name = "资源包链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.package_to


class rec_package_view(models.Model):
    package_view_id = models.CharField(max_length=20, primary_key=True)
    package_id = models.ForeignKey(rec_package, on_delete=models.CASCADE)
    view_user_id = models.CharField(max_length=20)
    view_time = models.DateTimeField()

    class Meta:
        verbose_name = "资源包访问"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.package_view_id


class rec_package_comment(models.Model):
    package_comment_id = models.CharField(max_length=20, primary_key=True)
    package_id = models.ForeignKey(rec_package, on_delete=models.CASCADE)
    comment = models.CharField(max_length=20)
    comment_user_id = models.CharField(max_length=20)
    comment_time = models.DateTimeField()

    class Meta:
        verbose_name = "资源包评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.package_comment_id


class rec_package_score(models.Model):
    package_score_id = models.CharField(max_length=20, primary_key=True)
    package_id = models.ForeignKey(rec_package, on_delete=models.CASCADE)
    score = models.SmallIntegerField()
    score_user_id = models.CharField(max_length=20)
    score_time = models.DateTimeField()

    class Meta:
        verbose_name = "资源包点评"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.package_score_id


# class rec_package_link(models.Model):
#     package_link_id = models.CharField(max_length=20, primary_key=True)
#     link_type = models.SmallIntegerField()
#     link_from_id = models.CharField(max_length=20)
#     link_to_id = models.CharField(max_length=20)

#     class Meta:
#         verbose_name = "资源包链接"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.package_link_id
