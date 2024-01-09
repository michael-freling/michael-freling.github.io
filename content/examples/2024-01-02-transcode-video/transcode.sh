#! /bin/bash

set -ex

INPUT=${1:-animation_with_audio.mkv}

ffmpeg -i $INPUT \
    -c:v libx264 \
    -c:a aac \
    -f dash \
    -dash_segment_type mp4 \
    -seg_duration 4 \
    -init_seg_name init\$RepresentationID\$.\$ext\$ \
    -media_seg_name segment\$RepresentationID\$-\$Number%05d\$.\$ext\$ \
    -hls_playlist true \
    -hls_master_name 'playlist.m3u8' \
    public/output/output.mpd
