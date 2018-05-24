The backend is made of django-restframework.
Environment:
Ubuntu16.04
python3.5
django1.11

and the requirements:
mysql5.7
mysqlclient==1.3.12
absl-py==0.1.11
adium-theme-ubuntu==0.3.4
astor==0.6.2
backports.weakref==1.0.post1
bleach==1.5.0
ecdsa==0.13
enum34==1.1.6
funcsigs==1.0.2
futures==3.2.0
gast==0.2.0
grpcio==1.10.0
html5lib==0.9999999
Markdown==2.6.11
mock==2.0.0
numpy==1.14.2
paramiko==1.16.0
pbr==3.1.1
Pillow==5.1.0
protobuf==3.5.2
pycrypto==2.6.1
pytz==2018.4
six==1.11.0
tensorboard==1.6.0
termcolor==1.1.0
unity-lens-photos==1.0
Werkzeug==0.14.1

I load data from csv file into mysql by use the under command:
    load data infile '/var/lib/mysql-files/test1.csv' 
    into table student character set gb2312
    fields terminated by ',' optionally enclosed by '"' escaped by '"' 
    lines terminated by '\r\n'; 
Beacause of the secure limit,I have to put the csv file into folder '/var/lib/mysql-files/'.





