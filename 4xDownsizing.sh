#!/bin/bash

input_root_dir="output_video"
output_dir="4xdownsizing_video"

for input_file in "$input_root_dir"/*.mp4; do
    base=$(basename "$input_file")
    filename="${base%.*}"
    
    output_file="$output_dir/$filename"_4xDownsized.mp4
    
    ffmpeg -i "$input_file" -vf "scale=iw/4:ih/4" -c:a copy "$output_file"
done

echo "downsizing complete"