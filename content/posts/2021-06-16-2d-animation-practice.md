---
title: "After Effects: Practice for old film effects"
date: 2021-06-16T03:01:07+09:00
draft: false
---

This post is written using After Effects 2021.

I wanted to show an animation like old tape films, and made the next video. In this video, I noted how I did it.

<iframe width="560" height="315" src="https://www.youtube.com/embed/gYhc__hA4AM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In fact, I noticed there are some plugins like [motionarray](https://motionarray.com/plugins/premiere-pro/transitions/basic-roll-9/), but I hadn't known before I made it.
So, we might be able to do the same thing by easier way with them.

Besides, there is [an article](https://blog.fmctraining.com/blog/more-of-the-same-6-ways-to-duplicate-elements-in-after-effects) for describe how to repeat objects in AE.
I use `Repeater` learned from this article, and didn't try other ways but might be worth trying.


Old film effects
---

First of all, I made a pre-composition to animate several scenes, without old film tapes.

Then using the pre-composition, I edited another composotion to show an old film tape.

### Old film tape

Like next video, I made the old film tape effect.

<iframe width="560" height="315" src="https://www.youtube.com/embed/YSB7M8c67Gc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

There are multiple ellipses on the above and below of each scene, and in order to show the same ellipses multiple times, `Repeater` for a Shape layer can be used.
These are steps to make those ellipses.

1. Add a Shape layer and render an ellipse in it
1. Click `Add` on the side of **Shape Layer > Contents**, and select `Repeater`
1. Change **Repeater > Copies** to add or remove the number of ellipses
1. Change **Repeater > Transform: Repeater > Position** to expand intervals between each ellipse
1. Then do the same thing to show other side


---
### Repeat a film screen

The above step only repeats eillipses, and in order to repeat pre-compositions, `Motion Tiles` can be used.
I tried and these are what I did

1. Add **Stylize > Motion Tile** to the pre-composition I made on the above steps
1. Change **Effects > Motion Tile > Output Width** to repeat screen horizontally. I chose (odd number) * 100, like 700 or 900. It looks how Output Width works if it is:
    - 100: show 1 screen
	- 200: show 1 screen and 0.5 on the left and 0.5 on the right
	- 300: show 3 screens
1. Change **Transform > Position** of the pre-composition to move the repeated pre-composition.

Then we can make an animation like the video on the top of this page.

There is a limitation of Motion Tiles, though, that it cannot exceed 30,000 pixels of either a width or height.
When I set more than that, like setting Output Width to 5000, then I got an error `After Effects error: Motion Tiles cannot allocate a buffer larger than 30000 pixels in either dimension (516)`.
In this case, we have to reduce either `Output Width` or `Output Height`.



### Further improvements
I haven't changed an appearance of a old film screen, but I found there are some articles or videos to explain about it.
It looked not so simple so I skipped it, but it can make an animation better.
