---
title: Adobe After Effects
date: 2026-06-28 01:00:00
last_modified_at: 2026-06-28 01:00:00
draft: false
tags:
  - Adobe After Effect
  - Anime
---

This is a blog post to collect effects which can be used for a character.

## Basic usages

- When you alt-click a stopwatch icon on the left of Transform property like **Position**, then it shows **Expression** for it to change an animation using an expression.


## Anime style speed line

Written in 2026-06-28.

This is based on

<iframe width="560" height="315" src="https://www.youtube.com/embed/kRdyxiONCDg?si=VDS2s69sbwGVbzXs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

~https://www.youtube.com/watch?v=73T5zAZtCpc~: Not this video because it used a file I wasn't able to download.

The steps to create lines

1. Create a background. Here add a gradient colored background
    1. Add new layer Solid from **New > Solid**
    2. Add **Gradient Ramp** effect. For eaxmple, On the layer, go to **Effects > Effects & Presets**, search "Ramp" and add it
    3. Set **Start Color** and **End Color**, like end color gets darker.
    4. Set **Ramp Shape** to **Radial Ramp**
        1. Click and drag the Start of Ramp (the center) and End of Ramp (the outer radius)
    5. Optional? Set **Ramp Scatter** to like 200 to make it nicer looks
2. Create a center light
    1. Add new Solid Layer and add a **Fill** effect
    2. Change the **Color** yellow
    3. Set **Transform > Rotation** on 45 degrees
    4. Set **Transform > Scale** to make it cover an entire screen
    5. Set a mask
        1. Select **Rectangle Tool** on a tool bar and create a Mask on the layer with the part of the central light
        2. Set **Mask Feather**. For example, 250. It makes a rectangle blur
        3. Set **Mask Expansion** to make the light wider or narrower.
3. Create the base shadow line layer
    1. Duplicate the center light layer and rename it "Line Shadows 01"
    2. Remove the **Fill** effect
    3. Add a **Fractal Noise** effect
    4. Set the Property of the fractal noise effect
        1. Set **Contrast** to, for example, 2500, to remove blur
        2. Set **Brightness** to, like 300, to separate white and black are clear
        3. Go to **Transform** and update the scale to look noises become noises with lines instead of rounded shapes
            1. Disable **Uniform Scaling**
            2. Increase scale width and decrease scale height
        4. Animate the layer using **Transform > Offset Turbulence**
            1. Create keyframe on the first layer for Offset Turbulance
            2. Create keyframe on the last layer for Offset Turbulance, and set different values from the first key frame.
        5. Alt-click **Sub Settings > Evolution** and set `time * X` in Expression. This is to increase the speed of a line
    5. Change the color of the lines
        1. Set "Blending Mode" to **Multiply**. I needed to click "Toggle Switches / Modes" on the bottom bar to show the Mode on each layer.
        2. To make the color lighter,
            1. Add an effect **CC toner**
            1. Change the **Tones** to **Duotone**
            2. Set Shadows to the color darker than the background
4. Add more variations of the shadow lines. Add as many layer as you want.
    1. Duplicate the above "Line Shadows 01" layer into new layer
    2. Update some properties to make them look different from the 01 layer. For example,
        1. Update Contrast, Brightness, or Scale
        2. Alt click **Sub Settings > Evolution** and set the expression like `time - 200`
5. Create highlights. Add as many layer as you want.
    1. Duplicate some shadows layer of existing highlights layers, and rename those layers to "Line Hightlights 01"
    2. Set Blending Modes of the new layer "Screen"
        1. Or set "Add" in a few layers depending on how they look
    4. Update "CC Toner" effect
        1. Set "Highlights" to the black
        2. Set "Shadows" to the brighter color
    5. Add some variations
        1. Update **Fractal Noise > Brightness**
        2. Update **Fractal Noise > Transform > Offset Turbulance**
        3. Update **Fractal Noise > Transform > Rotation**
    6. Add more variations by adding **Glow** effect. And update
        1. **Glow Threshold**
        2. **Glow Radius**
        3. **Glow Intensity**
6. Create corner shadows
    1. Duplicate the center light layer and rename it to a "corner shadows" layer
    2. Update the Mode of "Mask 1" to **Subtract** from **Add**
    3. Set the **Fill > Color** black
    4. Set the **Transform > Opacity** not to make too dark


Anime style speed line but the left top corner emits lights look like

1. Create a background in the same way
2. Create the base shadow layer. On top of the same step as above
    1. Add **Corner Pin** effect on the Line Shadows layer
    2. Drag the positions of each edge of the corner pin to move lines from one edge to another edge
3. Add soft Light
    1. Add new Solid layer
    3. Add new mask with rounded shape
    4. Set **Mask Feather** and **Mask Expansion**
    5. Set Blending Modes to Add
    6. Add **Fill** effect and set the color
4. Add main light
    1. Add new Solid layer
    4. Set Blending Modes to **Screen**
    2. Add new mask with light emitting layer
    3. Animate Mask Path by creating multiple key frames with multiple shapes
    6. Add **CC radial Radial Fast Blur** effect
