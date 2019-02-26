# Gmail credentials to send email from (must be Gmail)
gmailAddress = "<gmail_address_to_send_from>"
gmailPassword = "<gmail_password>"

# Email address to send notification too (can be any email)
sendToAddress = "<email_address_to_send_to>"

# Api URL (default is http://localhost:3000/api)
apiUrl = "http://localhost:3000/api"

# Interval between checking miner
interval = 5*60

# TODO
# - Get user to enter password instead of hard-coding

# DEPENDENCIES
# - requests

# NOTES
# - In the gmail account for `gmailAddress` be sure to allow less secure apps: https://devanswers.co/allow-less-secure-apps-access-gmail-account/
# - In the email account for `sendToAddress`, you may need to add `gmailAddress` to your contacts to avoid getting marked as spam



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


def checkMiner():
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

		return True

	except ValueError as e:
		msg = "*** NONCER PRO NIMIQ GPU MINER ALERT ***"
		msg += "\n" + str(e)
		sendEmail(msg)
		print(msg)
		
		return False

	except Exception as e:
		msg = "*** NONCER PRO NIMIQ GPU MINER ALERT ***"
		msg += "\nSomething went wrong with the miner!"
		sendEmail(msg)
		print(msg)

		return False

while True:
	if checkMiner() == False:
		break
	time.sleep(interval)

print("Program ending")

