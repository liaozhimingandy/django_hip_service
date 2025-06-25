# Changelog

## [26.2.0] - 2025-06-25

### Version Upgrade: `26.1.2` → `26.2.0`

### Features
- **core:** 重构docker镜像构建过程 (6c47259)

### Bug Fixes
- **core:** 修复已知bug (d612401)
- **core:** 修复已知bug (dc04756)

## [26.1.2] - 2025-06-23

### Version Upgrade: `26.1.1` → `26.1.2`

### Bug Fixes
- **core:** 修复已知bug (8e1ad6f)

## [26.1.1] - 2025-06-23

### Version Upgrade: `26.1.0` → `26.1.1`

### Bug Fixes
- **core:** 修复dockerfile文件 (8d78130)

## [26.1.0] - 2025-06-23

### Version Upgrade: `26.0.0` → `26.1.0`

### Features
- **core:** 使用uv管理环境 (f0851de)

### Bug Fixes
- **core:** 修复dockerfile文件 (ac5be08)
- **core:** 修复dockerfile文件 (a846342)
- **core:** 修复dockerfile文件 (c305bdc)
- **core:** 修复dockerfile文件 (dc9a7e4)
- **core:** 修复dockerfile文件 (2a9cdaf)
- **core:** 修复dockerfile文件 (23f153c)
- **core:** 修复dockerfile文件 (89b00ef)
- **core:** 修复dockerfile文件 (c375a0b)
- **core:** 修复dockerfile文件 (6539df5)
- **core:** 修复dockerfile文件 (eaffdab)
- **core:** 修复dockerfile文件 (ca19346)
- **core:** 修复dockerfile文件 (2b9934a)
- **core:** 修复dockerfile文件 (80713b3)
- **core:** 修复dockerfile文件 (e6efa91)
- **core:** 修复dockerfile文件 (875dfc0)
- **core:** 修复dockerfile文件 (a5fe535)

## [5.0.0](https://github.com/liaozhimingandy/django_hip_service/compare/v4.1.0...v5.0.0) (2025-04-10)


### ⚠ BREAKING CHANGES

* `extends` key in config file is now used for extending other config files

### Features

