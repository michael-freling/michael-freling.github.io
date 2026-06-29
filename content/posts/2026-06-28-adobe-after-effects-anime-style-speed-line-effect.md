---
title: Anime style speed line effect
date: 2026-06-28
last_modified_at: 2026-06-29
draft: false
tags:
  - Adobe After Effect
  - Anime
  - Effect animation
---

This article was written in 2026-06-28.

{{< toc >}}

I appreciated the next video which explains how to make the effect in details.

<iframe width="560" height="315" src="https://www.youtube.com/embed/kRdyxiONCDg?si=VDS2s69sbwGVbzXs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

I had followed [another video](https://www.youtube.com/watch?v=73T5zAZtCpc) in the middle of the way but stopped because some files were not downloadable.

## Speed lines

The steps to create lines. I created next animation following these steps:

[![bdnY2.gif](https://s13.gifyu.com/images/bdnY2.gif)](https://www.gifyu.com/image/bdnY2)

### 1. Create a background

Here add a gradient colored background.

1. Add new layer Solid from **New > Solid**
2. Add **Gradient Ramp** effect. For eaxmple, On the layer, go to **Effects > Effects & Presets**, search "Ramp" and add it
3. Set **Start Color** and **End Color**, like end color gets darker.
4. Set **Ramp Shape** to **Radial Ramp**
    1. Click and drag the Start of Ramp (the center) and End of Ramp (the outer radius)
5. Optional? Set **Ramp Scatter** to like 200 to make it nicer looks

### 2. Create a center light

1. Add new Solid Layer and add a **Fill** effect
2. Change the **Color** yellow
3. Set **Transform > Rotation** on 45 degrees
4. Set **Transform > Scale** to make it cover an entire screen
5. Set a mask
    1. Select **Rectangle Tool** on a tool bar and create a Mask on the layer with the part of the central light
    2. Set **Mask Feather**. For example, 250. It makes a rectangle blur
    3. Set **Mask Expansion** to make the light wider or narrower.

### 3. Create the base shadow line layer

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
        2. Change the **Tones** to **Duotone**
        3. Set Shadows to the color darker than the background

### 4. Add more variations of the shadow lines

Add as many layer as you want.

1. Duplicate the above "Line Shadows 01" layer into new layer
2. Update some properties to make them look different from the 01 layer. For example,
    1. Update Contrast, Brightness, or Scale
    2. Alt click **Sub Settings > Evolution** and set the expression like `time - 200`

### 5. Create highlights

Add as many layer as you want.

1. Duplicate some shadows layer of existing highlights layers, and rename those layers to "Line Hightlights 01"
2. Set Blending Modes of the new layer "Screen"
    1. Or set "Add" in a few layers depending on how they look
3. Update "CC Toner" effect
    1. Set "Highlights" to the black
    2. Set "Shadows" to the brighter color
4. Add some variations
    1. Update **Fractal Noise > Brightness**
    2. Update **Fractal Noise > Transform > Offset Turbulance**
    3. Update **Fractal Noise > Transform > Rotation**
5. Add more variations by adding **Glow** effect. And update
    1. **Glow Threshold**
    2. **Glow Radius**
    3. **Glow Intensity**

### 6. Create corner shadows

1. Duplicate the center light layer and rename it to a "corner shadows" layer
2. Update the Mode of "Mask 1" to **Subtract** from **Add**
3. Set the **Fill > Color** black
4. Set the **Transform > Opacity** not to make too dark

## Corner light variation

The above steps can be used for other cases like this animation.

[![bdnYS.gif](https://s13.gifyu.com/images/bdnYS.gif)](https://www.gifyu.com/image/bdnYS)

### 1. Create a background in the same way

### 2. Create the base shadow layer

On top of the same step as above.

1. Add **Corner Pin** effect on the Line Shadows layer
2. Drag the positions of each edge of the corner pin to move lines from one edge to another edge

### 3. Add shadow and highlight lines

Add shadow and highlight lines by following the same steps.

### 4. Add soft light

1. Add new Solid layer
2. Add new mask with rounded shape
3. Set **Mask Feather** and **Mask Expansion**
4. Set Blending Modes to Add
5. Add **Fill** effect and set the color

### 5. Add main light

1. Add new Solid layer
2. Set Blending Modes to **Screen**
3. Add new mask with light emitting layer
4. Animate Mask Path by creating multiple key frames with multiple shapes
5. Add **CC radial Radial Fast Blur** effect
