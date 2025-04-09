# Video Archive Automated Batch Transcode

This is just a dumbish command-line system I built to automate my transcoding
of MKV files. It could probably be done via Handbrake itself now that the 
Presets are built, but this is a workflow I like.

In my experiences with this, I realized that converting to `.mp4` was a lost
cause. And decided to just re-transcode to `.mkv`. This was to preserve multiple
subtitle tracks found when backing up my videos.

These prests are focused on a pretty-good quality NVENC encode that runs on my
4070ti gpu. Encoding time is roughly 300ish FPS for 1080p and 60ish FPS for 4k.
File sizes are approximately 1/3 their original size. Which I think is a fair
tradeoff in Size/Quality.

## Installation
Make sure you have Python 3 installed.

You will also need to install the python packages:
- [inquirer] (https://pypi.org/project/inquirer/)

## Usage
To start you need to make sure that there are two folders:
- `ToEncode` - This is where you put the files to encode
- `Encoded` - This is where the encoded files are output

To start an encode run:
> python3 ./ArchiveBR.py

Then select a preset to use. They are ordered by most commonly used.

### Presets
There are two major presets, One for 1080p and one for 4k. Both have a version
that offers a COMPLETE pass-through of audio and subtitle tracks. Which is useful
if you want to include ALL the extra bits, at the cost of end-file-size.

The 4K encoder will try to preserve HDR content in it's encode, granted I don't
have a GREAT way to verify that it's working correctly, but it seems to kinda 
be working...

There is also a Reduced Audio/Subtitle option for both, which will only keep the
languages [English, Spanish, Japanese] this is purely preference for my household
and our known languages so modify to taste. It will also strip out all the `MA`
audio tracks, these are the fully uncompressed audio tracks that are highest quality but
tend to bloat the files. 
