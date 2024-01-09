---
title: Investigate to transcode a video for a video on demand streaming by ffmpeg
date: 2024-01-08
draft: false
tags:
  - transcode
  - on-demand streaming
  - ffmpeg
  - adaptive bitrate streaming
  - hls
---


> **_NOTE:_**: This was written using ffmpeg version 4.4.2-0ubuntu0.22.04.1, and it's not been used on the production environment.

In this article, the video 

<video id="video" class="video-js vjs-default-skin" controls>
    <source src="/posts/2024/01/08/investigate-to-transcode-a-video-for-a-video-on-demand-streaming-by-ffmpeg/videos/playlist.m3u8" type="application/x-mpegURL" />
    Your browser does not support the video tag.
</video>

The audio in the above video was from [Beauteous of AlexiAction](https://pixabay.com/music/future-bass-beauteous-upbeat-electronic-162757/) in the Pixabay.


This article doesn't go into many topics for transcoding like

- Encryption of segments
- DRM (Digital Rights Management)

# tl;dr

The below commands transcode videos for the following qualities for streaming,

- 2.5M bps for 24 fps, which is for 480p video
- 8M bps for 30 fps, which is for 1080p video

For a video file with an audio,

```bash
INPUT_VIDEO_FILE=animation_with_audio.mkv

ffmpeg -i $INPUT_VIDEO_FILE \
    -c:v libx264 \
    -hls_time 6 \
    -hls_playlist_type vod \
    -hls_segment_type fmp4 \
    -b:v:0 8M -r:v:0 30 -bufsize 8M \
    -b:v:1 2.5M -r:v:1 24 -bufsize 2.5M \
    -b:a:0 384k \
    -b:a:1 128k \
    -map 0:v -map 0:a -map 0:v -map 0:a -var_stream_map "v:0,a:0,name:1080p v:1,a:1,name:480p" \
    -master_pl_name 'playlist.m3u8' \
    'public/animation_with_audio/playlist_segment_%v.m3u8'
```

For a video file without an audio,

```bash
INPUT_VIDEO_FILE=animation_without_audio.mkv

ffmpeg -i $INPUT_VIDEO_FILE \
    -c:v libx264 \
    -hls_time $SEGMENT_LENGTH \
    -hls_playlist_type vod \
    -hls_segment_type fmp4 \
    -b:v:0 8M -r:v:0 30 -bufsize 8M \
    -b:v:1 2.5M -r:v:1 24 -bufsize 2.5M \
    -map 0:v -map 0:v -var_stream_map "v:0,name:1080p v:1,name:480p" \
    -master_pl_name 'playlist.m3u8' \
    'public/animation_without_audio/playlist_segment_%v.m3u8'
```


# How Video on Demand works?

To develop a video-on-demand streaming, `transcoding` is used to convert the video into a suitable format of streaming.
in this article, transcoding is used for 2 purposes: encoding and fragmenting.

`Fragmenting` is used to achieve `Adaptive bitrate streaming`, which is essential for seamless video streaming experiences without buffering videos yet as high quality as possible.

At first, I'll explain about `Adaptive bitrate streaming` and then encoding to achieve the adaptive bitrate streaming.

## Adaptive bitrate streaming

Adaptive bitrate streaming is a way to improve streaming on HTTP. With this, viewers can watch a video without waiting to load an entire video and they can play the video with the highest quality as much as possible without buffering considering the network bandwidth and device type [[1]](#1).

In order to implement adaptive bitrate streaming, a video file is transcoded so that it is split into segment files and encoded for streaming.
Each segment is usually for a few seconds and it is for each bit rate, to a client to adapt the condition, like downloading high-quality video segments when a networking condition is good.

## Streaming format

So, to implement adaptive bitrate streaming, videos have to be encoded into suitable formats for streaming.
There are mainly 3 formats for this: CMAF, HLS and MPEG-Dash [[2]](#2)[[3]](#3).


### CMAF (Common Media Application Format)

This is not a protocol, but the standard to use a command media format for streaming to reduce complexity to make this work with HLS and DASH protocols.
CMAF supports a standard container format, which is fragmented MP4, for segments.


### HLS (HTTP Live Streaming)

HLS is the format developed by Apple and widely used by its products.

After Apple supported CMAF for HLS, it also developed the Low-Latency HLS, and thus, there are 3 versions of HLS formats

- Traditional HLS
- HLS with the Low-Latency HLS protocol to improve latency
- HLS with the CMAF format to standard container files

### MPEG-DASH (Dynamic Adaptive Streaming over HTTP)

MPEG-DASH is another way of streaming method.
You can see some comparisons in [the article from Cloudflare](https://www.cloudflare.com/learning/video/what-is-mpeg-dash/).

### Comparisons of 3 formats

| | CMAF | HLS | DASH |
| --- | --- | --- | --- |
| Device supports required | No | Yes | Yes |
| Fragmented MP4 support (fMP4) | Yes |  Yes | Yes |
| MPEG-TS support | No | Yes | Yes | 


## Video bit rate and frame rate

Next is about a bit rate and frame rate.
Frame rate is the number of images in a second and each image is called frame.
On the other hand, the video bit rate is the amount of details in each frame [[4]](#4).

The recommended parameters of each bit rate and frame rate are different on each streaming service.
For example, there are recommended settings on [YouTube](https://support.google.com/youtube/answer/1722171?hl=en#zippy=%2Ccontainer-mp%2Caudio-codec-aac-lc%2Cframe-rate)

On YouTube, the recommended parameters are different between an HDR (High Dynamic Range) and SDR (Standard Dynamic Range) video.
In short, HDR is higher quality than SDR according to [the article of ViewSonic](https://www.viewsonic.com/library/photography/what-is-hdr-hdr-vs-sdr/).

For HDR videos, the recommended parameters of bit rates and frame rates on YouTube as of January 2024 are

| Resolution | Video bit rate for frame rates (24, 25, 30) | Video bit rate for high frame rates (48, 50, 60) |
|---| --- |--- | 
| 1080p | 8 Mbps | 12 Mbps |
| 720p | 5 Mbps | 7.5 Mbps |
| 480p | 2.5 Mbps | 4 Mbps |

On the other hand, audio bit rates on YouTube are followings:

- Mono: 128 kbps
- Stereo: 384 kbps
- 5.1: 512 kbps

## Compression algorithm

There are multiple compression algorithms, H.264 and H.265.

H.264, or Advanced Video Encoding (AVC), has been a video compression standard.
And H.265 or High-Efficiency Video Coding (HEVC), is a successor of H.264 [[5]](#5).

As a successor, H.265 compressed files roughly twice as efficiently as H.264 does while maintaining the image quality, although requiring more computational resources, not only the time for encoding but also decoding for video playbook.

# FFmpeg commands

Now let's look at how the above `ffmpeg` command works.

```bash
ffmpeg -i animation_with_audio.mkv \
    -c:v libx264 \
    -hls_time 1 \
    -hls_playlist_type vod \
    -hls_segment_type fmp4 \
    -b:v:0 8M -r:v:0 30 -bufsize 8M \
    -b:v:1 2.5M -r:v:1 24 -bufsize 2.5M \
    -b:a:0 384k \
    -b:a:1 128k \
    -map 0:v -map 0:a -map 0:v -map 0:a -var_stream_map "v:0,a:0,name:1080p v:1,a:1,name:480p" \
    -master_pl_name 'playlist.m3u8' \
    'public/animation_with_audio/playlist_segment_%v.m3u8'
```

To see the details of options and how they work, there are the [official document](https://ffmpeg.org/ffmpeg-all.html) and [the wiki](https://trac.ffmpeg.org/wiki).

Here, I'm going to describe them briefly.
There is more information on pages like wiki. For instance, H.264 encoding is described in [this page](https://trac.ffmpeg.org/wiki/Encode/H.264)

## Map option

The map option chooses which stream of an input file should be output.
For example, the command `ffmpeg -i input0.mp4 -i input1.mp4 -map 0:v -map 1:a` means 

- `-map 0:v` means the video stream of 1st input file `input0.mp4` will be output
- `-map 1:a` means the audio stream of 2nd input file `input1.mp4` will be output

The more details of `map` option are described in [the ffmpeg wiki](https://trac.ffmpeg.org/wiki/Map)

## HLS specific parameters

- `-c:v libx264`: Use H.264. `H.265` didn't work on a browser.
- `-hls_segment_type`: The file format of a segment file. `fmp4` means fragmented MP4 format.
- `-hls_time X`: The time for each segment in seconds.
- `-hls_playlist_type vod`: Emit `Emit #EXT-X-PLAYLIST-TYPE:VOD` in the header of a m3u8 (manifest) file, and set `hls_list_size` to 0.
- `-hls_list_size`: The max number of segments. The default value is 5 and 0 means all segments.
- `-hls_segment_filename`: The filename of each segment
- `-master_pl_name`: The playlist name for HLS
- `var_stream_map`: Define how to group the audio, video, and subtitle streams into variant streams.
    - `v:0,a:0 v:1,a:1,s:1` creates a first group from the 1st stream of video and audio, and 2nd group from the 2nd stream of video, audio, and subtitle.
    - The allowed values for groups/variants are 0 to 9.
    - To set a text instead of indexes in segment filenames, add `name:` on each variant

## Bit rate and frame rate parameters

- `-b:v Xk`: The bitrate of a video stream
- `-b:a Xk`: The bitrate of an audio stream
- `-r:v X`: The frame rate on a video stream

On top of the above, there are a few parameters to limit output bit rates, described in [the ffmpeg wiki](https://trac.ffmpeg.org/wiki/Limiting%20the%20output%20bitrate).

- Bit rate and buffer size:
    - `bufsize` determines how frequently checks for calculating and correcting the average bit rate. Without this, output bit rates could be different from the specified average rates too much or too low.

# Frontend

Adaptive Bitrate Streaming, both of HLS and DASH and likely CMAF, isn't supported on browsers like Google Chrome, so it's required to use a library like [Video.js](https://videojs.com/).

```html
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="//vjs.zencdn.net/8.3.0/video-js.min.css" rel="stylesheet">
    </head>
    <body>
        <video id="video" class="video-js vjs-default-skin" controls>
            <source src="./output/playlist.m3u8" type="application/x-mpegURL" />

            Your browser does not support the video tag.
         </video>

         <script src="//vjs.zencdn.net/8.3.0/video.min.js"></script>
         <script src="https://unpkg.com/@videojs/http-streaming@3.8.0/dist/videojs-http-streaming.min.js"></script>
         <script>
            videojs('video');
         </script>
    </body>
</html>
```

## File structure

Before running the above command, create directories `public/animation_with_audio` and `public/animation_without_audio`.
Then it'll output files under those directories.
Then put `index.html` file described on the above section under the `public` directory.
So, the final file structure looks like next.

```bash
$ tree .
.
├──
├── animation_with_audio.mkv
├── animation_without_audio.mkv
├── hls.sh
├── index.js
├── package-lock.json
├── package.json
├── public
│   ├── animation_with_audio
│   │   ├── init_0.mp4
│   │   ├── init_1.mp4
│   │   ├── playlist.m3u8
│   │   ├── playlist_segment_1080p.m3u8
│   │   ├── playlist_segment_1080p0.m4s
│   │   ├── playlist_segment_1080p1.m4s
│   │   ├── playlist_segment_480p.m3u8
│   │   ├── playlist_segment_480p0.m4s
│   │   └── playlist_segment_480p1.m4s
│   ├── animation_without_audio
│   │   ├── init_0.mp4
│   │   ├── init_1.mp4
│   │   ├── playlist.m3u8
│   │   ├── playlist_segment_1080p.m3u8
│   │   ├── playlist_segment_1080p0.m4s
│   │   ├── playlist_segment_1080p1.m4s
│   │   ├── playlist_segment_480p.m3u8
│   │   ├── playlist_segment_480p0.m4s
│   │   └── playlist_segment_480p1.m4s
│   └── index.html
└── transcode.sh
```

Note that `index.js` is a small script to start an HTTP server.

## Others

Up until this section, all of them to run the above video was described.
I also looked into a few other things which described below.

### How to transcode to DASH format?

The next command also generates segment files by DASH format, as well as generating manifest files for HLS.

```bash
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
```

You can see the details of an option in [the official document](https://ffmpeg.org/ffmpeg-formats.html#dash-2).

### How to recognize if a video file exists an audio or not

I cannot find a way to run `ffmpeg` for both video files with and without audio.
As a workaround, we can check if a video file contains it or not by the following script.

```bash
AUDIO_CODEC_NAME=$(ffprobe -i $INPUT_FILE -select_streams a -v error -show_entries stream=codec_name -of json | jq -r '.streams[0].codec_name // empty')

if [ "$AUDIO_CODEC_NAME" = "" ]; then
  // No audio
else
  // With an audio
fi  
```

# Reference

There are also other resources that describe more details about video transcoding such as [the article of Scaleflex Blog](https://blog.scaleflex.com/optimize-and-accelerate-videos-for-fast-delivery-a-guide-to-video-transcoding-and-adaptive-streaming/).


- <a id="1">[1]</a> [Cloudflare: What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video/what-is-adaptive-bitrate-streaming/)
- <a id="2">[2]</a> [Wowza: What Is CMAF?](https://www.wowza.com/blog/what-is-cmaf)
- <a id="3">[3]</a> [touchstream: CMAF vs HLS vs Dash: The Impact of Multiple Streaming Formats on Observability](https://blog.touchstream.media/cmaf-vs-hls-vs-dash)

- <a id="4">[4]</a> [FFmpeg API: Media Bitrate vs. Frame Rate: A Detailed Exploration](https://ffmpeg-api.com/learn/ffmpeg/guide/bitrate-vs-frame-rate)
- <a id="5">[5]</a> [epiphan video: H.264 vs. H.265: Video codecs compared](https://www.epiphan.com/blog/h264-vs-h265/)

<script src="//vjs.zencdn.net/8.3.0/video.min.js"></script>
<script src="https://unpkg.com/@videojs/http-streaming@3.8.0/dist/videojs-http-streaming.min.js"></script>
<script>
    videojs('video');
 </script>
