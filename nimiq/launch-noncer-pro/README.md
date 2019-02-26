## launch-noncer-pro
This batch script can be used to automatically launch the Noncer Pro Nimiq GPU miner along side the monitor-noncer-pro tool (found at http://github.com/billygarrison/mining-tools/nimiq/monitor-noncer-pro).

### Usage
Edit windows_run.bat and make the following changes:
- Line 1: Set your desired `UV_THREADPOOL_SIZE`
- Line 2: Set the full path to your Noncer Pro .exe file (e.g. C:/NoncerPro/noncerpro.exe)
- Line 2: Set your Nimiq address, threads, and add --batch if you desire
- Line 4: Set the full path to your monitor_noncer_pro.py file (e.g. C:/monitor-noncer-pro/monitor_noncer_pro.py)

You can now run the .bat file and it will launch Noncer Pro as well as monitor-noncer-pro. You can use Windows Task Scheduler to automatically run the .bat file every time the computer is started.

### Task Scheduler Instructions
- Run Task Scheduler
- Click "Create Task"
- Name the task whatever you'd like (e.g. LaunchNoncerPro)
- Leave the rest of the settings on the General tab alone
- Click "New" under the Triggers tab
- Select "Begin the task: at startup"
- Click OK
- Click "New" under the Actions tab
- Select "Action: Start a program"
- Browse for and select "windows_run.bat"
- Click OK
- Uncheck all boxes under the Conditions tab
- Uncheck "Stop the task if it runs longer than"
- Click OK to save the scheduled task

### Automatically rebooting your computer
reboot.bat is a one-line batch file that just reboots your computer. This can be useful since Noncer Pro (like most miners) can crash after running for too long. You can use the Task Scheduler to schedule a task very similarly to the above instructions, except create your trigger to "Begin the task: On a schedule", check "Daily", and set it to however often you want your computer to rstart (I recommend ~3 days).
