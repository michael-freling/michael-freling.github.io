---
title: Anime style lightning effect
date: 2026-07-12
draft: false
tags:
  - Adobe After Effects
  - Anime
  - Effect animation
  - Anime Lightning effect
  - "Adobe After Effects: Advanced lightning"
---

{{< toc >}}

I appreciated the next video which explains how to make the effect in details.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5JHFggQ8Cqs?si=G_kUZJLJumj2QhU5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Lightning animation

This section was written on July, 2026.

Next animation was the one I made by following steps:

[![bdJHR.gif](https://s13.gifyu.com/images/bdJHR.gif)](https://www.gifyu.com/image/bdJHR)

### 1. Base layer

1. Create new solid layer
2. Add an effect **Advanced Lightning** and set following properties:
    - **Glow Settings > Forking** to 0, to remove lightning hairs
    - Change other settings on **Glow settings** and **Core Settings** to get what you want
3. Animate the layer by
    - Clicking the stop watch on the **Conductivity State**
    - Set the different values of **Conductivity State** in a few key frames

### 2. Core lightning layer

This will change the color of the core of the lightning to the color you want
It's because core and glow settings use screen-style blend instead of normal blend.
So if the core color is a bright color like white, this isn't necessary.

1. Duplicate the first layer.
2. Set the properties on the new layer:
    1. Set **Glow Settings > Radius** to 0
    2. Set **Core Settings > Color** to the color you want
3. On the previous layer, set **Core Settings > Radius** to 0

Then I was able to get what I wanted.
The video did pre-compose the new layer, add **Fill** effect and change the color of the effect, but I didn't see any difference.


### Variations of Advanced Lightning

The above lightning only goes from top to bottom, because the **Lightning Type** is Direction.
We can get some different animations with different lightning types.
Here are a few examples I played around.

However, for more details about Advanced Lightning effect, next video was the most helpful for me to walk through the details:

<iframe width="560" height="315" src="https://www.youtube.com/embed/YJ8jXYU9lYs?si=YkUEMn_3cYqbGIUc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


#### Bouncey

Here is the lightning animation with Bouncey **Lightning Type**.

[![bdJK2.gif](https://s13.gifyu.com/images/bdJK2.gif)](https://www.gifyu.com/image/bdJK2)

#### Anywhere

If it's set as "Anywhere", the lightning goes everywhere.
The example of the animation is next:

[![bdJHC.gif](https://s13.gifyu.com/images/bdJHC.gif)](https://www.gifyu.com/image/bdJHC)

Rough steps to create this was

1. Add new solid layer with **Advanced Lightning** effect, and set
    1. **Lightning Type** to Anywhere
    2. Set **Conductivity State** to make this animated
    3. Set **Forking** to **50%**
    4. Set **Core Settings** and **Glow Settings** as we want to
    5. Enable **Composite on Original**
    6. Set **Outer Radius** to make the effect enough to go a lightning from one edge to another
2. Duplicate the Advanced Lightning 3 times and on each set **Origin** to put them on 4 edges
