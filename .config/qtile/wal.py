import sys
import subprocess

def execute_program(process):
    subprocess.Popen(process.split())

#pywal colors load

execute_program('wal -i '+sys.argv[1])
execute_program('xrdb '+pywal_cache_path+'colors.Xresources') 
