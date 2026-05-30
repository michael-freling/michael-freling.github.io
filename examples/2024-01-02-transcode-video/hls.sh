#! /bin/bash

set -ex

SEGMENT_LENGTH=1 # 1 seconds

# profile options are recommended to be omitted: https://trac.ffmpeg.org/wiki/Encode/H.264#Profile
ffmpeg -i animation_with_audio.mkv \
    -c:v libx264 \
    -hls_time $SEGMENT_LENGTH \
    -hls_playlist_type vod \
    -hls_segment_type fmp4 \
    -b:v:0 8M -r:v:0 30 -bufsize 8M \
    -b:v:1 2.5M -r:v:1 24 -bufsize 2.5M \
    -b:a:0 384k \
    -b:a:1 128k \
    -map 0:v -map 0:a -map 0:v -map 0:a -var_stream_map "v:0,a:0,name:1080p v:1,a:1,name:480p" \
    -master_pl_name 'playlist.m3u8' \
    'public/animation_with_audio/playlist_segment_%v.m3u8'

ffmpeg -i animation_without_audio.mkv \
    -c:v libx264 \
    -hls_time $SEGMENT_LENGTH \
    -hls_playlist_type vod \
    -hls_segment_type fmp4 \
    -b:v:0 8M -r:v:0 30 -bufsize 8M \
    -b:v:1 2.5M -r:v:1 24 -bufsize 2.5M \
    -map 0:v -map 0:v -var_stream_map "v:0,name:1080p v:1,name:480p" \
    -master_pl_name 'playlist.m3u8' \
    'public/animation_without_audio/playlist_segment_%v.m3u8'


INPUT=${1:-animation_with_audio.mkv}

# Check a video contains an audio
AUDIO_CODEC_NAME=$(ffprobe -i $INPUT -select_streams a -v error -show_entries stream=codec_name -of json | jq -r '.streams[0].codec_name // empty')

if [ "$AUDIO_CODEC_NAME" = "" ]; then
    echo "$INPUT has no audio"
else
    echo "$INPUT has audio stream $AUDIO_CODEC_NAME"
fi
