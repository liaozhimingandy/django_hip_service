#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： Utils.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-07-29 15:11
    @Desc: 
================================================="""


class Utils(object):
    @staticmethod
    def find_all_file(path_dir: str, search_str: str) -> None:
        import glob
        _count = 0
        for file_name in glob.glob(path_dir):
            with open(file=file_name, mode='r', encoding="utf-8") as fp:
                content = fp.read()
                if search_str in content:
                    print(f"{file_name}")
                    _count += 1
        print(f"{_count} files")


if __name__ == "__main__":
    utils = Utils()
    # 交互服务
    # utils.find_all_file("../static/hipmessageservice/services/schemas/services/*", '身份证号')
    # cda
    utils.find_all_file("../static/hipmessageservice/services/schemas/cdas/*", '身份证号')