@echo off
setlocal enabledelayedexpansion

echo 警告：此脚本会在当前目录下的所有文件名前添加下划线。
echo.
echo 即将处理的目录：%CD%
echo.

:: choice /C YN /M "是否继续执行? [Y/N]"
:: if errorlevel 2 (
::     echo 操作已取消。
::     goto :eof
:: )

for %%a in (*.txt) do (
    if not "%%a"=="%~nx0" (
        echo rename: "%%a"  -^>  "_%%a"
        ren "%%a" "_%%a"
    )
)

echo.
echo 操作完成！
:: pause
    