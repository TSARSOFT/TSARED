mkdir ~/TSARSOFT
mkdir ~/TSARSOFT/TSARED
cd ~/TSARSOFT/TSARED
rm ~/TSARSOFT/TSARED/* -r
wget 'https://github.com/TSARSOFT/TSARED/blob/master/TSARED-latest.zip?raw=true'
mv ~/TSARSOFT/TSARED/TSARED-latest.zip\?raw=true ~/TSARSOFT/TSARED/TSARED-latest.zip
unzip ./TSARED-latest.zip
echo 'python3 ~/TSARSOFT/TSARED/latest/TSARED.py' >> ~/TSARSOFT/TSARED/run.sh
chmod 777 ./run.sh
echo 'installation of TSARED complete! rus using command ~/TSARSOFT/TSARED/run.sh'
