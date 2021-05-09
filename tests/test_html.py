import requests
from bs4 import BeautifulSoup
url1 = "https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/user_info?userid=A123456789"
url2="https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/company_info?companyid=1"
response =requests.get (url1)
soup=BeautifulSoup(response.text, "html.parser")
print("url1",soup.prettify())
response =requests.get (url2)
soup=BeautifulSoup(response.text, "html.parser")
print("url2",soup.prettify())
status1=requests.head(url1)
status2=requests.head(url2)

class TestHtml1:

    def test_case2(self):
        assert status1.status_code==200
class TestHtml2:

    def test_case3(self):
        assert status2.status_code==403