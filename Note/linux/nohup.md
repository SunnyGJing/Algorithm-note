1. 追加写入日志 / 覆盖写入日志
   ```bash
    # 两个'>>'是追加写入日志
    >> nohup python xxx.py >> nohup.out

    # 一个'>'是覆盖写入日志
    >> nohup python xxx.py > nohup.out
   ```

2. nohup 和 & 的作用
   ```
   nohup：
   nohup 是 no hang up 的缩写，防止在退出当前用户/关闭终端后杀死进程

   &：
   后台运行
   ```

3. 获取nohup进程号
   ```bash
   echo $! > xxx.pid  # 打印进程号到xxx.pid文件
   ```

4. 杀死nohup进程
   ```bash
   #!/bin/sh
   kill -9 `xxx.pid`  # 杀死xxx.pid文件中的进程号
   ```