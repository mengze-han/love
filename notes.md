## python

anaconda

```
conda create -n graph python=3.7
conda activate graph
conda deactivate
source activate name
```

**Anaconda导出与安装依赖包**

查看所有环境

```
conda env list
```

激活环境

```
activate env_name
```

导出该环境依赖包

```
conda env export > environment.yml
```

安装环境依赖包，需要输入yml文件的路径

```
conda env create -f environment.yml
```

**pip 导出与安装依赖包**

导出依赖包

```shell
pip freeze > requirements.txt
```

安装依赖包

```shell
pip install -r requirements.txt
```

pip 使用代理

```shell
pip3 --proxy ip:port  install packages
pip install -r requirements.txt  --proxy="ip:port"
```

## neo4j

#### 笔记

![image-20200520090330150](README.assets/image-20200520090330150.png)

```sql
create (N1:ToyNode {name: 'Tom'}) - [:ToyRelation {relationship: 'knows'}] -> (N2:ToyNode {name:
'Harry'}),
(N2) - [:ToyRelation {relationship: 'co-worker'}] -> (N3:ToyNode {name: 'Julian', job: 'plumber'}),
(N2) - [:ToyRelation {relationship: 'wife'}] -> (N4:ToyNode {name: 'Michele', job: 'accountant'}),
(N1) - [:ToyRelation {relationship: 'wife'}] -> (N5:ToyNode {name: 'Josephine', job: 'manager'}),
(N4) - [:ToyRelation {relationship: 'friend'}] -> (N5)
```

#### Getting Started With **Neo4j**

**View the resulting graph**
match (n:ToyNode)-[r]-(m) return n, r, m

**Delete all nodes and edges**
match (n)-[r]-() delete n, r

**Delete all nodes which have no edges**
match (n) delete n

**Delete all edges**
match (n)-[r]-() delete r

**Delete only ToyNode nodes which have no edges**
match (n:ToyNode) delete n

**Delete only ToyRelation edges**
match (n)-[r:ToyRelation]-() delete r

**Selecting an existing single ToyNode node**
match (n:ToyNode {name:'Julian'}) return n

**Adding to and Modifying a Graph**

**Adding a Node Correctly**
match (n:ToyNode {name:'Julian'})
merge (n)-[:ToyRelation {relationship: 'fiancee'}]->(m:ToyNode {name:'Joyce', job:'store clerk'})
**Adding a Node Incorrectly**
create (n:ToyNode {name:'Julian'})-[:ToyRelation {relationship: 'fiancee'}]->(m:ToyNode {name:'Joyce',
job:'store clerk'})
**//Correct your mistake by deleting the bad nodes and edge**
match (n:ToyNode {name:'Joyce'})-[r]-(m) delete n, r, m
**Modify a Node’s Information**
match (n:ToyNode) where n.name = 'Harry' set n.job = 'drummer'
match (n:ToyNode) where n.name = 'Harry' set n.job = n.job + ['lead guitarist']

![image-20200520091752975](README.assets/image-20200520091752975.png)

![image-20200520091743323](README.assets/image-20200520091743323.png)



