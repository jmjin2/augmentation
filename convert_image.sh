#!/bin/bash

input_root_dir="imageFiles"
output_dir="output_video"

for subdir in "$input_root_dir"/*; do
    if [[ -d "$subdir" ]]; then
        dir_name=$(basename "$subdir")
        output_file="${output_dir}/output_${dir_name}.mp4"
        
        mkdir -p "$output_dir"
        
        ffmpeg -framerate 30 -i "${subdir}/image_%05d".jpg -c:v libx264 -r 30 "$output_file"
        
        echo "Converted ${dir_name} images to video."
    fi
done

echo "Conversion complete."

