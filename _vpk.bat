@echo off
@chcp 65001 >nul

vpk\vpk.exe vpk\pak01_dir

timeout 1

set source="vpk\pak01_dir.vpk"
set destination="E:\GAME\steamapps\common\dota 2 beta\game\mod"

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

:: start "" "E:\GAME\steamapps\common\dota 2 beta\game\bin\win64\dota2.exe"
:: start "" "E:\GAME\steamapps\common\Lossless Scaling\LosslessScaling.exe"