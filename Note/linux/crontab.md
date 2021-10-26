systemctl restart crond.service
crontab -e
crontab -l
grep cron /var/log/syslog


1. 启动定时脚本
    ```
    # 添加定时执行命令:
    # 每天凌晨6点运行一次 /home/xxx/yyy.sh
    # 注意使用【绝对路径】

    #用crontab -e打开文件，vim编辑方式去掉“#”：
    #0 6 * * * /home/xxx/yyy.sh
    ```