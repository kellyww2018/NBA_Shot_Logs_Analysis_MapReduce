import os
import sys, socket

def writeHadoopConfigFile(name,xml):
    f = open("/usr/local/hadoop/etc/hadoop/" + name,"w")
    f.write(xml)
    f.close()

mf = open("manager","r")
sf = open("workers","r")
mip = mf.read().strip()
sip = sf.read().replace("-","")
mf.close()
sf.close()

print("Config Hadoop 2.9.2 YARN...")
mapredSiteXml = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
"""
writeHadoopConfigFile("mapred-site.xml",mapredSiteXml)

yarnSiteXml = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>%(mip)s</value>
    </property>

    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>

    <property>
         <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
         <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
  <property>
    <name>yarn.resourcemanager.address</name>
    <value>%(mip)s:8032</value>
  </property>
  <property>
     <name>yarn.resourcemanager.scheduler.address</name>
     <value>%(mip)s:8030</value>
  </property>
  <property>
     <name>yarn.resourcemanager.resource-tracker.address</name>
     <value>%(mip)s:8031</value>
  </property>
  <property>
     <name>yarn.resourcemanager.admin.address</name>
     <value>0.0.0.0:8033</value>
   </property>
   <property>
      <name>yarn.resourcemanager.webapp.address</name>
      <value>0.0.0.0:8088</value>
   </property>
   <property>
      <name>mapreduce.jobhistory.address</name>
      <value>%(mip)s:10020</value>
   </property>
   <property>
      <name>mapreduce.jobhistory.webapp.address</name>
      <value>0.0.0.0:19888</value>
   </property>
</configuration>
""" % dict(mip=mip)
writeHadoopConfigFile("yarn-site.xml",yarnSiteXml)

manager = mip
writeHadoopConfigFile("manager",manager)
workers = sip
writeHadoopConfigFile("workers",workers)
