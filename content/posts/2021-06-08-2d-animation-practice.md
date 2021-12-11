---
title: "After Effects: Practice for raining animation"
date: 2021-06-09T01:32:21+09:00
draft: false
---

This is a note when I tried to make a rain scene.
I'm not very familiar with Adobe After Effects, so some steps can be inefficient or incorrect, so please keep in mind about there might be better way when you read this post.

The example of the animation I made on this post is next one.


<iframe width="560" height="315" src="https://www.youtube.com/embed/dd3kWPGFnH0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The background of this animation is from [this page](https://unsplash.com/photos/cRBCdpGtPf4).

There are a few effects to make the rain scene more realistic:
* For rain drops on a window, use `CC. Mr Mercury`, `Fractral Noise`, and `Displament Map`
* For raining, use `CC. Rainfall`
* For a fogged window, use `Camera Lens Blur`
* For text on a fogged window, use `Overlay` blending mode


Details of each effect
===

Rain drops on a window
----

I watched next video to learn how to show rain drops, but I removed some steps that I couldn't see significant differences.

<iframe width="560" height="315" src="https://www.youtube.com/embed/XBnTxFPO_-M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Here are the each step for how to do:

1. To add an effect for rain drops which is transparent to the background
    1. Duplicate a background layer you wanna show through a window
    1. Add a **Simulation > Cc Mr. Mercury** effect to the layer
1. To make rain drops more realistic, update values of CC Mercury Control Effects
    1. To show the rain drops on wide area
        1. Change **Radius X** and **Radius Y**
    1. To change the size of each drop
        1. Change **Blob Birth Size** and **Blob Death Size**
    1. To change how many drops show and how long each drop should show
        1. Change **Birth Rate**
        1. Change **Longevity (sec)**
    1. To change how fast drops move
        1. Change **Velocity**. It seems this relates with horizontal moves especially when Gravity value is very low.
        1. Change **Gravity**
	1. To combine some rain drops randomly, especially for big rain drops
	    1. Add new solid layer on the bottom of a composition and add **Noise & Gain > Fractal Noise** effect to the layer
	    1. Add **Distort > Displament Map** effect to the rain drop layer
	    1. Change **Displament Map Layer** to the layer you added Factal Noise

In the animation, I set following values of the effect.
The composition size of the animation is 1920 x 1080.

1. For small rain drops sticking with the window
    * Radius X: 320
    * Radius Y: 320
    * Velocity: 0
    * Birth Rate: 80
    * Longevity: 20
    * Gravity: 0.0001
    * Blob Birth Size: 0.02
    * Blob Death Size: 0.02
1. For big rain drops falling down on the window shortly
    * Radius X: 320
    * Radius Y: 320
    * Velocity: 0.01
    * Birth Rate: 0.5
    * Longevity: 100
    * Gravity: 0.01
    * Blob Birth Size: 0.15
    * Blob Death Size: 0.2
    * Added Displament Map effect

I also watched next video to understand about Displament Map and Fracteral Noise, so it might be worth watching if you are not familiar with it.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4uQlymVXMPU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Raining
---

For Raining animation, I watched next video and learned `Cc Rainfall` effect can be used.

<iframe width="560" height="315" src="https://www.youtube.com/embed/FIIK73Xfh8E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

These are steps to add this effect:

1. Add an Adjustment layer and add **Simulation > Cc Rainfall** effect to the layer
1. To make raining better, update **CC Rainfall** values
    1. If rain is strong, then
	    1. Change **Drops** to show bigger number of rains
	    1. Change **Size** to show each rain makes it clear
		1. Change **Speed**
    1. If it's windy day, then to make rains fall diagonally,
	    * Change **Wind** and/or **Spread** value to bigger

In my video, the values of these are:

* Drops: 1000
* Size: 3.0
* Speed: 4000
* Wind: 0
* Spread: 6


Fogged window
---

I learned the idea of fogged window is from next video. In next video, there are many explanations not only fogged window, but also rain drops and how to make them more realistic.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GLwpCNil3XE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


To show a fogged window in AE, making our background blurred is one way.
I used `Camera Lens Blur` for my animation, but there are other types of blue so with them you can highly likely do similar things.

1. Add **Blur & Sharpen > Camera Lens Blur** to the background layer
1. Change **Camera Lens Blur** values
    1. Change **Blur Radius** to show how strong the window is fogged


Text on a foggy window
---

I couldn't find any information on how to show rain texts on a foggy window for AE, but there was a video for Photoshop and it can be used in AE too.
Next video is the one to explain how to show rain text on a foggy window with Photoshop.

<iframe width="560" height="315" src="https://www.youtube.com/embed/S893jAVHP3Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


In AE, we can add rain texts similarily and quite easily by:

1. Add a text layer and write texts
1. Change the mode from `Normal` to `Overlay` on the text layer
1. Change the text color to black.
    * The color depends on the blightness of background, but black usually works unless the background is dark


Further improvements
===

Melting text
----

For the words on the window in a rainy day, it's not always clear and usually looked like "melting", or being erased gradually.
I couldn't find how to do very well and easily.


More realistic rain drops
---

In this post, I described to animate rain drops using Mr Mercurity. But instead, there is a sophisticated way to show more reliastic rain drops explained in the next video.


<iframe width="560" height="315" src="https://www.youtube.com/embed/GLwpCNil3XE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

I didn't choose this way because it was too complicated and Mr Mercury was simple and sufficient for me, but if you do not satify with it, the way explained in this video may be helpful.
