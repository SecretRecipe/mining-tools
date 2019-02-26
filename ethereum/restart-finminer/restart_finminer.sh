killall -9 finminer

sleep 2s

tmux kill-session -t eth

sleep 2s

tmux new -s eth 'cd /home/billy/Desktop/FinMiner-linux-2.2.5/ && ./finminer'
