import reqests
import re


def run(self, ip):
    page = requests.get('http://' + ip + '/getflag').text
    return re.findall(r'[A-Z0-9]{31}=', page)
