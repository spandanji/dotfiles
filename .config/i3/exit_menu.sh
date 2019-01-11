while [ "$select" != "NO" -a "$select" != "YES" ]; do
    select=$(echo -e '          NO              \n            YES             ' | dmenu -nb '#151515' -nf '#999999' -sb '#f00060' -sf '#000000' -fn '-*-*-medium-r-normal-*-*-*-*-*-*-100-*-*' -i -p "Sure you wanna leave? xD ")
    [ -z "$select" ] && exit 0
done
[ "$select" = "NO" ] && exit 0
i3-msg exit
