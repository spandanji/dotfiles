#!/bin/bash
. "${HOME}/.cache/wal/colors.sh"
scrot i3lock.png;
convert i3lock.png -blur 20x20 i3lock.png;
i3lock -i i3lock.png -k --insidecolor="$color4""aa" --ringcolor="$color1""ff" --insidewrongcolor="$color9""ff" --keyhlcolor="$color0""ff" --linecolor="$color2""ff" --timecolor="$color0""ff" --time-font="Roboto Mono Bold" --verifcolor="$color0""ff" --ringvercolor="$color5""ff" --insidevercolor="$color7""ff"
rm i3lock.png;
