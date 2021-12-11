---
title: "Video Editing"
date: 2021-03-10T14:57:41+09:00
draft: false
---

This is written in March 2021.

In this page, Adobe Premiere Pro is mostly described.

Workflow
===

If you make a video from multiple other videos, then

1. Prepare source videos
1. Clip some videos to make import time shorter and easy to edit
    * `ffmpeg` might be helpful to do this
1. Import them into Premiere Pro
    * Ingest settings: Use Proxy
	* Codec: Apple ProRes or DNxHR
1. Edit a video

Codec
===

| Format           | H.264    | ProRes                  | DNxHD/HR/HQ    |
| ----             | ---      | ---                     | ---            |
| Compression rate | High     | Low                     | ?              |
| Editing          | Not good | Good                    | ?              |
| Image            | 8bit     | 10bit                   | 8bit?          |
| Audio            | ?        | Uncompressed            | ?              |
| Platform         | ?        | Windows may not support | Cross platform |

* DNxHQ: Standard codec as of 2018
* 10 bit codec has more color and shade options than 8 bit codec
* If a compression rate is higher, it is inefficient for video editing because it requires decompression during video editing.

Import media
===

* How to import `.webm` file?
    * Install a [plugin](https://www.easefab.com/video-to-software/webm-to-adobe-premiere.html)
* Which one is better to ingest, transcoding or using proxies?
    * I do not know so far.
    * Both of transcoding and proxies needs to encode a media and it takes long time if it's a big file. If media is 2GB, you may have to wait a couple of hours to finish it.

Export media
===

See [this video](https://www.youtube.com/watch?v=AT8sU0MyncA&t=268s) for more details about how to export videos faster in Premiere Pro.
Here is a few tips from the video.
For a complete tips, please watch the video.

1. Format and codec of a sequence
    * Choose lightweight but high quality format and codec. For instance,
        * Preview File Format: QuickTime
        * Codec: DNxHR/DNxHD or ProRes
    * Pre-render by hitting a return or enter key
	* Enable "Use Previews" when you export your video
1. About Bitrate ecoding settings under Video tab
    * Choose CBR (constant bitrates) and lower Target Bitrates for faster exporting
        * For example, to upload YouTube, YouTube recommendation for a HD video is 8Mbps bitrates


Audio editing
===

* [How to speed up or down audio without changing pitch](https://www.youtube.com/watch?v=2b23XoAlExs)


Troubleshootings for Adobe Premiere Pro
===

1. How to fix spikes seen on captions when a font size is big.
    * It seems there is no configuration to solve it on captions.
        * [Adobe Support Community](https://community.adobe.com/t5/premiere-pro/spikes-on-captions/td-p/9997652?page=1)
        * [Reddit](https://www.reddit.com/r/premiere/comments/gkua0c/help_spike_in_edge_caption/)
	* Workaround is to use a drop shadowing effect. See [this video](https://www.youtube.com/watch?v=CwTfcJisJw0) for the tutorial of it.
1. How to show two videos side by side?
    * Set scale to 50 for both of two videos and change the positions of them
    * See [this answer on Quora](https://www.quora.com/How-do-I-make-videos-side-by-side-both-playing-at-the-same-time-in-Premiere-Pro-or-After-Effects) for more details.


Other tools
===

ffmpeg
---
ffmpeg is a useful command line tool to encode, trim, or do other things for video files.
The example of trimming and copy a video without encoding is something like this `ffmpeg -i input.mp4 -ss HH:MM:SS -to HH:MM:SS -c copy output.mp4`.

Here is brief explanation of each option:
* Encoding: `-c` option
    * See [Tutorial - Using FFMPEG for DNxHD/DNxHR encoding, resizing, and batch encoding](https://macilatthefront.blogspot.com/2018/12/tutorial-using-ffmpeg-for-dnxhddnxhr.html) for more details
    * Instead of `-c`, `-c:a` for audio and `-c:v` for video can be used
* Trimming: `-ss` and `-to` options
    * See [Trim video files using FFmpeg](https://www.arj.no/2018/05/18/trimvideo/) or [Cutting the videos based on start and end time using ffmpeg](https://stackoverflow.com/questions/18444194/cutting-the-videos-based-on-start-and-end-time-using-ffmpeg) for more details.
	* When trimmings, there might be a black screen without showing anything on the beginning or end of the videos. It can be avoided by `-allow_negative_rs make_zero`.
	    * See [How to avoid the black screen at the beginning?](https://varhowto.com/cut-videos-ffmpeg/#How_to_avoid_the_black_screen_at_the_beginning) for more details

Also, there is an other way to use ffmpeg.

* Check a resolution of video: `ffmpeg -i [file]`


Spleeter
---
Spleeter is a tool to extract audios from a video.
See [its GitHub page](https://github.com/deezer/spleeter) for more details.

It doesn't require an off-vocal video to recognize an audio inside a video.


Utagoe Vocal Ripper (歌声りっぷ)
---

I've never used it.
It extracts an audio from a video, the same as Spleeter.
This requires an off-vocal video besides on-vocal one to extract.
There is few English resource, but this is [an example post](https://medansy.net/remix-web-1-04) to explain this tool in Japanese.
