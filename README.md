简介

这是一个用ansible写的自动化安装peertracker server的脚本.由于只在ubuntu14.04上测试过,所以推荐安装环境是ubuntu14.04.

web server用的apache2,数据库使用mysql,也可以用nginx postgresql SQLite替换,只需修改common/tasks目录下定义的task即可.

## Peertracker

PeerTracker is a  Simple, Efficient and Fast BitTorent Tracker.

https://github.com/JonnyJD/peertrackeris 

### 安装

需要环境已经安装好ansible,只需运行以下命令自动安装即可,中间如有失败,修正之后重复执行脚本即可:

ansible-playbook install_peertracker.yml


