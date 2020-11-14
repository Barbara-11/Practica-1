ic=$(curl ipconfig.me)
ip=$(hostname -I)


nmap --script ftp-syst $ip >Practica7.txt
nmap --script http-jsonp-detection.nse >>Practica7.txt
nmap --script netbus-brute $ic >>Practica7.txt

base64 < Practica7.txt > Practica7_e.txt


