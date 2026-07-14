---
title: Sparkling Stars animation
date: 2026-07-04
last_modified_at: 2026-07-14
draft: false
tags:
  - Adobe After Effect
  - Anime
  - Effect animation
---

{{< toc >}}

I appreciated the next video which explains how to make the effect in details.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lu7QTLSc9rE?si=ffJHXWFt5sE-5qLV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Sparkling stars animation
### 1. Make a star object and animate it

1. Add new Shape layer **New > Shape**
2. On the right of **Shape Layer1 > Contents**, there is a button **Add**. With that,
    1. Add **Ellipse** and make the size fits to your composition
    2. Add **Fill** and then change the color like yellow
    3. Add ***Pucker & Bloat**
3. Animate this star.
    1. Change the **Pucker & Bloat > Amount** and **Transform > Scale** to make this star animated. In the example,
        2. Set the 1st key frame to set -45 Amount and Scale 0, and
        3. Set the next key frame to set a different Amount and Scale 0
        4. In the middle of the above key frames, set the Scale to 100
    2. Go to a Graph editor by selecting a Graph icon. Right click and select **Edit Value Graph**. Use **Easy Ease** to make the graph to have a longer time around the scale is 100%
4. Rename the layer like **Star**
5. Add a **Outer Glow** effect on the Star layer and the set properties
    1. The Color as the same color as the Shape
    2. Set the Size and Opacity
6. Add this Shape layer into a new composition, like Star

### 2. Create an entire animation

1. Create new composition, let's say "Compositing"
2. Duplicate Star compositions as many starts as you want, and then change them look random like
    1. Set properties of Scale or Rotation
    2. Change the keyframes timing on animations
