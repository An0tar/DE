#!/bin/bash

get=$(awk '/"GET/ { count++ } END { print count }' access.log)
head=$(awk '/"HEAD/ { count++ } END { print count }' access.log)
post=$(awk '/"POST/ { count++ } END { print count }' access.log)
put=$(awk '/"PUT/ { count++ } END { print count }' access.log)
delete=$(awk '/"DELETE/ { count++ } END { print count }' access.log)
connect=$(awk '/"CONNECT/ { count++ } END { print count }' access.log)
options=$(awk '/"OPTIONS/ { count++ } END { print count }' access.log)
trace=$(awk '/"TRACE/ { count++ } END { print count }' access.log)
patch=$(awk '/"PATCH / { count++ } END { print count }' access.log)

arr=("$get GET" "$head HEAD" "$post POST" "$put PUT" "$delete DELETE" "$connect CONNECT" "$options OPTIONS" "$trace TRACE" "$patch PATCH")

echo "Отчет о логе веб-сервера" > report.txt
echo "====================" >> report.txt

unique_ips=$(echo | awk -F ' ' '{print $1}' access.log | sort | uniq | wc -l)

echo "Количество уникальный IP адресов :$unique_ips" >> report.txt
echo "Отчет запросов по методам:" >> report.txt

sum=0
for i in "${arr[@]}"; do
if [[ ${i} =~ [0-9] ]]; then
echo ${i} >> report.txt
new=$(echo ${i% *})
sum=$((sum + $new))
fi
done
echo "Общее количество запросов: $sum" >> report.txt



popular_url=$(echo | awk -F ' ' '{print $7}' access.log | sort | uniq -c | sort -rn | head -n1)  
echo "Самый популярный URL: $popular_url" >> report.txt

echo "Отчет сохранен в файл report.txt"
