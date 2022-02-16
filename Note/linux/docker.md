1. 查看docker镜像列表
   ```bash
    > docker images

    REPOSITORY          TAG     IMAGE ID       CREATED       SIZE
    hotspot_predone      v3    5dfc7c125e94   3 days ago    4.95GB
   ```

2. 查看docker容器列表
    ```bash
    > docker ps

    CONTAINER ID    IMAGE   COMMAND CREATED STATUS  PORTS    NAMES
    4cf33b17977b    dayin:v1    "/bin/bash" 2 days ago  Up 2 days   0.0.0.0:9030-9  031->9030-9031/tcp, :::9030-9031->9030-9031/tcp hotspot_aipre
    ```

3. 新建镜像
   - 基于Dockerfile和requirement.txt创建
        ```bash
        > docker build -t hotspot_test:v0.1 .

        """
        -t 标记来添加 tag
        “.” 是 Dockerfile 所在的路径（当前目录）
        """
        ```
    - 从容器创建一个新的镜像
        ```bash
        > docker commit f5352b9d7446 hotspot:v2

        # f5352b9d7446是容器ID, hotpot是REPOSITORY, v2是TAG)
        ```

4. 运行容器
   - 基于镜像新建一个容器并启动
        ```bash
        > docker run -itd --name hotspot --restart always --privileged=true -v /mnt/fileinfo:/mnt/fileinfo -p 9028:9030 hotspot:v1 /usr/sbin/init

        """
        -i	打开STDIN，用于控制台交互，通常与 -t 同时使用；
        -t	为容器重新分配一个伪输入终端，支持终端登录，通常与 -i 同时使用；
        -d	后台运行容器，并返回容器ID；
        --name 指定容器名字；
        --start 指定Docker重启时，容器是否自动启动：
        --privileged 指定容器是否为特权容器，特权容器拥有所有的capabilities；
        -v 给容器挂载存储卷，挂载到容器的某个目录(:之前是宿主机文件夹，之后是容器需共享的文件夹)；
        -p 指定容器暴露的端口（:之前对应外部端口，也就是本机的端口，之后对应docker内部的端口），
           注：先查看端口是否被占用，lsof -i:9028
        """
        ```

   - 启动终止状态(exited)下的docker容器
        ```bash
        # 开启一个可交互的终端
        > docker exec -it 4c /bin/bash

        # 运行一个脚本
        > docker exec -it hotspot sh /home/code/test.sh

        # 运行一个.py程序
        > docker exec -it hotspot python /home/code/test.py
        ```

5. docker容器与主机之间传送文件
    ```bash
    > docker cp
    ```

6. 删除docker镜像
   ```bash
    > docker rmi 366164d3d5e1
   ```

7. 删除docker容器
   ```bash
   > docker rm 2dad15117153
   ```

8.  打包镜像为 tar 包
    ```bash
    > docker save -o hotspot_predone.tar hotspot_predone:v2
    ```

9. linux资源限制配置文件
    ```bash
    > vim /etc/security/limits.conf
    ```

10. 配置系统内核参数
    ```bash
    > systcl -p
    # 从指定的文件加载系统参数，如不指定即从/etc/sysctl.conf中加载
    ```

11. sshd配置文件
    ```bash
    > vi /etc/ssh/sshd_config
    ```
    
12. sshd(secure shell)服务
    ```bash
    > service sshd restart
    ```


Reference:
- [几张图帮你理解 docker 基本原理及快速入门](http://www.hainiubl.com/topics/13)
- [用docker建立server自启动服务的几种方法(包含Dockerfile和requirements.txt制作方法)](https://blog.csdn.net/weixin_48185819/article/details/119447546)