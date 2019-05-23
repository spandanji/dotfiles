pactl set-sink-volume 0 +5%;
x=$(pamixer --get-volume);
echo $x;
if [ $x -gt 100 ]
then
    volnoti-show 100;
else
    volnoti-show $x;
fi
