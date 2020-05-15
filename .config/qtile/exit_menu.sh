#!/bin/bash
. "${HOME}/.cache/wal/colors.sh"
while [ "$select" != "NO" -a "$select" != "YES" ]; do
	select=$(echo -e 'NO\nYES' | dmenu -nb "$color0" -nf "$color1" -sb "$color1" -sf "$color0" -fn '-*-*-medium-r-normal-*-*-*-*-*-*-100-*-*' -i -p "Back to the den? XD                                 ")
    [ -z "$select" ] && exit 0
done
[ "$select" = "NO" ] && exit 0
killall qtile 
