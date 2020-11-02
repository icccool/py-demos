#!/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: lanxiong lanxiong@hydee.cn
@file: jks.py
@time: 2020/4/29 10:51
@desc:
'''

import jenkins

branch = 'V1.5.3'

all_jobs = {
    # 'basedata': 'V1.5.0.1',
    # 'basedata-batch-export': 'origin/dev',
    # 'development-management': 'origin/develop',
    # 'goods-collect': 'origin/develop',
    # 'h3': 'v1.5.3',
    # 'h3-basic-setting': 'V1.5.3',
    # 'h3-customer': branch,
    # 'h3-customplatform-process': 'V1.5.2',
    # 'h3-finance': branch,
    # 'h3-initdata': branch,
    # 'h3-job-admin': 'origin/master',
    # 'h3-manager': 'v1.6.1.1',
    # 'h3-orgmanager': 'v1.5.3',
    # 'h3-pos-transmission': 'v1.5.2.1',
    #
    # 'h3-promotion': 'V1.5.2.1',
    # 'h3-purchase': 'v1.5.2',
    # 'h3-report': branch,
    # 'h3-stock': 'V1.5.1.1',
    # 'h3-store': 'v1.5.3',
    # 'h3-supplier': 'V1.5.2',
    # 'h3-trade': 'V1.5.2.2',

    'h3-purchase': 'v1.5.5',
    'h3-ware': 'v1.5.5',
    'h3-orgmanager': 'v1.5.5',
    'h3-warehouse': 'v1.5.5',
    'h3-price': 'v1.5.5.1',
    'h3-basic-setting': 'v1.5.5',
    'h3-finance': 'v1.5.5',
    'basedata': 'v1.5.2',
}


env = 'pro'
env_password = 'ansible@jenkins211'

server = jenkins.Jenkins('http://192.168.10.58:8088/jenkins/', username='1admin', password='hydeeh3@2019')

"""
data = [('jar_name', 'h3-authorization-center'),
        ('jar_name', 'h3-orgmanager-center'),
        ('hydee_git_branch', 'v1.5.3'),
        ('env', 'pro'),
        ('env_password', 'ansible@jenkins211')]
"""

jobs = {}
for j in server.get_jobs():
    info = server.get_job_info(j['name'])
    jobs[j['name']] = ''
    if info['property']:
        for i in info['property']:
            if i['_class'] == 'hudson.model.ParametersDefinitionProperty':
                params = i['parameterDefinitions']
                for i in params:
                    if i['name'] == 'jar_name':
                        jobs[j['name']] = i['defaultParameterValue']['value']
                break

for k, v in list(jobs.items()):
    if k not in all_jobs:
        continue
    params = [('hydee_git_branch', all_jobs[k]),
              ('env', env),
              ('env_password', env_password)]
    for i in v.split(','):
        i and params.append(('jar_name', str(i)))
    print(k, params)
    try:
        res = server.build_job(k, parameters=params)
    except Exception as e:
        print('Error %s' % k)
        # print e.message
