#/bin/bash
clear
python3 API.py > .respons.txt
cat .respons.txt |sed 's/\:[0-9][0-9]+0[1-2]:00//g' |sed 's/\[/ /g' |sed 's/\,/\n/g' |sed 's/\]/\n/g' |sed s/\'//g |sed s/\{//g |sed 's/destinasjon://g' |sed s/\}//g |sed 's/sanntid//g' |sed 's/:[^~]*T//g' |sed 's/ : //g' |sed -r '/^\s*$/d' |sed ':a;N;$!ba;s/\n/ /g' |sed 's/^.\{6\}//g' |sed 's/\linje:/\n/g' |sed 's/: / /g' |sed 's/   /\t/g' > .output.txt
echo 
echo Klokken er:
date +%R
echo 
echo Neste avganger fra ditt stopp er:
echo 
sleep 1
cat .output.txt
echo 
echo 
echo Data provided by entur.org under NLOD 
echo 
