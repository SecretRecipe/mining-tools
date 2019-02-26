SET UV_THREADPOOL_SIZE=32

cd "<Path/To/NoncerPro/Folder>"

start cmd /k CALL noncerpro.exe --address="NQ05 PMG6 E64G BUCG 703E D38G 6H5F 34LB 6NAF" --threads=2

timeout /t 1 /nobreak

cd "<Path/To/monitor-noncer-pro/Folder>"
CALL python monitor_noncer_pro.py

pause
