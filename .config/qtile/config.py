#
#   Qtile Configuration : Spandan Ghosh
#
#
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
import json,subprocess,os
from typing import List  

mod = "mod4"

config_path = os.path.expanduser('~/.config/qtile/')
pywal_cache_path = os.path.expanduser('~/.cache/wal/')
wallpaper=os.path.expanduser('~/.config/qtile/wallpapers/deku.jpg')

def execute_program(process):
    subprocess.Popen(process.split())

#pywal colors load
 
def getcolorvars(path):
    d={}
    with open(path+"colors.json") as f:
        d = json.load(f)
    return d

pywaldict = getcolorvars(pywal_cache_path)



#Hooks

@hook.subscribe.startup_once
def autostart_once():
    execute_program('picom -f ')
    execute_program('wal -i '+wallpaper)
    execute_program('xrdb '+pywal_cache_path+'colors.Xresources')
    execute_program('nm-applet &')
    execute_program('pa-applet &')
    execute_program('clipmenud')
    
@hook.subscribe.startup
def autostart():
    #execute_program('picom -f ')
    #execute_program('wal -i '+wallpaper)
    #execute_program('xrdb '+pywal_cache_path+'colors.Xresources')
    #execute_program('clipmenud')
    pass


#Key bindings

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", 
        lazy.layout.down()),
    
    Key([mod], "j", 
        lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", 
        lazy.layout.shuffle_down()),

    Key([mod, "control"], "j", 
        lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", 
        lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", 
        lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", 
        lazy.layout.toggle_split()),
    
    Key([mod], "Return", 
        lazy.spawn("st")),

    Key([mod], "d", 
        lazy.spawn(config_path+'dmenu_run_history -nb "'+pywaldict["colors"]["color0"]+'" -nf "'+pywaldict["colors"]["color15"]+'" -sb "'+pywaldict["colors"]["color1"]+'" -sf "'+pywaldict["colors"]["color0"]+'"')),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", 
        lazy.next_layout()),
    
    Key([mod], "w", 
        lazy.window.kill()),

    Key([mod, "control"], "r", 
        lazy.restart()),

    Key([mod, "control"], "q", 
        lazy.spawn(config_path+'exit_menu.sh')), #lazy.shutdown()),
    
    Key([mod, "control"], "x", 
        lazy.spawn(config_path+'lock.sh')), 

    Key([mod], "r",
        lazy.spawncmd()),

    Key([mod, "shift"], "q",
            lazy.window.kill()),


    Key([mod], "f",
            lazy.window.toggle_fullscreen()),


    Key([mod, "shift"], "f",
            lazy.window.toggle_floating()),

    Key([mod, "shift"], "p",
            lazy.spawn("python "+config_path+"wal.py "+wallpaper)),
   
   Key([], "XF86AudioRaiseVolume",
           lazy.spawn("pactl set-sink-volume 0 +5%")),

   Key([], "XF86AudioLowerVolume",
           lazy.spawn("pactl set-sink-volume 0 -5%")),

   Key([], "XF86AudioMute",
           lazy.spawn("pactl set-sink-mute 0 toggle")),

   Key([], "XF86MonBrightnessUp",
           lazy.spawn("light -A 5")),


   Key([], "XF86MonBrightnessDown",
           lazy.spawn("light -U 5")),

   ]

groups = [Group(i) for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]

for i in groups:

    keys.extend([
        # mod1 + letter of group = switch to group
    
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
])

layouts = [

    layout.Columns(
        border_width=4,
        margin=10),
    
    layout.MonadTall(),
    
    layout.Columns(
        margin=20,
        name="moregaps"),
    
    layout.Tile(),
    
    layout.Max(),
    
    layout.Stack(
        num_stacks=2
        ),

    layout.Bsp(),
    
    # layout.Matrix(),
    # layout.MonadWide(),
    
    layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Roboto Mono Bold',
    fontsize=12,
    padding=5,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [   
                widget.Sep(
                    padding=6,
                    fontcolor= pywaldict['special']['background']
                    ),

                widget.GroupBox(
                    highlight_method='block',
                    disable_drag=True,
                    padding=3,
                    font = "Roboto Mono Bold",
                    inactive = pywaldict["colors"]["color1"],
                    active = pywaldict["special"]["foreground"],
                    foreground = pywaldict["colors"]["color1"],
                    this_current_screen_border=  pywaldict["colors"]["color1"],
                    ),
                widget.Prompt(),
                widget.Sep(
                    padding=20
                    ),
                widget.CPU(
                    background= pywaldict["colors"]["color6"],
                    foreground= pywaldict["colors"]["color0"]
                    ),
                #widget.CPUGraph(),
                widget.Sep(
                    padding=20
                    ),
                widget.Net(
                    interface='wlp60s0',
                    format='🌍:{down} ↓↑ {up}',
                    background= pywaldict["colors"]["color6"],
                    foreground= pywaldict["colors"]["color0"]
                    ),

#                widget.NetGraph(
#                    interface='wlp60s0'
#                    #fill_color=pywaldict["colors"]["color1"]+".3",
#                  ),
                widget.Sep(
                    padding=20
                    ),

                widget.WindowName(
                    foreground=pywaldict["colors"]["color5"],
                    ),
                widget.Systray(),
                widget.Backlight( 
                    background = pywaldict["colors"]["color6"],
                    foreground = pywaldict["special"]["background"],
                    backlight_name="intel_backlight",
                    fmt="Bri:{}",
                    ),
                widget.Battery(
                    background = pywaldict["colors"]["color5"],
                    foreground = pywaldict["special"]["background"],
                    fmt="BAT:{}",
                    ),
                widget.Volume(
                    background = pywaldict["colors"]["color4"],
                    foreground = pywaldict["special"]["background"],
                    fmt="Vol:{}",
                    ),
                widget.CapsNumLockIndicator(
                    background = pywaldict["colors"]["color3"],
                    foreground = pywaldict["special"]["background"],
                    ),
                widget.Pacman(
                    background = pywaldict["colors"]["color2"],
                    foreground = pywaldict["special"]["background"],
                    fmt="Updates:{}",
                    font = "Roboto Mono Bold",
                    fontsize = 12,
                    padding = 10,
                    ),
                widget.Clock(
                    background=pywaldict["colors"]["color3"],
                    foreground=pywaldict["special"]["background"],
                    format='%d-%m-%Y %a %I:%M %p',
                    font="Roboto Mono Bold",
                    padding=10,),

                widget.CurrentLayout(
                    background=pywaldict["colors"]["color1"],
                    foreground=pywaldict["special"]["background"],
                    padding=10),

                widget.CurrentLayoutIcon(
                    background=pywaldict["colors"]["color1"],
                    foreground=pywaldict["colors"]["color0"],
                    padding=5
                    ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("default config", name="default"),
                #widget.QuickExit(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
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
wmname = "qtile"
