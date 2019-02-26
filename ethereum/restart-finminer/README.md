# restart-finminer
This is a simple bash script that restarts FinMiner to prevent it from crashing. The script assumes you run FinMiner in a tmux session named `tmux-eth`:
- Kills all processes named `finminer`
- Kills the tmux session named `tmux-eth`
- Creates a new tmux session named `tmux-eth`
- In the `tmux-eth` session, it changes directory to <path_to_finminer_directory> (be sure to change this to your FinMiner directory, not including the FinMiner file itself)
- In the `tmux-eth` session, it runs ./finminer

### Usage
- Change the last line so that it `cd`s to your FinMiner directory, making sure that you don't include the actual FinMiner file itself in the path.
- `chmod +X ./restart_finminer.sh` to make it executable
- `./restart_finminer.sh` to run the file.
