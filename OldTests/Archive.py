import os
import subprocess

# Set the paths to HandBrakeCLI and the preset file
HB_CLI = "./HandBrakeCLI.exe"
# PRESET_FILE = ".\Archive1080p.json"

# Set the input and output directories
INPUT_DIR = "../ToEncode"
OUTPUT_DIR = "../Encoded"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Iterate over all MKV files in the input directory
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".mkv"):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, os.path.splitext(filename)[0] + ".mkv")
        print(f"Transcoding '{os.path.splitext(filename)[0]}'")
        
        # Build the HandBrakeCLI command
        command = [
            HB_CLI,
            "-i", input_path,
            "-o", output_path,
            # "--preset-import-file", PRESET_FILE,
            "--preset", "H.265 NVENC 1080p",

            # Video Settings
            "--encoder", "nvenc_h265_10bit",
            "--quality", "20",
            "--vfr",
            "--width", "1920",
            "--height", "1080",
            "--crop",
            
            # Audio Settings
            "--audio-lang-list", "all",
            "--all-audio",
            "--aencoder", "copy",

            # Subtitle Settings
            "--subtitle-lang-list", "all",
            "--all-subtitles",
            "--subtitle-burned", "none",
            "--subtitle-default", "none",
            "--subtitle-force", "0"
        ]
        
        # Run the command
        subprocess.run(command)

print("Transcode Complete.")