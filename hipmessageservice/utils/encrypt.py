#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： encrypt.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-06-05 10:19
    @Desc: 加解密工具
================================================="""
import base64
import hashlib
import json
from dataclasses import dataclass
import time

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


@dataclass(frozen=True)
class EncryptUtils:
    key: str
    hospital_id: str

    def _encrypt_bytes(self, data: bytes) -> bytes:
        """
       AES加密
       :param data: 明文（字节串）
       :param key: 密钥（字节串），长度应为16（AES-128）, 24（AES-192）, 或 32（AES-256）
       :return: 密文（字节串）
       """

        # AES是块加密算法，数据长度需要是块大小的倍数（对于AES，块大小为16字节）
        # 如果不是，需要进行填充
        if len(self.key) not in [16, 24, 32]:
            raise ValueError("Key must be either 16 bytes for AES-128, 24 bytes for AES-192, or 32 bytes for AES-256")
        cipher = AES.new(self.key.encode("UTF-8"), AES.MODE_ECB)  # 注意：ECB模式不安全，通常使用CBC, CFB, OFB, CTR, GCM等模式
        # 如果使用CBC模式，你需要一个初始化向量(IV)，并且需要保存它以备解密时使用
        # 在此示例中，我们仅使用ECB模式以简化代码
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        return ciphertext

    def encrypt(self, encrypt_data: dict) -> str:
        """
        对数据使用key进行加密
        :param encrypt_data: 待加密的数据
        :param encrypt_key:  加密用到的key
        :return:
        """
        # 需要根据key进行排序
        content = json.dumps(encrypt_data, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        encrypted_data = self._encrypt_bytes(content.encode("UTF-8"))
        return base64.b64encode(encrypted_data).decode('utf-8')

    def sign(self) -> tuple:
        """　
        形如:　hospitalId=ncdxfskqyy&timestamp=xxxxxxxx
        :return:
        """
        # 获取当前时间戳（以秒为单位）
        current_timestamp = int(time.time())
        # current_timestamp = 1704954674288
        sign_data = f"hospitalId={self.hospital_id}&timestamp={current_timestamp}"

        encrypted_data = self._encrypt_bytes(sign_data.encode("UTF-8"))
        md5_hash = hashlib.md5(encrypted_data).hexdigest()
        return md5_hash, current_timestamp


if __name__ == "__main__":
    key = "tGuWgUr8PaS3dl7m"
    hospital_id = "ytlyyy_001"
    encrypt = EncryptUtils(key=key, hospital_id=hospital_id)
    # 数据
    data = {"name":"测试11", "id_card_no":"111111"}
    # 签名
    md5_hash = encrypt.sign()
    # 加密
    encrypted = encrypt.encrypt(data)
    print(encrypted, md5_hash)

