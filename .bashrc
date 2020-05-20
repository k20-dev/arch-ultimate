#
# ~/.bashrc
#

# //VI MODE BASH
	set -o vim

# //PYWAL SHIT
# Import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
cat ~/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
source ~/.cache/wal/colors-tty.sh

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# // ALIAS
alias ls='ls --color=auto'

# // PYWAL IDK
wal -r && clear

# // PS1 SHIT
BLACK=$(tput setaf 0)
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
LIME_YELLOW=$(tput setaf 190)
YELLOW=$(tput setaf 3)
POWDER_BLUE=$(tput setaf 153)
BLUE=$(tput setaf 4)
MAGENTA=$(tput setaf 5)
CYAN=$(tput setaf 6)
WHITE=$(tput setaf 7)
BRIGHT=$(tput bold)
NORMAL=$(tput sgr0)
BLINK=$(tput blink)
REVERSE=$(tput smso)
UNDERLINE=$(tput smul)

# PS1="\[${WHITE}\]\[${YELLOW}\]\u@\h\[${WHITE}\]\[${NORMAL}\] "

export PS1="\e[0;33;1m[\u@\h \W]\$ \e[m"
