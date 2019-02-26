# Nimiq mining tools
This is a collection of scripts I've made to use for mining the cryptocurrency "Nimiq". So far these are Windows-only.

## monitor-noncer-pro
This is a Python program that uses the Noncer Pro API to monitor the status of the miner. If the hashrate is 0 for 60+ seconds, or if the miner can't be reached, an email alert is sent.

## launch-noncer-pro
This is a batch script that can be used to automatically launch the Noncer Pro Nimiq GPU miner along side the monitor-noncer-pro tool
