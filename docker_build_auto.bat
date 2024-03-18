@echo off

rem get Git hash
for /f "tokens=*" %%a in ('git rev-parse --short HEAD') do set GIT_HASH=%%a
for /f "tokens=*" %%a in ('git rev-parse --abbrev-ref HEAD') do set GIT_BRANCH=%%a

echo %GIT_HASH% > AppVersionHash.txt

rem 获取当前日期
for /f "tokens=2 delims==" %%a in ('wmic path win32_operatingsystem get LocalDateTime /value') do (
    set t=%%a
)

set Today=%t:~0,4%%t:~4,2%%t:~6,2%

rem 提取年月信息
set year=%Today:~0,4%
set month=%Today:~4,2%

rem build image for docker use git hash
docker build -t django_hip:%year%%month% .