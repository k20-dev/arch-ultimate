#!/bin/sh
xrandr --output HDMI-A-0 --primary &
xrandr --output DisplayPort-0 --right-of HDMI-A-0 &
xbindkeys &
picom &
wal -i /home/imperial/media/walls/bg5.png -a 80
