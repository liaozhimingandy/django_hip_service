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