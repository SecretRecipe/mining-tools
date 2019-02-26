## monitor-noncer-pro

# Usage
- Make sure to have Python installed. The only dependency that isn't built in is `requests`, install using `pip install requests`
- Edit monitor_noncer_pro.py and change the values of `gmailAddress`, `gmailPassword`, `sendToAddress`, and if necessary, `apiUrl` and `interval`.
- Run the windows_run.bat file and leave it running. If there are errors with your miner, it will send you an email.

# Notes
- In the gmail account for `gmailAddress` be sure to allow less secure apps: https://devanswers.co/allow-less-secure-apps-access-gmail-account/
- In the email account for `sendToAddress`, you may need to add `gmailAddress` to your contacts to avoid getting marked as spam

# TODO
- Get user to enter password instead of hard-coding