#!/bin/bash

input_root_dir="output_video"
output_dir="rotation_video"

mkdir -p "rotation_video"

for input_file in "$input_root_dir"/*.mp4; do
    base=$(basename "$input_file")
    filename="${base%.*}"
    
    output_file="$output_dir/$filename"_rotated.mp4
    
    ffmpeg -i "$input_file" -vf "transpose=1" -c:a copy "$output_file"
done

echo "rotate complete"