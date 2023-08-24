#!/bin/bash

input_root_dir="3DPW"
output_dir="3DPW_noising"

mkdir -p "$output_dir"

for input_file in "$input_root_dir"/*.mp4; do
    base=$(basename "$input_file")
    filename="${base%.*}"
    
    output_file="$output_dir/$filename"_noising.mp4
    
    ffmpeg -i "$input_file" -vf "noise=alls=50:allf=t" -c:a copy "$output_file"
done

echo "noising complete"