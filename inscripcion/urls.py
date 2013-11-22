'''
Created on 22/11/2013

@author: darwelx
'''
# -*- coding: utf-8 *-*
from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^inscripcion/$', 'inscripcion.views.inscripcion'),
)