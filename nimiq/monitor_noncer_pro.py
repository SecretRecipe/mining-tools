# Gmail credentials to send email from (must be Gmail)
gmailAddress = "<gmail_address_to_send_from>"
gmailPassword = "<gmail_password>"

# Email address to send notification too (can be any email)
sendToAddress = "<email_address_to_send_to>"

apiUrl = "http://localhost:3000/api"

# TODO
#- Send email alert instead of print statement
#- Run in background
#- Get user to enter password instead of hard-coding

# DEPENDENCIES
#- requests
import json, sys, time, smtplib
import requests


def zeroHashrate(apiUrl):
	try:
		# Get JSON data from API
		data = requests.get(apiUrl)
		miner = json.loads(data.text)

		# Loop through devices, if any have hashrate=0 for >60 sec, raise error
		for device in miner["devices"]:
			gpuId = device["gpuId"]
			hashrate = device["hashrate"]
			if hashrate == 0:
				return True
		return False

	except Exception as e:
		print(str(e))


def sendEmail(msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(gmailAddress, gmailPassword)
	server.sendmail(gmailAddress, sendToAddress, msg)
	server.quit()



try:
	# Get JSON data from API
	data = requests.get(apiUrl)
	miner = json.loads(data.text)

	if zeroHashrate(apiUrl) == True:
		print("Hashrate is 0... waiting 60 s")
		time.sleep(60)
		if zeroHashrate(apiUrl) == True:
			raise ValueError("Hashrate was 0 for 60+ seconds")
		else:
			print("All good!")

except Exception as e:
	print(str(e))
	# Send email
	msg = str(e) + "\n\nSomething went wrong. Error message above. Sending email."
	print(msg)
	#sendEmail(msg)

