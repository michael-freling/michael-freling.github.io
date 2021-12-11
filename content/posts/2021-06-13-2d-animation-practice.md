---
title: "Practice for a chat animation in Adobe After Effects"
date: 2021-06-14T07:51:48+09:00
draft: false
---

This post is written using After Effects 2021.
I also added the links to videos where I learned how to do, so if you are unfamiliar with UIs on AEs, those videos are helpful for how to use.



Chat animation
===

I made a chat animation, and from that knowledge, I made the next video.


<iframe width="560" height="315" src="https://www.youtube.com/embed/ghg05TdbZ4E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In this post, I'll describe how I made this video, especially how to make a speech bubble in details.

---

Speech bubble
---

There are a few things to consider to make a speech bubble.

- Speech bubble shapes
- Make speech bubble reusable
- Add popup effect to a speech bubble


### A speech bubble shape

I watched next video to learned how to make a speech bubble.

<iframe width="560" height="315" src="https://www.youtube.com/embed/aOrn-BdbveE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

From this video, I took these steps to make a speech bubble.
1. To make the shape
    * Add a **Shape Layer** in the composition, let's say "Speech bubble shape"
    * Add a **Rounded Rectangle** in the layer
        * It doesn't have to be a rounded rectangle. You can add an ellipse, rectangle, or other shapes.
    * ~~Add a triangle in the shape layer using **Pen Tool**~~
    * ~~To hide strokes of the triangle on the basic rounded rectangle area, click **Add** on the right of **Contents** in the shape layer and choose **Merge Path**~~
        * *I couldn't add the triangle because it's hard to animate, change text, and change the size of the rectangle dynamically which I described in the later steps.*
1. Add a Text layer, let's say "Speech bubble text"
1. Pre-compose the shape and text layers. Let's say "Speech bubble" for this pre-composition.


---
### Reusable speech bubble

Next, in order to make multiple speech bubbles with different texts, we are going to make one precomposition and make it reusable using `Essential Properties` and `Expression`.

* With `Essential Properties`, layers referring to the same precomposition can show different text
* With `Expression`, the shape layer can automatically resize even if the length of text changes


#### Enable to change text without changing precomposition

I learned how to use `Essential Properties` on next video.
<iframe width="560" height="315" src="https://www.youtube.com/embed/Wz_YM0l6AFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

These are steps to set text as essential properties of the pre-composition.

1. On Speech bubble precomposition, click "Open in Essential Graphics" by a right click on the precomposition or under "Edit" tab
1. On the Essential Graphics window, check if "Primary" shows the name of precomposition, which is "Speech bubble" in this post. If not, change it so
1. To add an essential property of the precomposition, drag **Text > Source Text** under the text layer into the "Essential Graphics" window
1. Rename the property name of Source Text if you want. In this post, keep it as it is, which means "Source Text".
1. Open the original composition layer and see you can see **Essential Properties** under the precomposion "Speech bubble" on the timeline window.
1. Now different text with same precomposition can be set even if we duplicate the layer using this Essential Properties.
    * For example, `"TEXT 1"` can be set on a layer while `"TEXT 2"` can be set on another layer
        * *Note that text must be double-quoted.b in Essential Properties, and \n has to be used for a line separator for a multi line text*

#### Auto resize the rectangle matching with the text size

I learned how to resize a rectangle automatically whenever the text length changes from next video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/XjVoN0n73sM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

These are steps to do it:
1. Add **Effects & Presets > Expression Controls > Slider Control** effect into the "Speech bubble shape" layer
1. Rename **Slider Control** under **Speech bubble shape > Effects** to "Padding", because this slider value is used for it between the text and the border of the rectangle
1. To edit Expression on the size of the rectangle, expand **Speech bubble shape > Contents > Rectangle 1 > Rectangle Path 1 > Size** and click "Size" while pressing alt key.
1. Update the Expression to next in order to update the size of the rectangle automatically.

    ```
    d = thisComp.layer("Speech bubble text").sourceRectAtTime();
    padding = effect("Padding")("Slider");
    x = d.width + padding;
    y = d.height + padding;
    [x, y]
    ```

Besides the above steps, it's better to change "Anchor Point" with the same way in the case if there are multiple lines on the Text layer.
Next video explains well about how to update expressions in each case.

<iframe width="560" height="315" src="https://www.youtube.com/embed/In4miXUdxko" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

These are steps for my video.
1. First of all, set "Parent Layer" on the Text Layer.
    1. If "Parent & Link" column doesn't show on the timeline window, at first you have to make it visible. To do it, right click on the header on the window and mark **Columns > Parent & Link**.
    1. Choose "Speech bubble shape" layer on the "Parent & Link" of "Speech bubble text" layer.
1. Set next expressions on **Speech bubble text > Transform > Anchor Point**.

    ```
    d = thisLayer.sourceRectAtTime();
    x = d.width / 2 + d.left;
    y = d.height / 2 + d.top;
    [x, y]
    ```

1. Similary, set next expressions on **Speech bubble shape > Transform > Anchor Point**.

    ```
    d = thisComp.layer("Speech bubble text").sourceRectAtTime();
    x = d.width / 2 + d.left;
    y = d.height / 2 + d.top;
    [x, y]
    ```


---
### Add popup effect on the speech bubble

I learned popup effect which looks it can be used in a chat animation from next video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZvQo4ryiyFQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

It's simple to do, but I just did next.
1. Change "Scales" of the "Speech bubble shape" layer on the timeline
    * At first, set 0 on the timeline
	* Then, Move to a value more than 100, like 110
	* At last goes back to 100

Because "Parent & Link" was added on the text layer, when the shape layer scales, the text layer also automatically scales as well.



---
Chat screen
---

In the previous section, I made the Speech bubble precomposition.
For chat animation, I created 2 more compositions for the video.

1. Chat screen composition: which includes layers to each speech bubble
    * Set the timeline for when each speech bubble shows
	* Set "Essential Properties" for what text it should show on each speech bubble
	* This composition itself have a bigger height than main composition
    ![Chat screen](/posts/2021/2021-06-13-2d-animation-practice/images/chat_screen_composition.png)
1. Main composition: Use chat screen composition
    * Change **Transform > Position** of Chat screen composition to camera in and out on the screen.
    ![Chat animation screen](/posts/2021/2021-06-13-2d-animation-practice/images/chat_animation_composition.png)


After making this, the video on the top of this page can be made.


---
Further improvements
---

### Add a triangle to a speech bubble
Because I couldn't change the size and position automatically when a text is updated, I removed the triangle of a speech bubble.
I think if I can use "Expression" better, it's possible to do, but I have no idea how to do.
