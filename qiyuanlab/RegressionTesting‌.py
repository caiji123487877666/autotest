# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    ：2025/7/1 15:02
# @Author  : _Gy
# @File    : RegressionTesting.py
# @Software: PyCharm
import requests
'''
{"code":0,"data":{"userId":1,"accessToken":"38bed776cb154082a20f351fa390675b","refreshToken":"bdfca8c96ef64674ad5b521a9b72740b","expiresTime":1751358066090},"msg":""}
'''
# json = {'username': "admin", 'password': "HcW*bV%$a^&A@A8N"}
# res = requests.request('POST','https://algos.qiyuanlab.com/admin-api/system/auth/login',json=json,headers={'Content-Type':'application/json'})
# print(res.json()['data']['accessToken'])
# token = 'Bearer '+ res.json()['data']['accessToken']
token = 'Bearer e760eca19dfd486f9e8efde4d30a5c50'
headers = {'Content-Type':'application/json',"authorization":token}

# url_list = ['https://algos.qiyuanlab.com/admin-api/app/person-resource/query','https://algos.qiyuanlab.com/admin-api/app/project-group/haveProjectGroup',
#             'https://algos.qiyuanlab.com/admin-api/app/datasets/list?query=','https://algos.qiyuanlab.com/admin-api/app/project-group/getUserProjectAndResource',
#             'https://algos.qiyuanlab.com/admin-api/app/image/parent-list',' https://algos.qiyuanlab.com/admin-api/infra/file-config/list',
#             'https://algos.qiyuanlab.com/admin-api/app/resources/getResourcesByCondition?projectGroupId=1&imageId=226&chipType=',
#             'https://algos.qiyuanlab.com/admin-api/app/algorithms/get?id=2722',
#             'https://algos.qiyuanlab.com/admin-api/app/algorithms/page?name=&status=&showMore=false&resourceId=&chipType=&image=&pageNo=1&pageSize=12',
#             'https://algos.qiyuanlab.com/admin-api/app/assignments/page?pageNo=1&pageSize=10&assignmentId=&showName=&status=&resourceId=&image=&chipType=',
#             'https://algos.qiyuanlab.com/admin-api/app/metric/getSingleMetric?metric=cpu%2Cmemory%2Cnpu%2Cmlu%2CcardMemory%2Cutilization',
#             'https://algos.qiyuanlab.com/admin-api/app/metric/getSpecialMetric?cluster=&metric=allCard',
#             'https://algos.qiyuanlab.com/admin-api/app/metric/getMultiMetric?interval=1&from=2025-06-26%2000%3A00%3A00&to=2025-07-02%2023%3A59%3A59&cluster=&metric=mlu%2Ccpu%2Cnpu%2Cmemory%2CcardMemory',
#         ]
# for i in url_list:
#     res2 = requests.get(url = i,headers=headers)
#     if res2.json()['code'] == 0:
#         print('{}无异常'.format(i))
#     else:
#         print('{}接口不通'.format(i))
url = 'https://algos.qiyuanlab.com/admin-api/app/metric/getMultiMetric?interval=1&from=2025-06-26%2000%3A00%3A00&to=2025-07-02%2023%3A59%3A59&cluster=&metric=mlu%2Ccpu%2Cnpu%2Cmemory%2CcardMemory'
data = {
    'algorithmId':2,'pageNo':1,'pageSize':10
}
res3 = requests.get(url = url,headers=headers)
print(res3.json())