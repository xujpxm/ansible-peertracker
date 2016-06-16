# 简介
这是一个用ansible写的自动化搭建P2P传输网络的脚本。Tracker采用谷歌10年开源出来的peertracker，p2p种子的生成和传输采用transmission。


### 安装


**安装peertracker:**

`ansible-playbook install_peertracker.yml`

默认创建的数据库:peertracker,用户名:peertracker,密码:yais6Yab

脚本执行完成后,通过网页创建数据库,详见下面peertracker的安装.

**安装transmission:**

`ansible-playbook install_transmission.yml`

默认rpc_username和password: **transmission/transmission** 

可自行修改/etc/transmission-daemon/settings.json文件自定义.


**创建下载目录**

`ansible-playbook download_dir.yml`

默认下载路径是:/data/transmission-daemon/downloads可自行更改

## Peertracker
P   eerTracker是一个简单、高效、迅速的BitTorent Tracker。  
安装要求：  
1. HTTP Web Server.Apache，nginx,lighttpd等只要支持php均可。  
2. PHP5+ 推荐php5.3以上版本  
3. Database.支持MySQL、SQLite3、PostgreSQL8.0和txtSQL 
脚本里采用的web server是apache2,数据库使用mysql。   


### Important Links:
---
Development Website: <http://code.google.com/p/peertracker/>  
Issue Tracker: <http://code.google.com/p/peertracker/issues/list>  
Source Code Repository: <http://peertracker.googlecode.com/svn/trunk/>  
github respository: <https://github.com/JonnyJD/peertrackeris>  

### **peertracker的安装**
脚本a安装环境：ubuntu  
1. 确认代码拷贝到网站根目录之后，浏览器访问: <http://serverip/peertracker/help.php    
2. 编辑配置文件tracker.mysql.php，这里已提前编辑好，主要更改了数据库的db_user、db_pass和db_name，默认数据库明和user是peertracker，密码：yais6Yab，也可自行修改templates里的文件。
  
3. 通过help页面提供的Utilities，安装Tracker Database。安装成功后可看到，数据库结构很简单，只有两个表：pt_peers和pt_tasks,分别记录peer和任务的信息。
  
4. 数据库创建成功之后实际已可以使用，tracker的url即为：<http://serverip/peertracker/mysql/announce.php> 如果是外网使用，可以把对应的announce和scrape.php文件移置网站的顶级目录，那么生成的tracker url即为:<http://serverip/announce.php>
   
5. help.php的页面示例：


![help.php](https://github.com/xujpxm/picture/blob/master/peertracker_help.png?raw=true>)  

也可以查看peer的状态：

<http://serverip/peertracker/mysql/scrape.php?stats>


 
## **Transmission**
  Transmission是一个强大的BitTorrent开源客户端，实现了BT协议中描述的大多数功能。目前，在它的官方网站上提供了多个版本可以下载，包括：Mac、GTK+、QT版本，还有Daemon版本。  
  Transmission支持DHT、Magnet Link、uTP以及PEX等特性。尤其是支持Magnet Link磁力链接下载十分重要，因为目前网上很多资源都是采用这种方式来分享的，而不是传统的.torrent文件，例如TPB、BTDigg。  




### **transmission的安装/配置**  
**安装**    
安装很简单，直接apt-get安装即可，运行transmission的role,脚本会自动安装。  
安装过程中会顺带把transmission-cli也安装上，安装完毕后系统会多出如下一些命令行工具。 
* transmission-cli： 独立的命令行客户端。  
* transmission-create： 用来建立.torrent种子文件的命令行工具。  
* transmission-daemon： 后台守护程序。  
* transmission-edit： 用来修改.torrent种子文件的announce URL。  
* transmission-remote： 控制daemon的程序。  
* transmission-show：查看.torrent文件的信息。  
**配置**  
settings.json是主要的配置文件，设置daemon的各项参数，包括RPC的用户名密码配置。它实际上是一个符号链接，指向的原始文件是/etc/transmission-daemon/settings.json。  
脚本里提供了一个模板文件，主要修改了下载路径、rpc认证和白名单、默认的rpc认证用户名/密码为：transmission/transmission  
RPC的几个配置参数：  
* rpc-authentication-required: rpc认证，建议开启  
* rpc-bind-address: String (default = “0.0.0.0”) Where to listen for RPC connections  
* rpc-enabled: Boolean (default = true)  
* rpc-password: String  
* rpc-port: 默认端口9091Number (default = 9091)  
* rpc-url: String (default = /transmission/. Added in v2.2)  
* rpc-username: String  
* rpc-whitelist: 设置白名单 String (Comma-delimited list of IP addresses. Wildcards allowed using ‘‘. Example: “127.0.0.,192.168..“, Default: “127.0.0.1” )  
* rpc-whitelist-enabled: Boolean (default = true)  

### **transmission使用web界面控制**
浏览器中访问：<http://serverip:9091/transmission/web/>  
即可在浏览器中添加种子文件，进行p2p网络传输。  
种子文件的生成可以使用transmission自带的transmission-remote命令，例如：  
`transmission-create -c "Standard Template " -t http://192.168.1.1/announce.php -o Template.torrent StandardTemplate`
 
 
下图是我自己测试的transmission实时速度，限速100M，起了五个peer基本打满带宽：  


![speed](https://github.com/xujpxm/picture/blob/master/peer.png?raw=true)  

**需要注意的是transmission的下载路径是/data/transmission-daemon/downloads,注意文件目录是否存在和权限,可以用download_dir.yml脚本创建**

