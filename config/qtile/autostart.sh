#!/bin/sh
#xrandr --output HDMI-A-0 --primary &
#xrandr --output DisplayPort-0 --left-of HDMI-A-0 &
xrandr --output DisplayPort-0 --off --output DisplayPort-1 --mode 1920x1080 --pos 2560x0 --rotate normal --gamma 0.85:0.85:0.85 --output DisplayPort-2 --off --output HDMI-A-0 --primary --mode 2560x1440 --rate 99.97 --pos 0x0 --rotate normal --gamma 0.85:0.85:0.85 &
qtile cmd-obj -o cmd -f restart &
xbindkeys &
picom --config ~/.config/picom.conf &
wal -i /home/thre4t/Media/walls_1/4.png -a 80
