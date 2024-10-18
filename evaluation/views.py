#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： views.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-10-09 10:45
    @Desc: 
================================================="""
import os
import shutil
import zipfile

from django.http import HttpResponse
from django.views import View


class DownloadZipView(View):
    def get(self, request, content_type, temp_dir_path, *args, **kwargs):
        # 指定要打包的目录
        directory_to_zip = f'temp/{content_type}/{temp_dir_path}'

        # 创建一个 Zip 文件
        zip_filename = f'archive-{content_type}-{temp_dir_path}.zip'
        zip_filepath = f'temp/{zip_filename}'

        with zipfile.ZipFile(zip_filepath, 'w') as zipf:
            for root, dirs, files in os.walk(directory_to_zip):
                for file in files:
                    file_path = os.path.join(root, file)
                    # 将文件添加到 ZIP 文件中
                    zipf.write(file_path, os.path.relpath(file_path, directory_to_zip))

        # 删除原始文件夹
        shutil.rmtree(directory_to_zip)

        # 创建 HTTP 响应
        with open(zip_filepath, 'rb') as zip_file:
            response = HttpResponse(zip_file.read(), content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename={zip_filename}'

        return response
