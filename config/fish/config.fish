#	# # # # # # # # # # # # # # #
#	# DP - CUSTOM FISH TERMINAL #
#	# # # # # # # # # # # # # # # 
#
#	⣶⣿⣾⣷⣷⣾⣿⣿⣿⠋⠀⠀⠀⢠⣾⣿⣿⣿⣶⣤⣤⡀⠀⠀⢀⠀⢹⣿⣿
#	⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣷⣸⣿⣿
#	⣿⣿⣿⣿⣿⣿⡿⡟⠀⠀⠀⠀⢿⣿⣿⣿⢷⣿⣿⣿⣿⣿⣿⣿⠿⠁⠃⣿⣿
#	⣿⣿⣿⣿⣿⣿⡄⡘⣤⠀⢀⣾⣿⣻⡿⢿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⣿⣿
#	⣿⣿⣿⣿⣿⣿⣿⡉⣩⠀⣦⡙⠟⠟⠛⢓⠀⠙⢿⣿⣿⣿⣿⡧⠀⠀⣾⣿⣿
#	⣿⣿⣿⣿⣿⣿⢿⣯⣿⢸⣿⣷⡗⠀⠀⠁⠒⠠⢀⢰⡿⠻⠼⠓⠂⠘⢿⣿⣿
#	⣻⣿⡟⣯⣿⢋⣯⡟⣿⠏⠿⣿⣧⠀⠀⠀⠀⠀⠀⣨⡇⠀⠀⠀⠀⠀⣈⣿⣿
#	⣿⣿⠿⣟⣻⣿⣿⣇⡟⡀⠀⣹⣿⣷⣦⣤⣤⣦⣾⣿⠇⠀⠀⠀⠀⢀⣾⣿⣿
#	⣿⠃⠐⢩⣿⣿⢟⠟⠃⠀⠀⢸⣿⣿⣿⣿⡟⠿⢿⣿⡄⢰⡆⠀⢀⣿⣿⣿⣿
#	⡏⡄⠀⠀⢻⡁⠀⠀⠀⠀⠐⠅⢻⣿⣿⣿⣿⣶⡄⠀⠀⠀⠁⢀⣾⣿⣿⣿⣿
#	⠔⠀⠀⠀⠈⢟⢄⠀⠀⠀⠀⠈⠘⠛⢷⡄⠀⠭⠉⠁⠀⠀⢠⣾⣿⣿⣿⣿⣿
#	⢵⠀⠀⠀⠀⠈⢉⣦⠀⠀⠀⠀⠀⢱⣶⣿⣶⣶⡄⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿
#	⢀⡐⠀⠀⠀⠀⠈⢼⢅⠀⠀⠀⠀⠀⠈⠉⠛⠛⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿
#	⠐⠀⠠⡀⠀⠀⠀⠈⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠉⠉⠉⠙⠻⠿⠿⣿
#	⠓⠄⡀⠈⠢⠀⠀⠐⢤⣄⡀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠣⡄⠀⠀⠀⠀⠀⠀

# Initialize Oh-My-Posh
#oh-my-posh --init --shell fish --config ~/.poshthemes/plague.omp.json | source
#oh-my-posh --init --shell fish --config ~/.poshthemes/atomicBit.omp.json | source
#oh-my-posh init fish | source
oh-my-posh --init --shell fish --config ~/.poshthemes/sonicboom_light.omp.json | source


# ALIASES
# Routes : Go to directory
alias 	gh	   "cd ~/"
alias 	codes  "cd ~/code"

# Current project
alias	app		"cd ~/code/p5/p5-bezier"	 	
alias	chat            "cd ~/code/reactjschat"	 	

# Files  : Edit files
alias   lvimrc   "cat ~/.vimrc"
alias 	evimrc   "nvim ~/.vimrc"
alias 	lfish  "cat ~/.config/fish/config.fish"
alias 	efish  "nvim ~/.config/fish/config.fish"

# Git Token
alias 	gittoken "echo git push https://danielplata79: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@github.com/danielplata79/reactjschat"
# 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

# List Aliases

# SHORTCUTS
alias 	rr 	   "ranger" 

# Display
#alias d2on "xrandr --output DisplayPort-1 --mode 1920x1080 --pos 2560x0 --rotate normal --gamma 0.85:0.85:0.85 && qtile cmd-obj -o cmd -f restart && wal -i (cat ~/.cache/wal/wal) -a 80"

alias d2on "xrandr --output DisplayPort-1 --mode 1920x1080 --pos 2560x0 --rotate normal --gamma 0.85:0.85:0.85 --rate 60.00 --output HDMI-A-0 --primary --mode 2560x1440 --rate 99.97 --pos 0x0 --rotate normal --gamma 0.75:0.75:0.75 && wal -i (cat ~/.cache/wal/wal) -a 80 && qtile cmd-obj -o cmd -f restart"

alias d3 "xrandr --output HDMI-A-0 --primary --mode 2560x1440 --rate 99.97 --pos 0x0 --rotate normal --gamma 0.60:0.60:0.60"


alias d2off "xrandr --output DisplayPort-1 --off"
