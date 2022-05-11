#!/bin/sh

vid_path = ""
total_frame = 10
save_path = ""

pip install -r requirements.txt

python -m --vid_path ${vid_path} \\
          --total_frame ${total_frame} \\
          --save_path ${save_path}
