# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget
from libqtile import hook
import os
import subprocess

mod = "mod4"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("urxvt")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # FIREFOX 
    Key([mod], "b", lazy.spawn("firefox")),

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")), 

]

colors = {
    "orange": ["#d84800", "#d84800"],
    "green":  ["#1B5E20", "#1B5E20"],
    "dark":  ["#282a36", "#282a36"],
    "grey":  ["#434758", "#434758"],
    "white": ["#ffffff", "#ffffff"],
    "pink":  ["#A77AC4", "#A77AC4"],
    "blue":  ["#7197E7", "#7197E7"],
    "darkblue": ["#3F51B5", "#3F51B5"],
    "black": ["#24242A", "#24242A"]
}

widgets_list = [
    widget.Sep(
        linewidth = 0,
        padding = 6,
        foreground = colors["white"],
        background = colors["dark"]
    ),
    widget.GroupBox(
        font = "Ubuntu Bold",
        fontsize = 9,
        margin_y = 0,
        margin_x = 0,
        padding_y = 9,
        padding_x = 5,
        borderwidth = 1,
        active = colors["white"],
        inactive = colors["white"],
        rounded = False,
        highlight_method = "block",
        this_current_screen_border = colors["orange"],
        this_screen_border = colors ["grey"],
        other_current_screen_border = colors["dark"],
        other_screen_border = colors["dark"],
        foreground = colors["white"],
        background = colors["dark"]
    ),
    widget.Sep(
        linewidth = 0,
        padding = 10,
        foreground = colors["white"],
        background = colors["dark"]
    ),
    widget.WindowName(font="Ubuntu",
        fontsize = 11,
        foreground = colors["orange"],
        background = colors["dark"],
        padding = 5
    ),
    widget.Prompt(), 
    widget.Systray(
        background = colors["dark"],
        padding = 1 
    ),
    widget.Sep(
        linewidth = 0,
        padding = 5,
        foreground = colors["white"],
        background = colors["dark"]
    ),
    widget.TextBox(
        font="Ubuntu Bold",
        text=" ⟳",
        padding = 5,
        foreground=colors["white"],
        background=colors["darkblue"],
        fontsize=14
    ),
    widget.Pacman(
        execute = "vlc",
        update_interval = 1800,
        foreground = colors["white"],
        background = colors["darkblue"]
    ),
    widget.TextBox(
        text=" ↯",
        foreground=colors["white"],
        background=colors["green"],
        padding = 10,
        fontsize=14
    ),
    widget.TextBox(
        font = "Ubuntu Bold",
        text = " ☵",
        padding = 1,
        foreground = colors["white"],
        background = colors["darkblue"],
        fontsize = 14
    ),
    widget.CurrentLayout(
        foreground = colors["white"],
        background = colors["darkblue"],
        padding = 5
    ),
    widget.TextBox(
        font = "Ubuntu Bold",
        text = " 🕒",
        foreground = colors["white"],
        background = colors["orange"],
        padding = 5,
        fontsize = 14
    ),
    widget.Clock(
        foreground = colors["white"],
        background = colors["orange"],
        format = "%A, %B %d - %H:%M"
    ),
]

groups = [Group(i) for i in ["NET", "DEV", "TERM", "MEDIA", "EXTRA 1", "EXTRA 2"]]

#for i in groups:
#    keys.extend([
#        # mod1 + letter of group = switch to group
#        Key([mod], i.name, lazy.group[i.name].toscreen()),
#
        # mod1 + shift + letter of group = switch to & move focused window to group
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
#    ])

for i in range(len(groups)):
    actual_key = i + 1
    keys.extend([
        Key([mod], str(actual_key), lazy.group[groups[i].name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(actual_key), lazy.window.togroup(groups[i].name)),
    ])

layouts = [
    layout.MonadTall(border_width= 2, margin= 20, border_focus = colors ["blue"][0]),
    layout.Max(),
    layout.Floating()
]
    
widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            widgets_list,
            24,
            opacity=0.95
        ),
    ),
    Screen(
            
    ),
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
