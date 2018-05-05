# encoding: utf-8
import xadmin

from .models import info_grade, info_package_from, info_package_link, info_period, info_school, info_school_type
from .models import info_subject, info_teacher, info_version
from .models import rec_package_view, rec_course, rec_package, rec_package_comment, rec_package_score


# class grade_admin(object):
#     list_display = ["grade"]

class package_from_admin(object):
    list_display = ["package_id", "package_from"]


class package_link_admin(object):
    list_display = ["package_id", "package_to"]


class school_type_admin(object):
    list_display = ["school_type_id", "school_type"]


class school_admin(object):
    list_display = ["school_id", "school_name", "school_type", "school_type_id", "school_location", "is_key" ]


class teacher_admin(object):
    list_display = ["teacher_id", "teacher_name", "teacher_user_name", "is_key"]


class period_admin(object):
    list_display = ["period_id", "period"]


class subject_admin(object):
    list_play = ["subject_id", "subject"]


class version_admin(object):
    list_play = ["version_id", "version"]


class grade_admin(object):
    list_display = ["grade_id", "grade"]


class course_admin(object):
    list_display = ["lession_id", "period_id", "subject_id", "version_id", "grade_id", "chapter_id", "section_id", "lesson_name"]


class package_admin(object):
    list_display = ["package_id", "package_from_id", "updata_school_id", "update_teacher_id", "lession_id", "update_time", "view_count", "comment_count", "score", "edu_design_id", "edu_video_id", "edu_resource", "good_level"]


class package_view_admin(object):
    list_display = ["package_view_id", "package_id", "view_user_id", "view_time"]


class package_comment_admin(object):
    list_display = ["package_comment_id", "package_id", "comment", "comment_user_id", "comment_time"]


class package_score_admin(object):
    list_display = ["package_score_id", "package_id", "score", "score_user_id", "score_time"]


xadmin.site.register(info_package_from, package_from_admin)
xadmin.site.register(info_package_link, package_link_admin)
xadmin.site.register(info_school_type, school_type_admin)
xadmin.site.register(info_school, school_admin)
xadmin.site.register(info_period, period_admin)
xadmin.site.register(info_teacher, teacher_admin)
xadmin.site.register(info_subject, subject_admin)
xadmin.site.register(info_version, version_admin)
xadmin.site.register(info_grade, grade_admin)
xadmin.site.register(rec_course, course_admin)
xadmin.site.register(rec_package, package_admin)
xadmin.site.register(rec_package_comment, package_comment_admin)
xadmin.site.register(rec_package_score, package_score_admin)