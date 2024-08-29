#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： test.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-04-23 16:06
    @Desc: 
================================================="""
import json

if __name__ == "__main__":
    # https://the-x.cn/zh-cn/cryptography/Sm4.aspx
    app_id = '19d8dca4b4c247f0bcd1c646bce94a10'
    app_key = '041cac65e6fecaeb59e352341baaf56823e1aa0ea36acf57c086c7f2371de51518e82edbfe5680f98cfe1f2e718fcec9f5bec1c64b015a7b052a3d89c8eee72f9f'
    app_secret = '423414dd8e04dfaaa1d82a115b017547022e9491c40ce9a818d2cde81bac0745'

    from gmssl import sm4
    from gmssl.sm4 import CryptSM4

    # 创建一个SM4加密器
    sm4_crypt = CryptSM4()
    # 设置密钥
    sm4_crypt.set_key(app_id.encode(), sm4.SM4_ENCRYPT)
    # 加密
    new_key_str = sm4_crypt.crypt_ecb(app_secret.encode()).hex().upper()
    print(new_key_str[:32])

    data = {"name": "John Doe","age": 10,"description": "This is a test object"}
    content = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    print(content)

    sm4_crypt.set_key(new_key_str[:32].encode(), sm4.SM4_ENCRYPT)
    result = sm4_crypt.crypt_ecb(content.encode()).hex().upper()

    print(result)
