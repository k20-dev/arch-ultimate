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
#oh-my-posh --init --shell fish --config ~/.poshthemes/amro.omp.json | source
#oh-my-posh --init --shell fish --config ~/.poshthemes/catppuccin_mocha.omp.json | source
#oh-my-posh --init --shell fish --config ~/.poshthemes/lambdageneration.omp.json | source
oh-my-posh --init --shell fish --config ~/.poshthemes/hul10.omp.json | source


# ALIASES
# Routes : Go to directory
alias 	gh	   "cd ~/"
alias 	codes  "cd ~/code"

# Current project
alias	app  "cd ~/code/p5/p5-bezier"	 	
alias	chat "cd ~/code/reactjschat"

# Files  : Edit files
alias   lvimrc   "cat ~/.vimrc"
alias 	evimrc   "vim ~/.vimrc"
alias 	lfish  "cat ~/.config/fish/config.fish"
alias 	efish  "vim ~/.config/fish/config.fish"

# Git Token
alias 	gittoken "echo git push https://danielplata79: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@github.com/danielplata79/reactjschat"
# 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
# List Aliases

# SHORTCUTS
alias 	rr 	   "ranger" 

# Screens
alias d2off "xrandr --output DisplayPort-1 --off"
alias d2on "xrandr --output DisplayPort-1 --mode 1920x1080 --pos 2560x0 --rotate normal --gamma 0.85:0.85:0.85"
