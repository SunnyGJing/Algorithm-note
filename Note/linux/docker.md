1. 查看docker环境列表
    ```bash
    > docker ps

    CONTAINER ID    IMAGE   COMMAND CREATED STATUS  PORTS    NAMES
    4cf33b17977b    dayin:v1    "/bin/bash" 2 days ago  Up 2 days   0.0.0.0:9030-9  031->9030-9031/tcp, :::9030-9031->9030-9031/tcp hotspot_aipre
    ```

2. 进入docker环境
    ```bash
    > docker exec -it 4c /bin/bash
    ```

docker cp
docker ps -a
docker rm 2dad15117153
docker run -itd --name hotspot --restart always --privileged=true -v /mnt/fileinfo:/mnt/fileinfo -p 9028:9030 hotspot:v1 /usr/sbin/init
ll -h
free -h

docker images
docker rmi 366164d3d5e1
docker commit f5352b9d7446 hotspot_predone:v2(hotpot是REPOSITORY, v2是TAG)
docker save -o hotspot_predone.tar hotspot_predone:v2(打包为tar)

rdz
rzs
rz

docker exec -it hotspot sh /home/code/test.sh
docker exec -it hotspot python /home/code/test.py
curl http://localhost:9030/second_hotword_modify
curl -P POST http://localhost:9030/second_hotword_modify
vi /etc/ssh/sshd_config
service sshd restart
adduser
adduser es
su - es
vim /etc/security/limits.conf
tar -xzf elasticsearch-7.8.0.tar.gz
systcl -p
sysctl -p
