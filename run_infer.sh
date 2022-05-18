#!/bin/sh

vid_path="test.mp4"
total_frame=3

pip install -r requirements.txt
pip install --upgrade google-cloud-vision
mkdir meta_data
mkdir result

python -m Infer.inference --vid_path ${vid_path} --total_frame ${total_frame}