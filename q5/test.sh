#!/bin/sh
../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /q5/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q5/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q5/output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /q5/input/
cat /mapreduceproject/shot_logs.csv | /usr/local/hadoop/bin/hdfs dfs -put - /q5/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../q5/mapper1.py -mapper ../q5/mapper1.py \
-file ../q5/reducer1.py -reducer ../q5/reducer1.py \
-input /q5/input/* -output /q5/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../q5/mapper2.py -mapper ../q5/mapper2.py \
-file ../q5/reducer2.py -reducer ../q5/reducer2.py \
-input /q5/output/part-00000 -output /q5/output2/


/usr/local/hadoop/bin/hdfs dfs -cat /q5/output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /q5/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q5/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q5/output2/
../stop.sh
