#!/usr/bin/python
#-*-coding:utf-8-*-

from django.forms.fields import CharField
from validators import idcard

class IdCardField(CharField):
    default_error_messages = {
        'invalid':u'请输入正确的身份证号',
        'required':u'身份证号必须要填',
    }
    default_validators = [idcard]
