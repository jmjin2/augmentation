#!/bin/bash

input_root_dir="output_video"
output_dir="hflipped_video"

mkdir -p "$output_dir"

for input_file in "$input_root_dir"/*.mp4; do
    base=$(basename "$input_file")
    filename="${base%.*}"
    
    output_file="$output_dir/$filename"_hflipped.mp4
    
    ffmpeg -i "$input_file" -vf "hflip" -c:a copy "$output_file"
done

echo "flipping complete"