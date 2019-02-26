killall -9 finminer

sleep 2s

tmux kill-session -t tmux-eth

sleep 2s

tmux new -s tmux-eth 'cd <path_to_finminer_directory> && ./finminer'
