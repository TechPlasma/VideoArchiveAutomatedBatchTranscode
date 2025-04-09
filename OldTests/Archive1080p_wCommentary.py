import os
import subprocess

# Set the paths to HandBrakeCLI and the preset file
HB_CLI = ".\HandBrakeCLI.exe"
PRESET_FILE = "Archive1080p.json"

# Set the input and output directories
INPUT_DIR = ".\ToEncode"
OUTPUT_DIR = ".\Encoded"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Iterate over all MKV files in the input directory
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".mkv"):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, os.path.splitext(filename)[0] + ".mp4")
        print(f"Transcoding '{os.path.splitext(filename)[0]}'")
        
        # Build the HandBrakeCLI command
        command = [
            HB_CLI,
            "-i", input_path,
            "-o", output_path,
            "--preset-import-file", PRESET_FILE,
            "--preset", "Archive 1080p",
            
            "--audio", "1,1,3",
            "--aname", "Stereo,\"Surround 5.1\",Commentary",
            "--aencoder", "av_aac,ac3,av_aac",
            "--ab", "160,640,160",
            "--mixdown", "stereo,5point1,stereo",
        ]
        
        # Run the command
        subprocess.run(command)

print("Transcode Complete.")