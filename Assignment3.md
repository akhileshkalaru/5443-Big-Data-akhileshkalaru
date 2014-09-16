# Assignment3 #

![Alt text](http://http://162.243.135.49/Assignment3.jpg "Optional title")


1Q: How do you add nodes to your Hadoop cluster?
Multi-Node Cluster Setup
Before merging both single node servers into a multi node cluster we need to make sure that both the node pings each other( they need to be connected on the same network / hub or both the machines can speak to each other). Once we are done with this process, we will be moving to the next step in selecting the master node and slave node
we need to add them in ‘/etc/hosts’ file on each machine as follows.
sudo vi /etc/hosts
It will display as
172.16.17.68     Haadoopmaster
172.16.17.61     hadoopnode
Note: The addition of more slaves should be updated here in each machine using unique names for slaves 
Enabling SSH
hduser on master(Hadoopmaster) machine need to able to connect to its own master (Hadoopmaster) account user and also need to connect hduser  to the slave (hadoopnode) machine via password-less SSH login.
hduser@Hadoopmaster:~$ ssh-copy-id -i ~/.ssh/id_rsa.pub hduser@hadoonode
when you run the given command on both master and slave, then we configured it correctly.
ssh Hadoopmaster
ssh hadoopnode
CONFIGURING MULTI NODE HADOOP CLUSTER:
MASTER:
In master (Hadoopmaster) machine we need to configure masters file accordingly as shown in the image and add the master (Hadoopmaster) node name.
vi masters
Hadoopmaster
SLAVE:
Lists the hosts, one per line, where the Hadoop slave daemons (DataNodes and TaskTrackers) will be running as shown:
Hadoomaster
hadoopnode


core-site.xml:
We are changing the host name from ‘localhost’ to Hadoopmaster, which specifies the NameNode (the HDFS master) host and port.
vi core-site.xml
hdfs-site.xml:
We are changing the replication factor to “2”, The default value of dfs.replication is 3. However, we have only two nodes available, so we set dfs.replication to 2.
vi hdfs-site.xml
mapred-site.xml:
We are changing the host name from ‘localhost’ to Hadoopmaster, which specifies the JobTracker (MapReduce master) host and port
vi mapred-site.xml
Formatting and Starting/Stopping the HDFS filesystem via the NameNode:
The first step to starting up your multi–node Hadoop cluster is formatting the Hadoop filesystem which is implemented on top of the local filesystem of your cluster. To format the filesystem (which simply initializes the directory specified by the dfs.name.dir variable), run the given command.
hadoop namenode –format
Starting the multi-node cluster:
Starting the cluster is performed in two steps.
We begin by starting the HDFS daemons first, the NameNode daemon is started on Hadoopmaster and DataNode daemons are started on all nodes(slaves).
Then we will start the MapReduce daemons, the JobTracker is started on Hadoomaster and TaskTracker daemons are started on all nodes (slaves)
To start HDFS daemons:
start-dfs.sh
This will get NameNode up and DataNodes up listed in conf/slaves.
By running jps command, we will see list of java processes running on master and slaves:
To start  Map Red daemons:
start-mapred.sh
This will bring up the MapReduce cluster with the JobTracker running on the machine you ran the previous command on, and TaskTrackers on the machines listed in the conf/slaves file.
By running jps command, we will see list of java processes including JobTracker and TaskTracker running on master and slaves:. To stop Map Red daemons:
stop-mapred.sh
To stop HDFS daemons:
stop-dfs.sh
 Running a Map-reduce Job:
Use a much larger volume of data as inputs as we are running in a cluster.
hadoop jar hadoop *examples*. jar wordcount  /user/hduser/demo  /user/hduser/demo-output
we can observe namenode,mapreduce,tasktracker process on the webinterface by following given url’s
•	http://Hadoopmaster:50070/ – web UI of the NameNode daemon
•	http://Hadoopmaster:50030/ – web UI of the JobTracker daemon
•	http://Hadoopmaster:50060/ – web UI of the TaskTracker daemon
*Hadoopmaster can be replaced with the machine ip
By this we are done in setting up a multi-node hadoop cluster, hope this step by step guide helps you to setup same environment at your place.

2Q: Can everyone in class add the remaining members of the class to thier cluster? 
Yes, it can be done by the above mentioned process
3Q: Can everyone simultaneously run thier own Hadoop cluster, AND be a slave (worker) in another Hadoop cluster? 
Yes, Client machine is to load data into the cluster, submit Map Reduce jobs describing how that data should be processed, and then retrieve or view the results of the job when its finished.  In smaller clusters (~40 nodes) you may have a single physical server playing multiple roles, such as both Job Tracker and Name Node.  With medium to large clusters you will often have each role operating on a single server machine.
