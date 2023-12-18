---
title: "Blender Scale Text by Each Letter"
date: 2023-12-17
draft: false
tags:
  - blender
  - blender 4.0
---

This was written using Blender 4.0 by a Blender novice.

The animation in this post looks like next.

<video src="/posts/2023/2023-12-17-blender-scale-text-by-each-letter/videos/step4.mp4" width="100%" height="auto" controls></video>

Except step 4, I referred to [this stackexchange answer](https://blender.stackexchange.com/questions/277352/scale-individual-letters-separately-from-string-to-curves-geometry-nodes-in-blen).

## Step 1: Scale an entire text on Geometry Nodes

![](/posts/2023/2023-12-17-blender-scale-text-by-each-letter/images/step1.png)

1. Add a **Instances > Scale Instances** node and connect between **Group Input** and **Group Output**
    - Set **Y** of **Scale** to 2.0 and make sure the text scales
1. Add a **Utilities > Text > String to Curves** node and set the **String** field on the node
    - Connect from **Curve Instances** of **String to Curves** to **Instances** of **Scale Instances** instead of **Group Input**.
1. Add a **Curve > Operations > Fill Curve** and put it between **String to Curves** and **Scale Instances**


Note that I couldn't figure out how to use the text of its mesh from the **Geometry Input** node for following animation steps correctly.


## Step 2: Animate texts by time frame

<video src="/posts/2023/2023-12-17-blender-scale-text-by-each-letter/videos/step2.mp4" width="100%" height="auto" controls></video>

1. Add a **Input > Scene > Scene Time** node
1. Add a **Utilities > Math > Map Range** node and on the node,
    - Connect the **Frame** of the **Scene Time** node to the **Value**
    - Connect the **Result** to the **Scale** of the **Scale Instances** node
    - Update the **From Max** and **To Max** values for testing. For example,
        - **From Max**: Set 10 so that the text gets the biggest size at 10 keyframe
        - **To Max**: The max scale size of the text
1. This is optional for an animation to change pop up a text from the bottom center instaed of bottom left of each letter. On the **String to Curve** node,
    - Updbate **Pivot Point** to **Bottom Center** 
    - Connect the output of **Pivot Point** to **Center** of **Scale Instance**

What Map Range does is to convert the value from `(From Min, From Max)` to `(To Min, To Max)` [^1].

[^1]: [Blender 4.0 Manual: Map Range node](https://docs.blender.org/manual/en/4.0/modeling/geometry_nodes/utilities/math/map_range.html)


## Step 3: Animate texts by each letter

<video src="/posts/2023/2023-12-17-blender-scale-text-by-each-letter/videos/step3.mp4" width="100%" height="auto" controls></video>

Now use the **Index**[^2] node to change the scale for each letter via **Map Range** node.

[^2]: [Blender 4.0 Manual: Index node](https://docs.blender.org/manual/en/4.0/modeling/geometry_nodes/geometry/read/input_index.html)

1. Add a **Geometry > Read > Index** node
1. Add a **Utilities > Math > Math** node, which is used for the interval frames of each letter, and on the node
    - Update the function to **Multiply**
    - Connect the output from the **Index** node to one of **Value**
    - Connect the output of **Value** on this node to the **From Min** of the **Map Range** node
    - Set another **Value** to an arbitarily number like 10 for the interval
1. Add a **Utilities > Math > Math** node, which is used for how long it takes to scale each letter, and on the node,
    - Update the function to **Add**
    - Connect the output of **Value** on the **Multiply** node to the one of the **Value** of this node
    - Connect the output of **Value** on this node to the **From Max** of the **Map Range** node
    - Set another **Value** to an arbitarily number like 20 for how long takes to animate each letter

## Step 4: Animate texts like soft objects

Animate texts like following squash and stretch principle.
I couldn't refer to anywhere, so there might be a better way.

<video src="/posts/2023/2023-12-17-blender-scale-text-by-each-letter/videos/step4.mp4" width="100%" height="auto" controls></video>

The logic of this animation looks like next.

- Decide what is the max scale of each letter, let's say `threshold`.
- Assuming the value of the **Map Range** node is `v_index`,
    - Set the **To Max** of the **Map Range** node to `2 * (threshold - 1) + 1`, let's say `t_max`
    - Set the scale
        - `t_max + 1 - s` if `v_index > threshold`, 
        - `v_index` otherwise

Note that the speed for a text to be bigger than 1.0 to `threshold`, and from `threshold` to 1.0 is the same.

To change the scale value based on the value by the above formula, I used **Greater Than** and **Mix** nodes by connecting the output of **Greater Than** to **Factor** of **Mix**.
Other than that, add many **Math** nodes to calculate the above.



# Reference
- [Stackexchange answer](https://blender.stackexchange.com/questions/277352/scale-individual-letters-separately-from-string-to-curves-geometry-nodes-in-blen)
