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
    Key([mod, "control"],"Return", lazy.spawn("cool-retro-term")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # CHROME
    Key([mod], "b", lazy.spawn("google-chrome-stable")),

    # QUTEBROWSER
    Key([mod, "control"], "b", lazy.spawn("qutebrowser")),

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
    "black": ["#24242A", "#24242A"],
    "cian": ["349c9c", "349c9c"],
    "pink900": ["#880E4F", "#880E4F"],
    "red": ["#B71C1C", "#B71C1C"]
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
        margin_y = 5,
        margin_x = 0,
        padding_y = 20,
        padding_x = 5,
        borderwidth = 1,
        active = colors["white"],
        inactive = colors["white"],
        rounded = False,
        highlight_method = "block",
        this_current_screen_border = colors["red"],
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
    widget.WindowName(font="FiraCode",
        fontsize = 11,
        foreground = colors["cian"],
        background = colors["dark"],
        padding = 5
    ),
    widget.Prompt(
        cursor = True,
        cursorblink = 0.5,
        background = colors["red"]
        ), 
    widget.Systray(
        background = colors["cian"],
        padding = 1 
    ), 
    widget.Battery(
       format = "{char} {percent:2.0%}",
       background = colors["cian"]
        ), 
    widget.CurrentLayout(
        foreground = colors["white"],
        background = colors["pink900"],
        padding = 5
    ),
    widget.Clock(
        foreground = colors["white"],
        background = colors["cian"],
        format = "%A, %B %d - %H:%M"
    ),
]

groups = [Group(i) for i in ["NET", "DEV", "TERM", "MEDIA", "EXTRA 1", "EXTRA 2"]]

for i in range(len(groups)):
    actual_key = i + 1
    keys.extend([
        Key([mod], str(actual_key), lazy.group[groups[i].name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(actual_key), lazy.window.togroup(groups[i].name)),
    ])

layouts = [
    layout.MonadTall(border_width= 2, margin= 15, border_focus = colors ["cian"][0]),
    layout.Max(),
    layout.Floating(),
    # layout.Matrix(border_width= 3, border_focus = colors ["blue"][0]),
    layout.MonadWide(border_width= 2,margin= 15, border_focus = colors ["blue"][0])
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

wmname = "LG3D"
