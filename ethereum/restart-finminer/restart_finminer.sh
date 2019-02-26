killall -9 finminer

sleep 2s

tmux kill-session -t eth

sleep 2s

tmux new -s eth 'cd <path_to_finminer_directory> && ./finminer'
