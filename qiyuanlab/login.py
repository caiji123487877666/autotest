import requests


class Login:
    access_token = None

    def get_token(self):
        url = 'http://mlops-test.qiyuanlab.com/qiyuanlab-mlops/gateway/userLogin'
        payload = {
            'username': 'root',
            'password': '96e79218965eb72c92a549dd5a330112'}
        res = requests.request(method='GET', url=url, params=payload)
        self.access_token = res.json()['data']['Authorization']
        return self.access_token

    def file_upload(self):
        url = 'http://mlops-test.qiyuanlab.com/qiyuanlab-mlops/datasetList/uploadReadMeFile'
        headers = {'authorization': self.access_token,
                   'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryR7zgLFiAEF7ZTvb6'}
        res = requests.request(method='POST', url=url, headers=headers, )

    def create_dataset(self):
        pass

    def upload_readme(self):
        url = 'http://mlops-test.qiyuanlab.com/qiyuanlab-mlops/datasetList/uploadReadMeFile'
        headers = {'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJyb290IiwiaWF0IjoxNzQzMDQxNTg0LCJleHAiOjE3NDMwNzc1ODR9.d9xhOrBA2O2UaTYL8HC-bp1mqSVBqRFtqYRDZr836zQ',
                   'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryR7zgLFiAEF7ZTvb6'}
        file_path = '../README.md'
        with open(file_path, 'rb') as f:
            binary_data = f.read()
        res = requests.request(method='POST', url=url, files={'file': binary_data}, headers=headers)
        return res.json()


if __name__ == '__main__':
    lg = Login()
    print(lg.get_token())