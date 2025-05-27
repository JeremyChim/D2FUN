@echo off
setlocal enabledelayedexpansion

echo 警告：此脚本会移除当前目录下所有文件名前的下划线。
echo.
echo 即将处理的目录：%CD%
echo.

:: choice /C YN /M "是否继续执行? [Y/N]"
:: if errorlevel 2 (
::     echo 操作已取消。
::     goto :eof
:: )

for %%a in (*.txt) do (
    set "filename=%%a"
    if "!filename:~0,1!"=="_" (
        if not "%%a"=="%~nx0" (
            set "newname=!filename:~1!"
            echo 正在重命名: "%%a"  -^>  "!newname!"
            ren "%%a" "!newname!"
        )
    )
)

echo.
echo 操作完成！
:: pause
    