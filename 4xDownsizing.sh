#!/bin/bash

input_root_dir="input_video"
output_dir="output_video"

for input_file in "$input_root_dir"/*.jpg; do
    base=$(basename "$input_file")
    filename="${base%.*}"
    
    output_file="$output_dir/$filename".jpg
    
    ffmpeg -i "$input_file" -vf "scale=iw/4:ih/4" -c:a copy "$output_file"
done

echo "downsizing complete"
