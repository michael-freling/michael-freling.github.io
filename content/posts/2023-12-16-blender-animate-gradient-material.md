---
title: "Blender: Animate a gradient material"
date: 2023-12-16T15:17:29-08:00
draft: false
tags:
  - blender
  - blender 4.0
---

This post was written using Blender 4.0.

This blog is about to create the animation for color gradient.
The final output of this post is like next:

<video src="/posts/2023/2023-12-16-blender-animate-a-gradient-material/videos/final.mp4" width="100%" height="auto" controls></video>


## Step 1. Add a color gradient

To add color gradient to a material, go to the **Sharding** tab and update nodes like the next.

![](/posts/2023/2023-12-16-blender-animate-a-gradient-material/images/gradient.png)

This is basically by:
- Add a **Texture > Gradient Texture** node
- Add a **Converter > Color Ramp** node between **Gradient Texture** and **Principled BSDF**



## Step 2. Animate a color gradient

1. Add **Vector > Mapping**, **Input > Texture Coordinate**, and **Converter > Separate XYZ** nodes
1. Connect inputs and outputs of each node by followings:
    - Connect **Generated** of Texture Coordinate to **Vector** of **Mapping**
    - Connect **Vector** of **Mapping** to **Vector** of **Separate XYZ**
    - Connect **Z** of **Separate XYZ** to **Fac** of **Color Ramp**
1. This value will be changed on the step 3, but change the Z value of the **Mapping** node and insert the keyframe on a frame appropriately to animate.
    1. Set the same color for the pos = 0 and pos = 1 on `Color Ramp`.
    1. Set z=1 on 100 frames, z=-1 on 101 frames, and z=1 on 200 frames

By following the above, the animation becomes like next.

<video src="/posts/2023/2023-12-16-blender-animate-a-gradient-material/videos/step2.mp4" width="100%" height="auto" controls></video>

Now it's possible to animate, but there is an issue that the animation shows the red color too long and not smooth to transition to another color.


#### Step 3: Smoothly loop the gradient animation

To solve the issue on the step 2, update nodes like next

1. Add 3 **Converter > Math** nodes and change 2 nodes from **Add** to **Truncated Modulo** and **Less Than**.
1. Update values of the nodes to followings
    - **Truncated Modulo**
        - 1st Value: the **Z** of the **Separate XYZ** node
        - 2nd Value: 1.0
    - **Less Than**
        - 1st Value: the **Value** of the **Truncated Modulo** node
        - 2nd Value: 0
    - **Add**
        - 1st Value: **Value** of the **Truncated Modulo** node
        - 2nd Value: **Value** of the **Less Than** node
        - Output Value: **Fac** of the **Color Ramp** node
1. Change the Z of the **Mapping** node on
    - 1st frame: 0
    - 100 frame: 5

The each Math node is described in [this official document](https://docs.blender.org/manual/en/latest/compositing/types/converter/math.html#properties).
I think these nodes are to convert the value of **Z** of **Mapping** between 0.0 to 1.0.

By following the above steps, we completed the gradient animation and made the one like the first video on the top of this post.

# Reference

For Step 1, I referred to the next video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CIjCqR3g_Es?si=t-MfjklU456b5Y4v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


For Step 2, I referred to the next video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ViqfL0LOwUM?si=GAv_9XIujyL7rvYu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

For Step 3, I referred to [this stackoverflow answer](https://blender.stackexchange.com/questions/129918/how-to-animate-a-gradient-moving-over-an-object).
