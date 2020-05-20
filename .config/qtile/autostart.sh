#!/bin/sh
#
# COMPOSTER
compton & 
# WAL
wal -i /home/daniel19/media/wallpapers/background02.jpg -a 90 &
# KEYBOARD ES
setxkbmap -layout es &
# TOUCHPAD
synclient rightedge=2200 &
synclient ClickPad=1 &
synclient TapButton1=1 &
synclient MaxSpeed=1 &
synclient VertEdgeScroll=1 &
synclient HorizTwoFingerScroll=0 &
synclient VertTwoFingerScroll=0 &
synclient HorizEdgeScroll=1 &
synclient BottomEdge=300 &
