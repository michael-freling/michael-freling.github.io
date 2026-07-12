---
title: Anime style fire
date: 2026-07-05
last_modified_at: 2026-07-11
draft: false
tags:
  - Adobe After Effect
  - Anime
  - Effect animation
---

{{< toc >}}

I appreciated the next video which explains how to make the effect in details. Use `audio` on the Android App to auto-translate.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4KwAQF46x-s?si=Jx6EZyLTXLJPwkHx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Fire animation

This section was written on July, 2026.

The core parts of this frame are

- Shape layer to draw a shape
- Use Wave Warp and CC Sphere effects

Next animation was the one I made by following steps:

[![bdygf.gif](https://s13.gifyu.com/images/bdygf.gif)](https://www.gifyu.com/image/bdygf)

### 1. Create a fire with one color

1. Create a composition main and select it
2. Select "Path" tool and add a rough shape of a water drop. It should create a "Shape Layer"
    1. Click and drag each point to enable to make the edge round instead of straight lines
3. Set the colors of Stroke and Fill to orange and name the layer to **Orange**
4. Add the effect **Wave Warp** to the layer and set Property
    1. **Wave Type** to the **Circle**
    2. **Wave Height** 25, **Wave Width** 80, **Direction**'s angle to 35, for instance
    3. Set **Pinning** to the **Bottom edge**
    4. Preview the animation and see if it already looks like a fire
5. Duplicate the effect and set Properties
    1. Wave Height -25
    2. Direction's angle to -40
6. In order not to move the bottom of the shape
    1. add new ellipse on the bottom of the shape as a new layer.
    2. Rename the layer as orange_core
    3. Copy 2 effects of Wave Warp effects from the orange layer into the orange_core layer
    4. On the properties on the first Wave Warp
        1. Set the Wave Height to 15
    5. On the properties of the 2nd Wave Warp
        3. Set the Wave Type to **Smooth Noise**
        4. Set the Wave Height to 100
        5. Set the Wave Speed to 0.5
7. Adjust the path's shapes of the layer orange when needed


### 2. Create an inner fire

1. Duplicate the orange layers and name them to yellow and yellow_core layers
2. Change the color of the new layers to yellow
3. Set the paths of the Contents of the yellow layer to make it smaller than orange
4. Set the properties of the yellow layer
    1. Set the direction to a different value from orange layer, like 3

### 3. Create sparks

1. Duplicate the composition main and create sparks 1
2. In the sparks 1 composition, delete layers o
3. Set the properties of the 2nd Wave Warp of the layer
    1. Set Wave Height to -150
    2. Set Direction's degree to -36
4. Duplicate the 2nd Wave Warp, and of the new Wave Warp, set
    1. Wave Type to **Smooth Noise**
    2. Wave Height to 30
    3. Wave Width to 100
    4. Direction to -40
    5. Wave Speed to 0.5
5. Duplicate the orange layer and delete 2nd and 3rd Wave Warp effects
6. Set following properties of the 1st Wave Warp on the new layer:
    1. Wave Type to Uncircle
    2. Wave Height to 230
    3. Wave Width to 135
    4. Direction to -25
    5. Wave Speed to 0.5
7. Set the Mode of the new layer to Silhouette Alpha to extract all animations that are below those layers by the layer
8. To make the frame smaller, to set the path of the first layer to smaller


### 4. Create another sparks

Create sparks for far from the core of a fire

1. Duplicate the composition "sparks 1" and rename it to "sparks 2"
3. On the 1st orange layer
    3. Set the path to make it wider and a little taller
    4. Set the following properties of 2nd Wave Warp effect:
        1. Wave Height to 60 from -150
5. On the 2nd orange layer
    1. Set the path to the similar width as the first layer
    2. Set the following properties of Wave Warp effect:
        1. Wave Height to 200
        2. Wave Width to 100
        3. Direction to -40
6. In order to make the central part of this animation less, duplicate the 2nd layer
    1. Set the path to thinner
    2. Set the following properties of Wave Warp effect:
        1. Wave Type to Circle
        2. Wave Height to 25
        3. Wave Width to 80
        4. Direction to -36
    1. Duplicate the first Wave Warp effect and set the following properties of new effect:
        1. Wave Type to Smooth Noise
        2. Wave Height to -260
        3. Wave Width to 180
        4. Direction to -40


### 5. Compose all compositions

1. Select all compositions, fire, sparks 1, and sparks 2 and create another composition by "New Comp from Selection". Let's say it's "finish"
2. Add an effect "CC Sphere" on sparks 2 composition in the "finish" composition and set properties of the effect by followings:
    1. **Rotation > Rotation Y** to 60 degrees
    2. **Radius** to 400
    3. **Light > Light intensity** to 0
    4. **Shading > Ambient** to 100
    5. Set Offset to make them to go around the center
        6. **Note that I created the animation as the portrait, but that caused this animation failed to go around to the top of the fire composition's fire. The fix was to set the size of composition of spark 2 to the square**
3. Duplicate the composition and update Rotation Rotation Y's degree and offset to make it go around in the other side.
4. To adjust a few effects, add a new Adjustment layer and on the layer
    1. add "Roughten Edges" effect
        1. And set Border to 4
        2. **I cannot see any difference**
    2. Add a new effect **Posterize Time** and set:
        1. Set Frame rate to 12
    3. Add a new effect **Glow**
        1. Set Glow intensity to 0.7, for example
    4. Duplicate the Glow effect
5. Adjust properties like colors on each layers for cleaning up

Afterward, the video didn't describe anything, so I updated a few things by myself

1. Add **Fill** effect to spark 1 composition to make the color red
2. I made the spark 2's composition to shorter
3. Duplicate the spark 2 again, set **Transform Y's degree**, add Fill effect to change the color
