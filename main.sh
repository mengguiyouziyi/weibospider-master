#/usr/bin/env bash

nips=`ifconfig | grep "eth1.\d\d\d" -P -A 1 | grep "inet addr" | perl -ne "s/.*addr:| Bcast:.*//g;print;"`
echo "Number of vitural ip: " `echo $nips | sed "s/ /\n/g" | wc -l`
for ip in $nips
do
	echo $ip
	python ./first_task_execution/home_first.py $ip
done
