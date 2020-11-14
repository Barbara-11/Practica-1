ic=$(curl ipconfig.me)
ip=$(hostname -I)


nmap --script ftp-syst $ip >Actividad7.txt
nmap --script http-jsonp-detection.nse >>Actividad7.txt
nmap --script netbus-brute $ic >>Actividad7.txt

base64 < Actividad7.txt > Actividad7-e.txt

