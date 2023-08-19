#!/bin/bash

input_root_dir="output_video"
output_dir="2xDownsizing_video"

for input_file in "$input_root_dir"/*.mp4; do
    base=$(basename "$input_file")
    filename="${base%.*}"
    
    output_file="$output_dir/$filename"_2xDownsized.mp4
    
    ffmpeg -i "$input_file" -vf "scale=iw/2:ih/2" -c:a copy "$output_file"
done

echo "downsizing complete"