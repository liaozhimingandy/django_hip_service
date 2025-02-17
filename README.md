# django_hip_service

#### 参考链接

```
官方文档：https://pdm-project.org/2.12/
其它文档：https://blog.csdn.net/aichaoxy/article/details/134733841
```

### 依赖
```python
pdm export -o requirements.txt --without-hashes
```

### 数据备份还原
```python
# 备份
python manage.py dumpdata hipmessageservice > hipmessageservice/fixtures/samples.json
# 还原
python manage.py loaddata hipmessageservice/fixtures/samples.json

```

### 反向导出数据库到模型
```python
 python manage.py inspectdb  > cda\models.py
```

### 部署注意
```python
# config/entrypoint.sh 文件修改exec gunicorn django_hip_service.wsgi:application -c /app/config/gunicorn.py 修改成实际项目配置
# 当python版本变更时,比如3.13变成3.14,请在 复制构建产物 处记得变更为3.14
```

#### 参考链接

```
官方文档：https://pdm-project.org/2.12/
其它文档：https://blog.csdn.net/aichaoxy/article/details/134733841
```

### 首次安装依赖
```python
pdm install
```

### 依赖
```python
pdm export -o requirements.txt --without-hashes
```

#### 增加依赖库
```python
# 使用pdm add命令能为当前目录的项目添加依赖库，添加到默认环境, 如
eg: pdm add requests
```

#### 依赖库分组
pdm为依赖库的管理提供了分组能力，常见的组有dev（开发专属）、prod（生产专属）等等，也可以自定义创建组。
```python
# 添加pytest依赖，到dev环境，并加入分组test
pdm add pytest -dG test
# 添加到测试环境
pdm add pytest -d
```
