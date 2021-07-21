#!/bin/sh
centroid[0]=$1
i=0
../start.sh
while true
do
   a=$((i+1))
   b=${centroid[$i]}
   /usr/local/hadoop/bin/hdfs dfs -mkdir -p /q6/input/
   cat /mapreduceproject/shot_logs.csv | /usr/local/hadoop/bin/hdfs dfs -put - /q6/input/
   /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
   -file ../q6/mapper.py -mapper "../q6/mapper.py $b" \
   -file ../q6/reducer.py -reducer ../q6/reducer.py \
   -input /q6/input/* -output /q6/output$a/
   centroid[$a]=$(/usr/local/hadoop/bin/hdfs dfs -cat /q6/output$a/part-00000)
   if [ ${centroid[$a]} == ${centroid[$i]} ] || [ "$i" -gt 50 ]
   then
      break
   else
      i=$((i+1))
      /usr/local/hadoop/bin/hdfs dfs -cat /q6/output$a/part-00000
      /usr/local/hadoop/bin/hdfs dfs -rm -r /q6/input/
      /usr/local/hadoop/bin/hdfs dfs -rm -r /q6/output$a/
   fi
done
/usr/local/hadoop/bin/hdfs dfs -cat /q6/output$a/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /q6/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q6/output$a/
../stop.sh