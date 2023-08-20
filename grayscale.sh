#!/bin/bash

input_root_dir="3DPW"
output_dir="3DPW_grayscale"

mkdir -p "$output_dir"

for input_file in "$input_root_dir"/*.mp4; do
    base=$(basename "$input_file")
    filename="${base%.*}"
    
    output_file="$output_dir/$filename"_grayscale.mp4
    
    ffmpeg -i "$input_file" -vf "hue=s=0" -c:a copy "$output_file"
done

echo "grayscale complete"