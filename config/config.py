# -*- coding: utf-8 -*-

import os
import socket
import subprocess
from libqtile import backend, bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile.lazy import lazy
from typing import List  # noqa: F401o

mod = "mod4"
terminal = "konsole"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # Move windows up or down in current stack
    Key([mod,"shift", "control"], "k", lazy.layout.shuffle_down()),
    Key([mod,"shift", "control"], "j", lazy.layout.shuffle_up()),
    Key([mod,"shift", "control"], "h", lazy.layout.shuffle_left()),
    Key([mod,"shift", "control"], "l", lazy.layout.shuffle_right()),

    Key([mod], "n", lazy.layout.swap_column_left()), 
    Key([mod], "m", lazy.layout.swap_column_left()),

    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    # Key([mod], "Return", lazy.spawn("urxvt")),
    Key([mod], "Return", lazy.spawn("konsole")),
    Key([mod, "control"],"Return", lazy.spawn("cool-retro-term")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # CHROME
    Key([mod], "b", lazy.spawn("firefox")),

    # QUTEBROWSER
    Key([mod, "control"], "b", lazy.spawn("qutebrowser")),

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")), 

    
    Key([mod,"shift"],  "comma",  lazy.function("window_to_next_screen")),
    Key([mod,"shift"],  "period", lazy.function("window_to_previous_screen")),
    Key([mod,"control"],"comma",  lazy.function("window_to_next_screen, switch_screen=True")),
    Key([mod,"control"],"period", lazy.function("window_to_previous_screen, switch_screen=True")),
]

def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)


# TODO fix MUS layout && add music station there
group_names = [
    ("NET", {'layout': 'columns'}),
    ("DEV", {'layout': 'columns'}),
    ("SYS", {'layout': 'columns'}),
    ("CHAT", {'layout': 'columns'}),
    ("VBOX", {'layout': 'columns'}),
    ("MUS", {'layout': 'floating'}),
    ("VID", {'layout': 'columns'}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))


### DEFAULT COLOR SCHEME ### ]

colors = [
    ["#293136", "#293136"],  # color 0
    ["#3b4252", "#3b4252"],  # color 1
    ["#8c8c8c", "#8c8c8c"],  # color 2
    ["#565b78", "#565b78"],  # color 3
    ["#a1acff", "#a1acff"],  # color 4
    ["#ffffff", "#ffffff"],  # color 5
    ["#9293d2", "#9293d2"],  # color 6
    ["#89b8fd", "#89b8fd"],  # color 7
    ["#e2c5dc", "#e2c5dc"],  # color 8
    ["#0ee9af", "#0ee9af"],  # color 9
    ["#e9c46a", "#e9c46a"],  # color 10
    ["#4f76c7", "#4f76c7"],  # color 11
    ["#00ff32", "#00ff32"],  # color 12
    ["#90cda3", "#90cda3"],  # color 13
    ["#f39c12", "#f39c12"],  # color 14
    ["#2a2d2f", "#2a2d2f"],  # Color 15 = MATE BLACK
    ["#100016", "#100016"],  # Color 16 = DEEP PURPLE
    ["#8bf609", "#8bf609"],  # Color 17 = ACID GREEN
    ["#7eb980", "#7eb980"],  # Color 18 = LIME
]

### DEFAULT WIDGET SETTINGS ###
extension_widget_defaults = dict(
    font='Dejavu Serif',
    fontsize=12,
    padding=2,
    rounded=True,
    margin_y=4,
    margin_x=3,
    background=colors[0]
)

layouts = [
    layout.MonadTall(
        border_focus = colors[17],
        border_normal = colors[1],
        border_width=3,
        margin=15,
        border_on_single=True,
        margin_on_single=30,
    ),
    layout.Floating(
        border_focus = colors[17],
        border_normal = colors[14]
    ),
    layout.Columns(
        border_focus=colors[17],
        margin=15
),
    layout.Max()
]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

screens = [
    Screen(
        top=bar.Bar(
            background=colors[16],
            margin=[15, 15, 12, 15],
            size=25,
            opacity=0.9,
            widgets=[
                widget.Sep(
                    background=colors[16],
                    linewidth=0,
                    padding=16
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser(
                        "~/.config/qtile/icons")
                    ],
                    foreground=colors[1],
                    background=colors[14],
                    padding=5,
                    scale=0.7,
                    rounded=True
                ),
                widget.Sep(
                    background=colors[16],
                    linewidth=0,
                    padding=16
                ),
                widget.Sep(
                    linewidth=4,
                    padding=10,
                    foreground=colors[5],
                    background=colors[0]),
                widget.GroupBox(
                    font="iosevka bold",
                    fontsize=10,
                    margin_y=3,
                    margin_x=2,
                    padding_y=10,
                    padding_x=5,
                    borderwidth=4,
                    active=colors[14],
                    inactive=colors[18],
                    rounded=False,
                    highlight_color=colors[14],
                    highlight_method="block",
                    this_current_screen_border=colors[17],
                    this_screen_border=colors[16],
                    other_current_screen_border=colors[17],
                    other_screen_border=colors[16],
                    foreground=colors[18],
                    background=colors[16],
                ),
                widget.Sep(
                    linewidth=4,
                    padding=10,
                    foreground=colors[5],
                    background=colors[0]
                ),
                widget.Sep(
                linewidth=4,
                padding=10,
                foreground=colors[1],
                background=colors[16]
                ),
                widget.Prompt(
                    background=colors[3],
                    foreground=colors[5],
                    font="CaskaydiaCove Nerd Font Mono",
                    fontsize=14,
                ),
                widget.WindowName(
                    background=colors[16],
                    foreground=colors[17],
                    font="JetBrainsMono Nerd Font Mono",
                    fontsize=14,
                    padding=10
                ),
                widget.Sep(
                    padding=10,
                    linewidth=10,
                    background=colors[16],
                    foreground=colors[16],
                ),
                widget.Sep(
                    padding=10,
                    linewidth=2,
                    background=colors[16]
                ),
                widget.LaunchBar(
                    background= colors[14],
                    foreground= colors[16],
                    icon_size= 17,
                    padding_y=-2,
                    default_icon='/home/imperial/.config/qtile/icons/headphones.ico',
                    progs=[('pavucontrol','pavucontrol')]
                ),
                widget.Volume(
                    background=colors[14],
                    foreground = colors[16],
                ),
                widget.Sep(
                    padding=10,
                    linewidth=2,
                    background=colors[16]
                ),
                widget.CurrentLayout(
                    background=colors[14],
                    foreground = colors[16],
                    font="CaskaydiaCove Nerd Font Mono",
                    fontsize="14",
                    padding=10
                ),
                widget.CurrentLayoutIcon(
                    foreground = colors[16],
                    background=colors[14],
                    padding = 5,
                    scale = 0.8
                ),
                widget.Sep(
                    padding=10,
                    linewidth=2,
                    background=colors[16]
                ),
                widget.Clock(
                    font="CaskaydiaCove Nerd Font Mono",
                    foreground=colors[16],
                    background=colors[14],
                    fontsize=16,
                    padding=10,
                    format='%a  %d/%m | %I:%M %p',
                ),
                widget.Sep(
                    padding=10,
                    linewidth=0,
                    background=colors[16],
                    foreground=colors[16],
                )
            ],
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# @hook.subscribe.startup_once
# def startup():
#     Group("CHAT", spawn="slack")
#     Group("MUS", spawn="vlc")

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
