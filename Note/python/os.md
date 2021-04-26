### 删除文件/文件夹
1. 删除文件
   - os.remove(path)  
     ```
     删除路径为path的文件
     如果path是文件夹，将抛出OSError
     ```
2. 删除空文件夹
   - os.rmdir(path)  
     ```
     删除路径为path的空文件夹
     如果文件夹非空，则抛出OSError
     ```
   - os.removedirs(path)  
     ```
     递归调用os.rmdir删除路径为path的空目录
     如果目录下的子文件夹非空，则抛出OSError
     ```
3. 删除非空文件夹（高级权限）
   - shutil.rmtree(path)
     ```
     删除路径为path的非空文件夹
     ```

### 获取路径/文件名/文件后缀名
1. 获取路径
   - os.getcwd()
     ```
     返回当前工作目录
     ```
   - os.path.abspath(path)
     ```
     返回它的绝对路径
     ```
   - os.path.dirname(path)
     ```
     返回它的父文件夹的路径
     ```
   - os.path.split(path)[0]
     ```
     返回它的父文件夹的路径
     ```
   - os.path.splitext(path)[0]
     ```
     返回它的路径（去除文件后缀名）
     ```
2. 获取子文件/子文件夹
   - os.listdir(path)
      ```
      返回它的子文件/子文件夹名称的列表
      （返回格式为list）
      （注意：只返回第一级子文件/子文件夹）
      ```
3. 获取文件名
   - os.path.basename(path)
     ```
     返回它的文件名（含后缀）
     ```
   - os.path.split(path)[-1]
     ```
     返回它的文件名（含后缀）
     ```
   - os.path.splitext(os.path.basename(path))[0]
     ```
     返回它的文件名（去除后缀）
     ```
4. 获取文件后缀名
   - os.path.splitext(path)[-1]
     ```
     返回它的后缀名
     ```

### 创建/重命名文件/文件夹  
1. 创建
   - os.mkdir(path)
     ```
     新建路径为path的文件夹
     ```
2. 重命名
   - os.rename(name, new_name)
     ```
     将路径为name的文件夹/文件重命名为new_name
     ```

### 文件/文件夹的判断
1. 是否存在
   - os.path.exists(path)
     ```
      判断是否存在路径为path的文件/文件夹
     ```

