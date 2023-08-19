#!/bin/bash

input_root_dir="output_video"
output_dir="vflipped_video"

mkdir -p "$output_dir"

for input_file in "$input_root_dir"/*.mp4; do
    base=$(basename "$input_file")
    filename="${base%.*}"
    
    output_file="$output_dir/$filename"_vflipped.mp4
    
    ffmpeg -i "$input_file" -vf "vflip" -c:a copy "$output_file"
done

echo "flipping complete"