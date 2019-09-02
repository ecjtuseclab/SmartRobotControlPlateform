# SmartRobotControlPlateform
SmartRobotControlPlateform——智能机器人控制平台

说在前面<br>
喜欢我们的项目请Fork、Star、Watching支持我们。<br>
如果有宝贵的意见，请在Issue中回复或者加QQ群：498487801，你们宝贵的意见是我们完善的动力。<br>

开发人员：[康文洋](https://github.com/Little-kwy?tab=repositories)、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳<br>
### 作者康文洋正在找工作(应届生)，如果您对该项目感兴趣，请联系我：1981664245@qq.com

# 智能机器人控制平台为基于4G网络的复杂环境特种作业智能机器人安全远控系统的关键部分
基于4G网络的复杂环境特种作业智能机器人安全远控系统是在已经完成的安全态势感知工控系统基础上进
一步研发，主要包括远程作业智能机器人端、机器视觉端、数据中心端、视频流媒体服务器端、特种作业Web管理端和
APP操控端，使用4G网络作为远程作业智能机器人端与数据中心端的主要通信方式，远程作业智能机器人端接受来自特
种作业Web管理端和APP操控端的控制命令并上报实时监测数据。该项目提供远程操控作业机器人，在远程操控作业机
器人搭载Tenserflow深度学习框架做图像识别，搭载基于树莓派的Kali做内网物理渗透攻击。

* ssaicsp_app为树莓派web控制端：<br>
    使用Django搭建
     
* ssaicsp_socket为树莓派服务控制端：<br>
    AESHelper：加密帮助类<br>
    SM2：国密SM2公钥密码算法类<br>
    SM3：国密SM3散列算法类<br>
    KeyAgreementProcessProtocol：密钥协商处理类<br>
    Socket：socket类<br>
    Packet：控制数据封包<br>
    Sensor：传感器基类<br>
    led：LED类<br>
    dht11：dht11类<br>
    Redis：数据缓存类<br>
    MySQL：mysql数据库操作类<br>
    Logger：日志记录类<br>
    ...<br>
    

* 运行环境：<br>
    python3.5以上<br>
    python安装：pip3 isnatll django <br>

具体环境配置请移步我的博客园文章：https://www.cnblogs.com/little-kwy/p/10341403.html

# 版本说明：<br>
目前开源的版本为v0.01版，v0.02版正在努力开发中....<br>
基于v0.01版已经可以用于搭建个人的智能家居系统，实现了温湿度、光照、雨滴等传感器的实时监控，开灯等实时控制，数据加密传输/签名验证等安全机制。<br>
在v0.02版中加入了激光雷达，履带式坦克控制，机械臂控制，4G通讯，遥感控制，ROS机器人系统，Kali渗透测试平台等。<br>
未来打算实现分布式集群部署控制。<br>
该框架仅用于学习交流探讨，切勿用于商业用途！！！

QQ群扫码加入：<br>
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/498487801.png)

演示Demo界面如下：<br>
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/0.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/14.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/15.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/16.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/17.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/18.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/1.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/2.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/3.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/4.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/5.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/6.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/7.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/8.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/9.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/10.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/11.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/12.png)
![image](https://raw.githubusercontent.com/ecjtuseclab/SmartRobotControlPlateform/master/13.png)




