import os
import subprocess
import inquirer
import winsound

# Set the paths to HandBrakeCLI and the preset file
HB_CLI = "./HandBrakeCLI.exe"

COMPLETION_TONE = [
  (587, 150),  # D5
  (784, 500)   # G5 (longer final note)
]

# Presets
PRESET_BR1080p = "./Archive1080pV2.json"        # BR Rip Standard Output
PRESET_BR1080pRA = "./Archive1080pV2_RA.json"   # Reduced audio languages, and codacs
PRESET_BR4k = "./Archive4k.json"                # 4kBR Rip
PRESET_BR4kRA = "./Archive4k_RA.json"           # 4kBR Rip Reduced audio languages, and codacs

questions = [
  inquirer.List(
    "mode",
    message="Which Preset should be used?",
    choices=[
      "BR 1080p Reduced Audio/Subtitles", 
      "BR 4k HDR Reduced Audio/Subtitles",
      "BR 1080p", 
      "BR 4k HDR",
    ]
  ),
]
answers = inquirer.prompt(questions)

match answers['mode']:
  case "BR 1080p":
    PRESET_FILE = PRESET_BR1080p
    PRESET_NAME = "Archive 1080p"
    PRESET_CONTAINER = ".mkv"
  case "BR 1080p Reduced Audio/Subtitles":
    PRESET_FILE = PRESET_BR1080pRA
    PRESET_NAME = "Archive 1080p"
    PRESET_CONTAINER = ".mkv"
  case "BR 4k HDR":
    PRESET_FILE = PRESET_BR4k
    PRESET_NAME = "Archive 4k HDR"
    PRESET_CONTAINER = ".mkv"
  case "BR 4k HDR Reduced Audio/Subtitles":
    PRESET_FILE = PRESET_BR4kRA
    PRESET_NAME = "Archive 4k HDR"
    PRESET_CONTAINER = ".mkv"

# Set the input and output directories
INPUT_DIR = "./ToEncode"
OUTPUT_DIR = "./Encoded"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Iterate over all MKV files in the input directory
for filename in os.listdir(INPUT_DIR):
  if filename.endswith(".mkv"):
    input_path = os.path.join(INPUT_DIR, filename)
    output_path = os.path.join(OUTPUT_DIR, os.path.splitext(filename)[0] + PRESET_CONTAINER)
    print(f"Transcoding '{os.path.splitext(filename)[0]}'")
    
    # Build the HandBrakeCLI command
    command = [
      HB_CLI,
      "-i", input_path,
      "-o", output_path,
      "--preset-import-file", PRESET_FILE,
      "--preset", PRESET_NAME,
    ]
    
    # Run the command
    subprocess.run(command)


# Notifiy the user that the transcoding is complete
for freq, duration in COMPLETION_TONE:
  winsound.Beep(freq, duration)
print("Transcode Complete.")