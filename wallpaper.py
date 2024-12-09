#!/usr/bin/env python3  
import os


wallpaper = "/home/mantodea/Downloads/forest1.jpg" 
desktop_monitor = os.system(f"xwallpaper --zoom {wallpaper} --output eDP-1")
laptop_monitor = os.system(f"xwallpaper --zoom {wallpaper} --output HDMI-1-0")
