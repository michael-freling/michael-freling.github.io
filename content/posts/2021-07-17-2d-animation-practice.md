---
title: "After Effects: What I did to make fan made MV for about me / Suisei Hoshimachi cover"
date: 2021-07-17T00:48:02+09:00
draft: false
---

Written in July 2021.

I posted next video on YouTube.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/gGZpKmEfddw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

I used Adobe After Effects for 2D animation for the 1st time, so in this post, I described how I made each scene.
I already wrote some posts to make this video for practice, so I just referred those posts on some scenes.
But this is the first time to use AE, so there can be better ways to do.


Chat screen
===

There is [another post](https://michael-freling.github.io/posts/2021/06/14/practice-for-a-chat-animation-in-adobe-after-effects/) for how to do a chat animation scene.


Rain scene
===

There is [another post](https://michael-freling.github.io/posts/2021/06/09/after-effects-practice-for-raining-animation/) for raining scene.
But there were a few things that I didn't describe in the post but I tried on the videos.

* Rain drops on a window and its frame should be shown differently
* Words on window and its frame should be shown differently

In both of cases, Luma matte can be used.
Luma matte, which is one of Track Matte, can expose only specific places of an image, and expose its [luminance value](https://stackoverflow.com/a/56678483), which is a numeric value for light from RGB, ,
For more details, [this page](https://www.schoolofmotion.com/blog/how-to-use-track-mattes-after-effects) clearly explains them.

In my video, I created pre-composition for text layers. And it is used by following ways:

* Duplicate window frame image layer
* Duplicate the pre-composition layer
* Put the pre-composition layer below the window frame image layer
* Set Luma Matte for Track Matte to the pre-composition on the text layer

I was able to do the same thing for rain drops layer.


### Improvements

Because I used Luma matte for rain drops, I couldn't animate rain drops to stuck on the top of frame side.
Currently, if rain drops reaches window frame, then it stil drops behind the frame.
Those rain drops cannot be seen because the frame but it will appear after it passes the frame.
I wanted to stuck them, drop on the frame with different speed, and then drop again on the window, but I couldn't figure out how.


Rotate text
===

In order to rotate a text, I learned how to do on next video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ykncwozwUBM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* Add a text layer
* Add a mask on which the text wants to move on the text layer
* Set **Text > Path Options > Path** to the Mask on the text layer
* Enable **Text > Path Options > Reverse Path** when we want to change the direction and position in a opposite way
* To animate a text, change **Text > Path Options > First Margin** gradually on the timeline

Reverse text screen
===

Set scale negative value for x axis.
Then it shows a text backward.

Text shadow
===

In a text layer, we can only set one stroke, but sometimes we wanna show other color as an outer stroke again.
In that case, we can use `Perspective > Drop Shadow` effect.

Audio spectrum
===

I wrote [a different post describing audio spectrum](https://michael-freling.github.io/posts/2021/06/15/after-effects-practice-for-visualizing-audio-file/).


Black noise
===

Use Fractal noise effect on the duplicated image layer.
And change **Fractal Noise > Evolution Options > Random Seed** values on the timeline for animation.

1. To add a black noise on a specific image or on a specific layer
    1. Duplicate the image on which black noise wants to show
	1. Add **Effects & Presets > Noise & Gain > Fractal Noise** to the layer
1. To animate the noise,
    1. Change **Fractal Noise > Evoluion Options > Random Seed** on the timeline

The same thing was performed with `Noise` or `Turbulent Noise` instead of `Fractal Noise`, but `Fractal Noise` could be the best in my case.



Old film tape
===

I wrote [an other post](https://michael-freling.github.io/posts/2021/06/16/after-effects-practice-for-old-film-effects/) differently for old film tape effect.


Rotate randomly
===
In the 2nd interlude, in my video, audio spectrums rotates randomly.
I use [`noise`](https://ae-expressions.docsforadobe.dev/random-numbers.html) function to make it smoothly rotate.
There are other functions like `random`, but it rotates too fast in the scene and I couldn't figure out how to rotate slower using those functions.
I did next changes:

* Make the audio spectrums layer to 3D
* Change X, Y, and Z rotation transform properties to following expressions. Note that SPEED is something you want to change the rotation speed. if it's bigger number, it rotates slower. In my video, I set 2 on one spectrum and 5 on another.

    ```
	SPEED=2
	seedRandom(index)
	transform.xRotation + 360*noise(time/SPEED)
    ```


Transit scenes like closing eyes
---

In my video, animation for closing eyes actually does

- Change the background from white to black, with a wipe transition
- Remove an effect to reduce a saturation on a layer if the background is white

At first, I thought **Effects & Presets > Animation Presets > Transition - Wipes > Iris - round** can be used but because of 2nd bullet point and the transition is reverse direction, I couldn't do it.
So, instead, I created 2 separate layers and animate separately but it behaves like the same way.

### 1. Change the background from white to black

This is very easy.
I created a shape layer, render circle with white fill color, and cover the entire composition.
And change the size on the timeline for animation to make it zero gradually.
Also, under this shape layer, create a solid layer with black color, so once the shape on the shape layer is gone, the background becomes black.

### 2. Animate mask on the Adjustment layer for its effect

In order to remove an effect on the layer, I used Mask and change the size of Mask gradually on its timeline.
I got this idea from next video, and also there is [an article](https://blog.frame.io/2018/02/12/animated-masks-after-effects/) to animate masks.

<iframe width="560" height="315" src="https://www.youtube.com/embed/StCBpTIwOFE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In my video, I did
1. Add an Adjustment Layer
1. Add Hue/Saturation effect to the Layer
1. Add a Mask on the Adjustment layer, and added Ellipse exactly the same size as the shaper layer created on the above
    - This mask
1. Set the size of the Ellipse on timeline exactly the same way as the shape layer created above




Other resources
===
I use these web sites to check previews of each animation and see whether there is a good effect.

- [Preview Gallery for each transition](https://blog.motionisland.com/after-effects-transitions-presets/#.YIXFQKGRXws
)
- [Preview Gallery of each text animation](https://blog.motionisland.com/after-effects-presets-text-animation/#.YIXIwaGRXws)