* **color:** 增加模型文档生成工具 ([8c9657c](https://github.com/liaozhimingandy/django_hip_service/commit/8c9657cb0f1b6476584fd87a55da99165166927e))
* **core:** 修复mssql无法连接问题 ([6376080](https://github.com/liaozhimingandy/django_hip_service/commit/6376080b140e6242f20407ec22c5467dd55479ea))
* **core:** 修复已知bug ([1a7df13](https://github.com/liaozhimingandy/django_hip_service/commit/1a7df13cd8b9ef625c552557eb932ccf64aef274))
* **core:** 增加新app, DockerCMD及其它的优化 ([4ce5a2c](https://github.com/liaozhimingandy/django_hip_service/commit/4ce5a2c1a81d358cedd61f253b5754975a728fe1))
* **core:** 完善api ([7ea79df](https://github.com/liaozhimingandy/django_hip_service/commit/7ea79df614e98e44f1b2c16b2099539eaa950a81))
* **core:** 完善api ([944df75](https://github.com/liaozhimingandy/django_hip_service/commit/944df75e48c04df70c78b205b8e4d585aab1e87a))
* **core:** 完善校验文件 ([d38872f](https://github.com/liaozhimingandy/django_hip_service/commit/d38872f7418f7919df31ec7eefb5996c2d7cfe81))
* **core:** 更新dockerfile文件 ([88e3d17](https://github.com/liaozhimingandy/django_hip_service/commit/88e3d170ff6fb4734902280f17d6c77f9d73fbc1))
* **core:** 更新python解释器到3.13 ([5ad560f](https://github.com/liaozhimingandy/django_hip_service/commit/5ad560f89c8eaf7233323be758aed516f5c23fa1))
* 调整部分内容 ([762fe16](https://github.com/liaozhimingandy/django_hip_service/commit/762fe1692e6f925efdfd2c0e5bb040ff4d7212be))
* 调整部分内容 ([c19a7d5](https://github.com/liaozhimingandy/django_hip_service/commit/c19a7d5bfeefc44251c973ee2c08cf9255fa89e0))


### Bug Fixes

* **core:** 修复3.8a3发现的问题 ([75f9a9e](https://github.com/liaozhimingandy/django_hip_service/commit/75f9a9ec9134e5bbf041bbef658b4cc6282c0567))
* **core:** 修复graphQL查询失败问题 ([2278ab4](https://github.com/liaozhimingandy/django_hip_service/commit/2278ab4dfbf4ed230e053ce7dd4c512b4ec0f395))
* **core:** 修复主索引接口调用bug ([670a384](https://github.com/liaozhimingandy/django_hip_service/commit/670a384039ad5b7ca49b2cbddc4e9e7662314827))
* **core:** 修复主索引注册问题 ([1baa97c](https://github.com/liaozhimingandy/django_hip_service/commit/1baa97c87f380465d1e842b66f563200f40a3b0a))
* **core:** 修复合并冲突文件 ([7590252](https://github.com/liaozhimingandy/django_hip_service/commit/7590252468583f0947a4eac1e306a0c16dce35ff))
* **core:** 修复已知bug ([311dd39](https://github.com/liaozhimingandy/django_hip_service/commit/311dd39a87326738eef95a6cc60daa16c0b9809b))
* **core:** 修复已知bug ([b800916](https://github.com/liaozhimingandy/django_hip_service/commit/b800916c71cb6f163d7c4397e8ed1583424df0ca))
* **core:** 修复已知bug ([b7690aa](https://github.com/liaozhimingandy/django_hip_service/commit/b7690aab45b82b992a9c30ccb6025b7b9f02c2dd))
* **core:** 修复已知bug ([f180d06](https://github.com/liaozhimingandy/django_hip_service/commit/f180d060c54ad81a040ebb5f02ccfd75531b4465))
* **core:** 修复并完善已知问题 ([360351e](https://github.com/liaozhimingandy/django_hip_service/commit/360351e68b2e5adfb3e07c1336edbfaad68e3172))
* **core:** 完善校验文件 ([9a8ff77](https://github.com/liaozhimingandy/django_hip_service/commit/9a8ff77eb86c52d2d842b0c75951c96f8df4ca07))
* **scheme:** 修复输血服务的校验文件问题 ([de54f32](https://github.com/liaozhimingandy/django_hip_service/commit/de54f3297319e1182c0f826e71619479ea56ba22))
* 修复docker镜像构建失败问题 ([fa1355f](https://github.com/liaozhimingandy/django_hip_service/commit/fa1355f6d163ea33f77dfa06034101459fa80456))
* 修复docker镜像构建失败问题-2 ([b6c94da](https://github.com/liaozhimingandy/django_hip_service/commit/b6c94dad39872519b7c27bbe4952835ea0f7482d))
* 修复docker镜像构建失败问题-3 ([7591945](https://github.com/liaozhimingandy/django_hip_service/commit/75919455563d8db5bd952c2dc99741c8813afebb))
* 修复docker镜像构建失败问题-4 ([fad95fc](https://github.com/liaozhimingandy/django_hip_service/commit/fad95fc61cd61a1a924faa71941ab597f344a418))
* 修复docker镜像构建失败问题-5 ([d2947ae](https://github.com/liaozhimingandy/django_hip_service/commit/d2947aec50efba2335281d6d6f1e01c513ab03c4))
* 修复版本号获取不对问题 ([d817cfb](https://github.com/liaozhimingandy/django_hip_service/commit/d817cfbab09edde08f5ee94a659781ac1b30efed))


### Performance Improvements

* **color:** 优化一部分代码 ([26ba059](https://github.com/liaozhimingandy/django_hip_service/commit/26ba05967f824636b2a4863bdb92005563e6e1fb))
* **core:** 优化部分代码 ([34c6c70](https://github.com/liaozhimingandy/django_hip_service/commit/34c6c706c4ed7ed0371ee17f8fb06782cd73a3ea))
* **core:** 完善校验 ([ab22886](https://github.com/liaozhimingandy/django_hip_service/commit/ab22886b2ec7bdf82c00f7b024df887ad6f7f1d5))
* **core:** 完善配置 ([5b5379d](https://github.com/liaozhimingandy/django_hip_service/commit/5b5379d64fe48269a741d0ef02c4b04822c729a9))
* **core:** 完善配置 ([b7bcf91](https://github.com/liaozhimingandy/django_hip_service/commit/b7bcf91cf7c288762b7a8b7948c47ff6d59c9387))
* **core:** 补充医院要求市互认接口上传加密和签名功能 ([eeb4347](https://github.com/liaozhimingandy/django_hip_service/commit/eeb4347fea32ca1a2cce4aea21b54aabc8524a8f))
* **core:** 重构 ([b2880f6](https://github.com/liaozhimingandy/django_hip_service/commit/b2880f671329676bea13eeb08b2ed07c60f84614))
* **core:** 重构 ([f247fda](https://github.com/liaozhimingandy/django_hip_service/commit/f247fda08bc3061e725a2fd7a0196dcd43bbc885))
* **core:** 重构 ([bb36576](https://github.com/liaozhimingandy/django_hip_service/commit/bb36576dc05bb332238dd3e4004e5b15885ebf35))
* **core:** 重构 ([2485aec](https://github.com/liaozhimingandy/django_hip_service/commit/2485aec0c1ad61512c6441cfb81c3b0845bdfe3b))
* **core:** 重构 ([bea5a2d](https://github.com/liaozhimingandy/django_hip_service/commit/bea5a2dbea50115c0a0d25006b49b982db29ef2e))
* **core:** 重构 ([f54ac34](https://github.com/liaozhimingandy/django_hip_service/commit/f54ac34f1586347c0a29f47d58eb258487fd1dc7))
* **core:** 重构 ([9354dca](https://github.com/liaozhimingandy/django_hip_service/commit/9354dca515bf6a320de67c7f10f075cc6df2d971))
* **core:** 重构 ([8ec9ef9](https://github.com/liaozhimingandy/django_hip_service/commit/8ec9ef9b17c8b7b95dab1b48ccc08ff558192720))
* **core:** 重构 ([ca6b069](https://github.com/liaozhimingandy/django_hip_service/commit/ca6b069dfc706a5300e77907e906561f9c3c1888))
* **core:** 重构 ([8c615aa](https://github.com/liaozhimingandy/django_hip_service/commit/8c615aa0762cbaad5ef99c46957d9991db7185e0))
* **core:** 重构 ([f8a799f](https://github.com/liaozhimingandy/django_hip_service/commit/f8a799f5af1e47b675ccea563917dcfd9e840252))
* **core:** 重构 ([32918a3](https://github.com/liaozhimingandy/django_hip_service/commit/32918a39b687935b3603b5abee4801e592481f83))
* **core:** 重构 ([0485b13](https://github.com/liaozhimingandy/django_hip_service/commit/0485b131eaa23175264914e7a777ce7ad312ef64))
* **core:** 重构 ([93a33e1](https://github.com/liaozhimingandy/django_hip_service/commit/93a33e1900ab881b8ca38fa01dff3aa27ff1bc9a))
* **core:** 重构dockerfile构建文件 ([f702388](https://github.com/liaozhimingandy/django_hip_service/commit/f702388c4584b7877bfb3ac50ddceb80926f7133))

## [4.1.0](https://github.com/liaozhimingandy/django_hip_service/compare/v4.0.1...v4.1.0) (2025-02-19)


### Features

* **core:** 增加新app, DockerCMD及其它的优化 ([4ce5a2c](https://github.com/liaozhimingandy/django_hip_service/commit/4ce5a2c1a81d358cedd61f253b5754975a728fe1))
* **core:** 完善api ([7ea79df](https://github.com/liaozhimingandy/django_hip_service/commit/7ea79df614e98e44f1b2c16b2099539eaa950a81))
* **core:** 完善api ([944df75](https://github.com/liaozhimingandy/django_hip_service/commit/944df75e48c04df70c78b205b8e4d585aab1e87a))


### Bug Fixes

* **core:** 修复已知bug ([311dd39](https://github.com/liaozhimingandy/django_hip_service/commit/311dd39a87326738eef95a6cc60daa16c0b9809b))

## [4.0.1](https://github.com/liaozhimingandy/django_hip_service/compare/v4.0.0...v4.0.1) (2024-12-10)


### Bug Fixes

* **core:** 修复主索引接口调用bug ([670a384](https://github.com/liaozhimingandy/django_hip_service/commit/670a384039ad5b7ca49b2cbddc4e9e7662314827))

## [4.0.0](https://github.com/liaozhimingandy/django_hip_service/compare/v3.1.0...v4.0.0) (2024-12-06)


### ⚠ BREAKING CHANGES

* `extends` key in config file is now used for extending other config files

### Features

* **color:** 增加模型文档生成工具 ([8c9657c](https://github.com/liaozhimingandy/django_hip_service/commit/8c9657cb0f1b6476584fd87a55da99165166927e))
* **core:** 修复已知bug ([1a7df13](https://github.com/liaozhimingandy/django_hip_service/commit/1a7df13cd8b9ef625c552557eb932ccf64aef274))
* **core:** 更新dockerfile文件 ([88e3d17](https://github.com/liaozhimingandy/django_hip_service/commit/88e3d170ff6fb4734902280f17d6c77f9d73fbc1))
* **core:** 更新python解释器到3.13 ([5ad560f](https://github.com/liaozhimingandy/django_hip_service/commit/5ad560f89c8eaf7233323be758aed516f5c23fa1))
* 调整部分内容 ([762fe16](https://github.com/liaozhimingandy/django_hip_service/commit/762fe1692e6f925efdfd2c0e5bb040ff4d7212be))
* 调整部分内容 ([c19a7d5](https://github.com/liaozhimingandy/django_hip_service/commit/c19a7d5bfeefc44251c973ee2c08cf9255fa89e0))


### Bug Fixes

* **core:** 修复3.8a3发现的问题 ([75f9a9e](https://github.com/liaozhimingandy/django_hip_service/commit/75f9a9ec9134e5bbf041bbef658b4cc6282c0567))
* **core:** 修复graphQL查询失败问题 ([2278ab4](https://github.com/liaozhimingandy/django_hip_service/commit/2278ab4dfbf4ed230e053ce7dd4c512b4ec0f395))
* **core:** 修复主索引注册问题 ([1baa97c](https://github.com/liaozhimingandy/django_hip_service/commit/1baa97c87f380465d1e842b66f563200f40a3b0a))
* **core:** 修复合并冲突文件 ([7590252](https://github.com/liaozhimingandy/django_hip_service/commit/7590252468583f0947a4eac1e306a0c16dce35ff))
* **core:** 修复已知bug ([b800916](https://github.com/liaozhimingandy/django_hip_service/commit/b800916c71cb6f163d7c4397e8ed1583424df0ca))
* **core:** 修复已知bug ([b7690aa](https://github.com/liaozhimingandy/django_hip_service/commit/b7690aab45b82b992a9c30ccb6025b7b9f02c2dd))
* **core:** 修复已知bug ([f180d06](https://github.com/liaozhimingandy/django_hip_service/commit/f180d060c54ad81a040ebb5f02ccfd75531b4465))
* **core:** 修复并完善已知问题 ([360351e](https://github.com/liaozhimingandy/django_hip_service/commit/360351e68b2e5adfb3e07c1336edbfaad68e3172))
* **scheme:** 修复输血服务的校验文件问题 ([de54f32](https://github.com/liaozhimingandy/django_hip_service/commit/de54f3297319e1182c0f826e71619479ea56ba22))
* 修复docker镜像构建失败问题 ([fa1355f](https://github.com/liaozhimingandy/django_hip_service/commit/fa1355f6d163ea33f77dfa06034101459fa80456))
* 修复docker镜像构建失败问题-2 ([b6c94da](https://github.com/liaozhimingandy/django_hip_service/commit/b6c94dad39872519b7c27bbe4952835ea0f7482d))
* 修复docker镜像构建失败问题-3 ([7591945](https://github.com/liaozhimingandy/django_hip_service/commit/75919455563d8db5bd952c2dc99741c8813afebb))
* 修复docker镜像构建失败问题-4 ([fad95fc](https://github.com/liaozhimingandy/django_hip_service/commit/fad95fc61cd61a1a924faa71941ab597f344a418))
* 修复docker镜像构建失败问题-5 ([d2947ae](https://github.com/liaozhimingandy/django_hip_service/commit/d2947aec50efba2335281d6d6f1e01c513ab03c4))
* 修复版本号获取不对问题 ([d817cfb](https://github.com/liaozhimingandy/django_hip_service/commit/d817cfbab09edde08f5ee94a659781ac1b30efed))


### Performance Improvements

* **color:** 优化一部分代码 ([26ba059](https://github.com/liaozhimingandy/django_hip_service/commit/26ba05967f824636b2a4863bdb92005563e6e1fb))
* **core:** 优化部分代码 ([34c6c70](https://github.com/liaozhimingandy/django_hip_service/commit/34c6c706c4ed7ed0371ee17f8fb06782cd73a3ea))
* **core:** 完善校验 ([ab22886](https://github.com/liaozhimingandy/django_hip_service/commit/ab22886b2ec7bdf82c00f7b024df887ad6f7f1d5))
* **core:** 完善配置 ([5b5379d](https://github.com/liaozhimingandy/django_hip_service/commit/5b5379d64fe48269a741d0ef02c4b04822c729a9))
* **core:** 完善配置 ([b7bcf91](https://github.com/liaozhimingandy/django_hip_service/commit/b7bcf91cf7c288762b7a8b7948c47ff6d59c9387))
* **core:** 补充医院要求市互认接口上传加密和签名功能 ([eeb4347](https://github.com/liaozhimingandy/django_hip_service/commit/eeb4347fea32ca1a2cce4aea21b54aabc8524a8f))
* **core:** 重构 ([b2880f6](https://github.com/liaozhimingandy/django_hip_service/commit/b2880f671329676bea13eeb08b2ed07c60f84614))
* **core:** 重构 ([f247fda](https://github.com/liaozhimingandy/django_hip_service/commit/f247fda08bc3061e725a2fd7a0196dcd43bbc885))
* **core:** 重构 ([bb36576](https://github.com/liaozhimingandy/django_hip_service/commit/bb36576dc05bb332238dd3e4004e5b15885ebf35))
* **core:** 重构 ([2485aec](https://github.com/liaozhimingandy/django_hip_service/commit/2485aec0c1ad61512c6441cfb81c3b0845bdfe3b))
* **core:** 重构 ([bea5a2d](https://github.com/liaozhimingandy/django_hip_service/commit/bea5a2dbea50115c0a0d25006b49b982db29ef2e))
* **core:** 重构 ([f54ac34](https://github.com/liaozhimingandy/django_hip_service/commit/f54ac34f1586347c0a29f47d58eb258487fd1dc7))
* **core:** 重构 ([9354dca](https://github.com/liaozhimingandy/django_hip_service/commit/9354dca515bf6a320de67c7f10f075cc6df2d971))
* **core:** 重构 ([8ec9ef9](https://github.com/liaozhimingandy/django_hip_service/commit/8ec9ef9b17c8b7b95dab1b48ccc08ff558192720))
* **core:** 重构 ([ca6b069](https://github.com/liaozhimingandy/django_hip_service/commit/ca6b069dfc706a5300e77907e906561f9c3c1888))
* **core:** 重构 ([8c615aa](https://github.com/liaozhimingandy/django_hip_service/commit/8c615aa0762cbaad5ef99c46957d9991db7185e0))
* **core:** 重构 ([f8a799f](https://github.com/liaozhimingandy/django_hip_service/commit/f8a799f5af1e47b675ccea563917dcfd9e840252))
* **core:** 重构 ([32918a3](https://github.com/liaozhimingandy/django_hip_service/commit/32918a39b687935b3603b5abee4801e592481f83))
* **core:** 重构 ([0485b13](https://github.com/liaozhimingandy/django_hip_service/commit/0485b131eaa23175264914e7a777ce7ad312ef64))
* **core:** 重构 ([93a33e1](https://github.com/liaozhimingandy/django_hip_service/commit/93a33e1900ab881b8ca38fa01dff3aa27ff1bc9a))
* **core:** 重构dockerfile构建文件 ([f702388](https://github.com/liaozhimingandy/django_hip_service/commit/f702388c4584b7877bfb3ac50ddceb80926f7133))

## [3.1.0](https://github.com/liaozhimingandy/django_hip_service/compare/v3.0.1...v3.1.0) (2024-12-06)


### Features

* **color:** 增加模型文档生成工具 ([8c9657c](https://github.com/liaozhimingandy/django_hip_service/commit/8c9657cb0f1b6476584fd87a55da99165166927e))
* **core:** 修复已知bug ([1a7df13](https://github.com/liaozhimingandy/django_hip_service/commit/1a7df13cd8b9ef625c552557eb932ccf64aef274))


### Bug Fixes

* **core:** 修复已知bug ([b800916](https://github.com/liaozhimingandy/django_hip_service/commit/b800916c71cb6f163d7c4397e8ed1583424df0ca))
* **scheme:** 修复输血服务的校验文件问题 ([de54f32](https://github.com/liaozhimingandy/django_hip_service/commit/de54f3297319e1182c0f826e71619479ea56ba22))


### Performance Improvements

* **color:** 优化一部分代码 ([26ba059](https://github.com/liaozhimingandy/django_hip_service/commit/26ba05967f824636b2a4863bdb92005563e6e1fb))

## [3.0.1](https://github.com/liaozhimingandy/django_hip_service/compare/v3.0.0...v3.0.1) (2024-11-19)


### Bug Fixes

* 修复docker镜像构建失败问题-5 ([d2947ae](https://github.com/liaozhimingandy/django_hip_service/commit/d2947aec50efba2335281d6d6f1e01c513ab03c4))

## [3.0.0](https://github.com/liaozhimingandy/django_hip_service/compare/v2.0.0...v3.0.0) (2024-11-19)


### ⚠ BREAKING CHANGES

* `extends` key in config file is now used for extending other config files

### Features

* **core:** 更新dockerfile文件 ([88e3d17](https://github.com/liaozhimingandy/django_hip_service/commit/88e3d170ff6fb4734902280f17d6c77f9d73fbc1))
* **core:** 更新python解释器到3.13 ([5ad560f](https://github.com/liaozhimingandy/django_hip_service/commit/5ad560f89c8eaf7233323be758aed516f5c23fa1))
* 调整部分内容 ([762fe16](https://github.com/liaozhimingandy/django_hip_service/commit/762fe1692e6f925efdfd2c0e5bb040ff4d7212be))
* 调整部分内容 ([c19a7d5](https://github.com/liaozhimingandy/django_hip_service/commit/c19a7d5bfeefc44251c973ee2c08cf9255fa89e0))


### Bug Fixes

* **core:** 修复3.8a3发现的问题 ([75f9a9e](https://github.com/liaozhimingandy/django_hip_service/commit/75f9a9ec9134e5bbf041bbef658b4cc6282c0567))
* **core:** 修复graphQL查询失败问题 ([2278ab4](https://github.com/liaozhimingandy/django_hip_service/commit/2278ab4dfbf4ed230e053ce7dd4c512b4ec0f395))
* **core:** 修复主索引注册问题 ([1baa97c](https://github.com/liaozhimingandy/django_hip_service/commit/1baa97c87f380465d1e842b66f563200f40a3b0a))
* **core:** 修复合并冲突文件 ([7590252](https://github.com/liaozhimingandy/django_hip_service/commit/7590252468583f0947a4eac1e306a0c16dce35ff))
* **core:** 修复已知bug ([b7690aa](https://github.com/liaozhimingandy/django_hip_service/commit/b7690aab45b82b992a9c30ccb6025b7b9f02c2dd))
* **core:** 修复已知bug ([f180d06](https://github.com/liaozhimingandy/django_hip_service/commit/f180d060c54ad81a040ebb5f02ccfd75531b4465))
* **core:** 修复并完善已知问题 ([360351e](https://github.com/liaozhimingandy/django_hip_service/commit/360351e68b2e5adfb3e07c1336edbfaad68e3172))
* 修复docker镜像构建失败问题 ([fa1355f](https://github.com/liaozhimingandy/django_hip_service/commit/fa1355f6d163ea33f77dfa06034101459fa80456))
* 修复docker镜像构建失败问题-2 ([b6c94da](https://github.com/liaozhimingandy/django_hip_service/commit/b6c94dad39872519b7c27bbe4952835ea0f7482d))
* 修复docker镜像构建失败问题-3 ([7591945](https://github.com/liaozhimingandy/django_hip_service/commit/75919455563d8db5bd952c2dc99741c8813afebb))
* 修复docker镜像构建失败问题-4 ([fad95fc](https://github.com/liaozhimingandy/django_hip_service/commit/fad95fc61cd61a1a924faa71941ab597f344a418))
* 修复版本号获取不对问题 ([d817cfb](https://github.com/liaozhimingandy/django_hip_service/commit/d817cfbab09edde08f5ee94a659781ac1b30efed))


### Performance Improvements

* **core:** 优化部分代码 ([34c6c70](https://github.com/liaozhimingandy/django_hip_service/commit/34c6c706c4ed7ed0371ee17f8fb06782cd73a3ea))
* **core:** 完善校验 ([ab22886](https://github.com/liaozhimingandy/django_hip_service/commit/ab22886b2ec7bdf82c00f7b024df887ad6f7f1d5))
* **core:** 完善配置 ([5b5379d](https://github.com/liaozhimingandy/django_hip_service/commit/5b5379d64fe48269a741d0ef02c4b04822c729a9))
* **core:** 完善配置 ([b7bcf91](https://github.com/liaozhimingandy/django_hip_service/commit/b7bcf91cf7c288762b7a8b7948c47ff6d59c9387))
* **core:** 补充医院要求市互认接口上传加密和签名功能 ([eeb4347](https://github.com/liaozhimingandy/django_hip_service/commit/eeb4347fea32ca1a2cce4aea21b54aabc8524a8f))
* **core:** 重构 ([b2880f6](https://github.com/liaozhimingandy/django_hip_service/commit/b2880f671329676bea13eeb08b2ed07c60f84614))
* **core:** 重构 ([f247fda](https://github.com/liaozhimingandy/django_hip_service/commit/f247fda08bc3061e725a2fd7a0196dcd43bbc885))
* **core:** 重构 ([bb36576](https://github.com/liaozhimingandy/django_hip_service/commit/bb36576dc05bb332238dd3e4004e5b15885ebf35))
* **core:** 重构 ([2485aec](https://github.com/liaozhimingandy/django_hip_service/commit/2485aec0c1ad61512c6441cfb81c3b0845bdfe3b))
* **core:** 重构 ([bea5a2d](https://github.com/liaozhimingandy/django_hip_service/commit/bea5a2dbea50115c0a0d25006b49b982db29ef2e))
* **core:** 重构 ([f54ac34](https://github.com/liaozhimingandy/django_hip_service/commit/f54ac34f1586347c0a29f47d58eb258487fd1dc7))
* **core:** 重构 ([9354dca](https://github.com/liaozhimingandy/django_hip_service/commit/9354dca515bf6a320de67c7f10f075cc6df2d971))
* **core:** 重构 ([8ec9ef9](https://github.com/liaozhimingandy/django_hip_service/commit/8ec9ef9b17c8b7b95dab1b48ccc08ff558192720))
* **core:** 重构 ([ca6b069](https://github.com/liaozhimingandy/django_hip_service/commit/ca6b069dfc706a5300e77907e906561f9c3c1888))
* **core:** 重构 ([8c615aa](https://github.com/liaozhimingandy/django_hip_service/commit/8c615aa0762cbaad5ef99c46957d9991db7185e0))
* **core:** 重构 ([f8a799f](https://github.com/liaozhimingandy/django_hip_service/commit/f8a799f5af1e47b675ccea563917dcfd9e840252))
* **core:** 重构 ([32918a3](https://github.com/liaozhimingandy/django_hip_service/commit/32918a39b687935b3603b5abee4801e592481f83))
* **core:** 重构 ([0485b13](https://github.com/liaozhimingandy/django_hip_service/commit/0485b131eaa23175264914e7a777ce7ad312ef64))
* **core:** 重构 ([93a33e1](https://github.com/liaozhimingandy/django_hip_service/commit/93a33e1900ab881b8ca38fa01dff3aa27ff1bc9a))
* **core:** 重构dockerfile构建文件 ([f702388](https://github.com/liaozhimingandy/django_hip_service/commit/f702388c4584b7877bfb3ac50ddceb80926f7133))

## 3.10.0 (2024-11-19)


### Features

* **core:** 更新dockerfile文件 ([88e3d17](https://github.com/liaozhimingandy/django_hip_service/commit/88e3d170ff6fb4734902280f17d6c77f9d73fbc1))
* **core:** 更新python解释器到3.13 ([5ad560f](https://github.com/liaozhimingandy/django_hip_service/commit/5ad560f89c8eaf7233323be758aed516f5c23fa1))
* 调整部分内容 ([762fe16](https://github.com/liaozhimingandy/django_hip_service/commit/762fe1692e6f925efdfd2c0e5bb040ff4d7212be))
* 调整部分内容 ([c19a7d5](https://github.com/liaozhimingandy/django_hip_service/commit/c19a7d5bfeefc44251c973ee2c08cf9255fa89e0))


### Bug Fixes

* **core:** 修复3.8a3发现的问题 ([75f9a9e](https://github.com/liaozhimingandy/django_hip_service/commit/75f9a9ec9134e5bbf041bbef658b4cc6282c0567))
* **core:** 修复graphQL查询失败问题 ([2278ab4](https://github.com/liaozhimingandy/django_hip_service/commit/2278ab4dfbf4ed230e053ce7dd4c512b4ec0f395))
* **core:** 修复主索引注册问题 ([1baa97c](https://github.com/liaozhimingandy/django_hip_service/commit/1baa97c87f380465d1e842b66f563200f40a3b0a))
* **core:** 修复合并冲突文件 ([7590252](https://github.com/liaozhimingandy/django_hip_service/commit/7590252468583f0947a4eac1e306a0c16dce35ff))
* **core:** 修复已知bug ([b7690aa](https://github.com/liaozhimingandy/django_hip_service/commit/b7690aab45b82b992a9c30ccb6025b7b9f02c2dd))
* **core:** 修复已知bug ([f180d06](https://github.com/liaozhimingandy/django_hip_service/commit/f180d060c54ad81a040ebb5f02ccfd75531b4465))
* **core:** 修复并完善已知问题 ([360351e](https://github.com/liaozhimingandy/django_hip_service/commit/360351e68b2e5adfb3e07c1336edbfaad68e3172))
* 修复版本号获取不对问题 ([d817cfb](https://github.com/liaozhimingandy/django_hip_service/commit/d817cfbab09edde08f5ee94a659781ac1b30efed))


### Performance Improvements

* **core:** 优化部分代码 ([34c6c70](https://github.com/liaozhimingandy/django_hip_service/commit/34c6c706c4ed7ed0371ee17f8fb06782cd73a3ea))
* **core:** 完善校验 ([ab22886](https://github.com/liaozhimingandy/django_hip_service/commit/ab22886b2ec7bdf82c00f7b024df887ad6f7f1d5))
* **core:** 完善配置 ([5b5379d](https://github.com/liaozhimingandy/django_hip_service/commit/5b5379d64fe48269a741d0ef02c4b04822c729a9))
* **core:** 完善配置 ([b7bcf91](https://github.com/liaozhimingandy/django_hip_service/commit/b7bcf91cf7c288762b7a8b7948c47ff6d59c9387))
* **core:** 补充医院要求市互认接口上传加密和签名功能 ([eeb4347](https://github.com/liaozhimingandy/django_hip_service/commit/eeb4347fea32ca1a2cce4aea21b54aabc8524a8f))
* **core:** 重构 ([b2880f6](https://github.com/liaozhimingandy/django_hip_service/commit/b2880f671329676bea13eeb08b2ed07c60f84614))
* **core:** 重构 ([f247fda](https://github.com/liaozhimingandy/django_hip_service/commit/f247fda08bc3061e725a2fd7a0196dcd43bbc885))
* **core:** 重构 ([bb36576](https://github.com/liaozhimingandy/django_hip_service/commit/bb36576dc05bb332238dd3e4004e5b15885ebf35))
* **core:** 重构 ([2485aec](https://github.com/liaozhimingandy/django_hip_service/commit/2485aec0c1ad61512c6441cfb81c3b0845bdfe3b))
* **core:** 重构 ([bea5a2d](https://github.com/liaozhimingandy/django_hip_service/commit/bea5a2dbea50115c0a0d25006b49b982db29ef2e))
* **core:** 重构 ([f54ac34](https://github.com/liaozhimingandy/django_hip_service/commit/f54ac34f1586347c0a29f47d58eb258487fd1dc7))
* **core:** 重构 ([9354dca](https://github.com/liaozhimingandy/django_hip_service/commit/9354dca515bf6a320de67c7f10f075cc6df2d971))
* **core:** 重构 ([8ec9ef9](https://github.com/liaozhimingandy/django_hip_service/commit/8ec9ef9b17c8b7b95dab1b48ccc08ff558192720))
* **core:** 重构 ([ca6b069](https://github.com/liaozhimingandy/django_hip_service/commit/ca6b069dfc706a5300e77907e906561f9c3c1888))
* **core:** 重构 ([8c615aa](https://github.com/liaozhimingandy/django_hip_service/commit/8c615aa0762cbaad5ef99c46957d9991db7185e0))
* **core:** 重构 ([f8a799f](https://github.com/liaozhimingandy/django_hip_service/commit/f8a799f5af1e47b675ccea563917dcfd9e840252))
* **core:** 重构 ([32918a3](https://github.com/liaozhimingandy/django_hip_service/commit/32918a39b687935b3603b5abee4801e592481f83))
* **core:** 重构 ([0485b13](https://github.com/liaozhimingandy/django_hip_service/commit/0485b131eaa23175264914e7a777ce7ad312ef64))
* **core:** 重构 ([93a33e1](https://github.com/liaozhimingandy/django_hip_service/commit/93a33e1900ab881b8ca38fa01dff3aa27ff1bc9a))
* **core:** 重构dockerfile构建文件 ([f702388](https://github.com/liaozhimingandy/django_hip_service/commit/f702388c4584b7877bfb3ac50ddceb80926f7133))