[csv link](https://d3c33hcgiwev3.cloudfront.net/_84ec1bfd4d29ad5649fcbec4165c341b_neo4j_module_datasets.zip?Expires=1590105600&Signature=h7DMf2Te30ZtXeFwpW2idKVZR2OCtjg5k5XSZHxo1NBTO8GjGV2lmWEAgxaXrHG4EynDcheaTgG6VFv-2t87ueMiyLkeu7e17r4RvuYiKrsjJE1afBX9~qe8~lnjkK9EY0WNjaqQIDau7cwvnt-nQ8itnSoBz5vWa8wMIDEI0HA_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

![image-20200520092149899](README.assets/image-20200520092149899.png)

#### Cypher Scripts for Importing Data Into Neo4j

LOAD CSV WITH HEADERS FROM "file:///terrorist_data_subset.csv" AS row
MERGE (c:Country {Name:row.Country})
MERGE (a:Actor {Name: row.ActorName, Aliases: row.Aliases, Type: row.ActorType})
MERGE (o:Organization {Name: row.AffiliationTo})
MERGE (a)-[:AFFILIATED_TO {Start: row.AffiliationStartDate, End: row.AffiliationEndDate}]->(o)
MERGE(c)<-[:IS_FROM]-(a);

#### Basic Graph Operations with CYPHER

**Counting the number of nodes**
match (n:MyNode)
return count(n)

**//Counting the number of edges**
match (n:MyNode)-[r]->()
return count(r)

**Finding leaf nodes:**
match (n:MyNode)-[r:TO]->(m)
where not ((m)-->())
return m
**//Finding root nodes:**
match (m)-[r:TO]->(n:MyNode)
where not (()-->(m))
return m
**//Finding triangles:**
match (a)-[:TO]->(b)-[:TO]->(c)-[:TO]->(a)
return distinct a, b, c
**//Finding 2nd neighbors of D:**
match (a)-[:TO*..2]-(b)
where a.Name='D'

return distinct a, b

**//Finding the types of a node:**
match (n)
where n.Name = 'Afghanistan'
return labels(n)

**//Finding the label of an edge:**
match (n {Name: 'Afghanistan'})<-[r]-()
return distinct type(r)

**//Finding all properties of a node:**
match (n:Actor)
return * limit 20

**//Finding loops:**
match (n)-[r]->(n)
return n, r limit 10

**//Finding multigraphs:**
match (n)-[r1]->(m), (n)-[r2]-(m)
where r1 <> r2
return n, r1, r2, m limit 10

**//Finding the induced subgraph given a set of nodes:**
match (n)-[r:TO]-(m)
where n.Name in ['A', 'B', 'C', 'D', 'E'] and m.Name in ['A', 'B', 'C', 'D', 'E']

return n, r, m

**Path Analytics with CYPHER**
**//Viewing the graph**
match (n:MyNode)-[r]->(m)
return n, r, m
**//Finding paths between specific nodes:**
match p=(a)-[:TO*]-(c)
where a.Name='H' and c.Name='P'
return p limit 1
*Your results might not be the same as the video hands-on demo. If not, try the following query and it
should return the shortest path between nodes H and P:
match p=(a)-[:TO*]-(c) where a.Name='H' and c.Name='P' return p order by length(p) asc limit 1
**//Finding the length between specific nodes:**
match p=(a)-[:TO*]-(c)
where a.Name='H' and c.Name='P'
return length(p) limit 1
**//Finding a shortest path between specific nodes:**
match p=shortestPath((a)-[:TO*]-(c))
where a.Name='A' and c.Name='P'
return p, length(p) limit 1
**//All Shortest Paths:**
MATCH p = allShortestPaths(source-[r:TO*]-destination)
WHERE source.Name='A' AND destination.Name = 'P'
RETURN EXTRACT(n IN NODES(p)| n.Name) AS Paths
**//All Shortest Paths with Path Conditions:**
MATCH p = allShortestPaths(source-[r:TO*]->destination)
WHERE source.Name='A' AND destination.Name = 'P' AND LENGTH(NODES(p)) > 5
RETURN EXTRACT(n IN NODES(p)| n.Name) AS Paths,length(p)
**//Diameter of the graph:**
match (n:MyNode), (m:MyNode)
where n <> m
with n, m
match p=shortestPath((n)-[*]->(m))
return n.Name, m.Name, length(p)
order by length(p) desc limit 1
**//Extracting and computing with node and properties:**
match p=(a)-[:TO*]-(c)
where a.Name='H' and c.Name='P'
return extract(n in nodes(p)|n.Name) as Nodes, length(p) as pathLength,
reduce(s=0, e in relationships(p)| s + toInt(e.dist)) as pathDist limit 1
//Dijkstra's algorithm for a specific target node:
MATCH (from: MyNode {Name:'A'}), (to: MyNode {Name:'P'}),
path = shortestPath((from)-[:TO*]->(to))
WITH REDUCE(dist = 0, rel in rels(path) | dist + toInt(rel.dist)) AS distance, path
RETURN path, distance
**//Dijkstra's algorithm SSSP:**
MATCH (from: MyNode {Name:'A'}), (to: MyNode),
path = shortestPath((from)-[:TO*]->(to))
WITH REDUCE(dist = 0, rel in rels(path) | dist + toInt(rel.dist)) AS distance, path, from, to
RETURN from, to, path, distance order by distance desc
**//Graph not containing a selected node:**
match (n)-[r:TO]->(m)
where n.Name <> 'D' and m.Name <> 'D'
return n, r, m
**//Shortest path over a Graph not containing a selected node:**
match p=shortestPath((a {Name: 'A'})-[:TO*]-(b {Name: 'P'}))
where not('D' in (extract(n in nodes(p)|n.Name)))
return p, length(p)
**//Graph not containing the immediate neighborhood of a specified node:**
match (d {Name:'D'})-[:TO]-(b)
with collect(distinct b.Name) as neighbors
match (n)-[r:TO]->(m)
where
not (n.Name in (neighbors+'D'))
and
not (m.Name in (neighbors+'D'))
return n, r, m
;
match (d {Name:'D'})-[:TO]-(b)-[:TO]->(leaf)
where not((leaf)-->())
return (leaf)
;
match (d {Name:'D'})-[:TO]-(b)<-[:TO]-(root)
where not((root)<--())
return (root)
**//Graph not containing a selected neighborhood:**
match (a {Name: 'F'})-[:TO*..2]-(b)
with collect(distinct b.Name) as MyList
match (n)-[r:TO]->(m)
where not(n.Name in MyList) and not (m.Name in MyList)
return distinct n, r, m

### 备份与还原

来自[官方文档](https://neo4j.com/docs/operations-manual/3.5/tools/dump-load/)

社区版的备份要求必须停机，姑且称之为冷备份吧。

#### 备份

```shell
neo4j-admin dump --database=<database> --to=<destination-path>
```

###### 举个例子：

```shell
bin/neo4j-admin dump --database=graph.db --to=/backups/2016-10-02.dump
```

然后 ls /backups/graph.db就能看见刚才备份的数据库了



#### 还原

```shell
neo4j-admin load --from=<archive-path> --database=<database> [--force]
```

 例子：

```
bin/neo4j stop
bin/neo4j-admin load --from=/backups/graph.db/2016-10-02.dump --database=graph.db --force
```

Load the backed-up database contained in the file `/backups/graph.db/2016-10-02.dump` into database `graph.db`. Since we have a database running, we first have to shut it down. When we use the `--force` option, any existing database gets overwritten.

## Linux

### 查看文件夹大小

```shell
du -sch ./*
```

-s, --summarize 只顯示總計

-c, --total 增列一行 "總計"

-h, --human-readable 以 K, M, G 為計量單位

### docker 

#### docker 常用指令

1、docker run ：创建一个新的容器并运行一个命令 

2、docker start :启动一个或多个已经被停止的容器 

3、docker stop :停止一个运行中的容器 

4、docker restart :重启容器 

5、docker rm ：删除一个或多少容器

6、docker create ：创建一个新的容器但不启动它

7、docker exec ：在运行的容器中执行命令

8、docker ps : 列出容器 

9、docker commit :从容器创建一个新的镜像。

10、docker pull : 从镜像仓库中拉取或者更新指定镜像 

11、docker push : 将本地的镜像上传到镜像仓库,要先登陆到镜像仓库 

12、docker search : 从Docker Hub查找镜像 

13、docker images : 列出本地镜像。

 14、docker images : 列出本地镜像。 

15、docker info : 显示 Docker 系统信息，包括镜像和容器数。 

16、docker version :显示 Docker 版本信息。

### ssh代理

正向代理

```shell 
ssh -FCNL localport:user@remote ip:remote port  user@jumper ip
```

反向代理

```shell
ssh -FCNR localport:user@remote ip:remote port  user@jumper ip
```

```apacheconf
GatewayPorts yes
```

socket 代理

```bash
ssh -D localhost:1080  HostB
```

### 深度学习

#### 激活函数

##### sigmoid

```python
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5., 5., 0.1)
y_sig = sigmoid(x)

plt.show()

plt.plot(x, y_sig, 'b', label='sigmoid')
plt.grid()
plt.title("Sigmoid Activation Function")
plt.text(6, 0.8, r'$\sigma(x)=\frac{1}{1+e^{-x}}$', fontsize=15)
plt.legend(loc='lower right');
```





##### 笔记

Ubuntu系统备份

ssh、ftp，exfat的支持

监控（iotop、htop、ctop）

docker docker-compose



命令 一键处理脚本

### 保存代码

### ssh代理

正向代理

```shell 
ssh -FCNL localport:user@remote ip:remote port  user@jumper ip
```

反向代理

```shell
ssh -FCNR localport:user@remote ip:remote port  user@jumper ip
```

```apacheconf
GatewayPorts yes
```

socket 代理

```bash
ssh -D localhost:1080  HostB
```





现在很多ssh client都可以设置端口转发了
