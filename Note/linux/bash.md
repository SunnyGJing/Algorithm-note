1. time 统计命令/程序运行时长
   ```bash
    # 终端显示
    >> time python xxx.py

    # 输出重定向
    >> { time python xxx.py; } 2>time.log

    # 输出重定向（追加写入）
    >> nohup bash -c "time python xxx.py" >> time.log 2>&1
   ```

2. 字符串和变量拼接
   ```bash
   # 注意：等号两边不能有空格
   file_name="xxx.txt"

   # 注意：必须用双引号，或者省掉双引号
   # 注意：可以去掉大括号，也可以把变量放在双引号外面
   python xxx.py --file "./file_dir/${file_name}"
   ```