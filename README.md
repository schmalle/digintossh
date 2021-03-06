# Digging in a month of SSH data ###

Date: December 2018
Author: Markus Schmall

When you operate a large honeypot network, besides the generation of IP reputation  lists, it is also a good idea to dig a little bit deeper in the data.
The following data was taken from DTAGs Honeypot network (https://dtag-dev-sec.github.io) and (https://www.sicherheitstacho.eu).

## Context ##

- 30 days of SSH data (collected by Cowrie, T-Pot)
- 76382827 sessions & alarms
- 400 SSH honeypots (cowrie, all T-Pot[https://dtag-dev-sev.github.io] based)
- data collected from 23th of October to 22th of November 2018
                                                                     
## Tools used ##

## First steps ##

Initially , when looking at looking at the distribution of all requests, we see roughly 2mio++ login attempts per day and about 10% successful login attempts over the time.


![Login distribution](https://gitlab.com/flakedev/digintossh/blob/master/logins.png "Grafana graphics")
