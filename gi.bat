@echo off
@chcp 65001 >nul

set source="gi\gameinfo.gi"
set destination="E:\GAME\steamapps\common\dota 2 beta\game\dota"

if exist %source% (
    if not exist %destination% (
        mkdir %destination%
    )
    copy %source% %destination%
    if %errorlevel% equ 0 (
        echo 文件复制成功。
    ) else (
        echo 文件复制失败。
    )
) else (
    echo 源文件不存在。
)

timeout 1

set source="gi\gameinfo_branchspecific.gi"
set destination="E:\GAME\steamapps\common\dota 2 beta\game\dota"

if exist %source% (
    if not exist %destination% (
        mkdir %destination%
    )
    copy %source% %destination%
    if %errorlevel% equ 0 (
        echo 文件复制成功。
    ) else (
        echo 文件复制失败。
    )
) else (
    echo 源文件不存在。
)

timeout 1