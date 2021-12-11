---
title: "After Effects: Practice for visualizing audio file"
date: 2021-06-15T12:33:23+09:00
draft: false
---

This post is written using After Effects 2021.

I made a simple video to use and compare effects described in this post.
<iframe width="560" height="315" src="https://www.youtube.com/embed/GPUCqm7jN9A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



Audio spectrum/waveform effects
---

In AE, there are two effects `Audio Spectrum` and `Audio Waveform` to visualize an audio file.
I learned how to use an audio wavespectrum from next video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Dj2jIxlL0G8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

These are steps for how to use it.
1. Import an audio file to a project and also import it in the composition
1. To show an audio wavespectrum,
    1. Add a Solid layer
    1. Add `Audio Spectrum` effect from **Presets & Efforts > Generate** into the solid layer
    1. Change **Effects > Audio Spectrum > Audio Layer** to the audio file

Now, an audio spectrum was added into the composition.
In order to change the form of it to the circle, `Polar Coordinates` effect can be used.

1. Add **Effects & Presets > Distort > Polar Coordinates** into the solid layer
1. Change **Polar Coordinates > Type of Conversion** to `React to Polar`
1. Set 100 to **Polar Coordinates > Interpolation**
1. If it shows an arc but doesn't show a circle, change **Audio Spectrum > Start Point** or **Audio Spectrum > End Point** to make it circle


The above steps is described for `Audio Spectrum`, but `Audio Waveform` effect can be added by almost identical steps.
The `Audio Waveform` is explained and used in the next video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7EUxhkO3fpg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Many values on Audio Spectrum and Audio Waveform affect their forms and animations, so it's important to change each value and see how it affects, like Display Options.


Note that "Polar coordinates" is a mathematics term and we can see the details of it in [Wikipedia](https://en.wikipedia.org/wiki/Polar_coordinate_system).
