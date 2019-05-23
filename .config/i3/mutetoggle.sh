x=$(pamixer --get-mute)


if [ "$x" = "false" ]
then
    pamixer -m
    volnoti-show -m
else 
    vol=$(pamixer --get-volume);
    pamixer -u
    volnoti-show $vol  
fi