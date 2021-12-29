---
title: "Blender"
date: 2021-12-24T13:08:16-08:00
draft: false
---

Written in December 2021, with Blender 2.93.

Modeling
===

Basics
---
- In order to set real-world size, enable **Viewport Overlays > Measurement > Edge length** during "Edit mode" and show the size of meshes.
  See [this StackExchange answer](https://blender.stackexchange.com/questions/164091/real-world-scale-size) for more details.


Model example
---

### Door

There are a few things to consider before modeling a door
1. The aspect ratio: According to [this article](https://interiordesignassist.wordpress.com/2019/02/25/door-proportions/), most of doors have either of following aspect ratios:
    - Two squares: `1:2`
    - Golden proportion: `1:1.61`
1. Swing direction: A door is designed differently if it's for a right hand or left hand as well as it is opened to an inward or outward direction. See [this article](https://ezhangdoor.com/how-to-determine-door-swing-direction/#:~:text=To%20determine%20the%20door%20swing%20while%20replacing%20an%20existing%20door,the%20door%20is%20left%20handed.) for each case.


#### Handle
See [this video](https://youtu.be/x0of3b6KGRE) for modeling a handle.

#### Board
See [this article](https://thilakanathanstudios.com/2014/10/beginner-tutorial-how-to-create-and-setup-a-door-for-animation-in-blender/) for each step.



Materials
===

Basics
---
- In order to assign a different material on the face of a mesh from the other faces, go to Edit Mode, select the face, and assign the material.

Use cases
---

### Make a glass material

In order to make a glass material like a window, it looks we can do by setting these things.

1. Enable alpha-based transparency
    - Go to **Material > Settings > Blend Mode**
    - Select something like **Alpha Blend**.
1. Use Transparent BSDF Node. This is to show objects inside a glass material in Object Mode.
    - Open **Shading** workspace
    - In **Shader Editor**
        - Add **Transparent BSDF** node
        - Add **Mix Shader** node
        - Connect Shader of **Mix Shader** to the **Surface** of Material Output
        - Connect two **Shader** of Mix Shader to the BSDF of Transparent BSDF and Principled BSDF
1. Set glass like properties. This is to change a material like a glass and also show images outside of the glass.
    - Go to **Material > Surface**
    - Set **Transmission** to 1 or close to it.
    - Set **Roughness** as you like

See following materials for more details
- [Blender Knowledgebase: Basic Alpha Transparency](https://www.katsbits.com/codex/alpha/) 
- [StackExchange: Glass: Increase "Transmission Roughness" as the object behind goes far](https://blender.stackexchange.com/questions/168179/glass-increase-transmission-roughness-as-the-object-behind-goes-far)
- [Blender 3.0 Manual: Principled BSDF](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html#inputs)



Images
===

Troubleshootings
---

### How to find missing texture files and update them?
Go to **File > External Data > Find missing files** and select a correct directory for texture files.

This solution is from [this answer in Stack Exchange](https://blender.stackexchange.com/questions/96587/how-to-re-link-missing-blender-files).

### How to remove images completely from a blender file?
Even if you delete a material using an image file, it can still be selected on a Mateiral.
In order to delete it completely, Go to **Outliner Editor > Orphan Data Display Mode**.
Then delete images you want, or click Purge to delete every data, including images.

This solution is from [this answer in Stack Exchange](https://blender.stackexchange.com/a/142340), and there is an image in the answer.


3D animation
===

1. In order to add an object into your Timeline Editor, choose an object, right click, and click to **_Insert Keyframe** and select one of them like **Location and Rotation**.



Free materials
===

3D Models
---
In each model, it usually has a license so if you plan to use it for non-personal use, you need to check the license and whether it can be used or not.

- [cgtrader](https://www.cgtrader.com/)
- [Free 3D](https://free3d.com/)
- [Sketchfab](https://sketchfab.com/feed)
- [TURBOSQUID](https://www.turbosquid.com/): 


### Note to import 3D models

1. Make sure that 3D models can be imported into Blender. Some models are exported from other modeling tools and cannot be imported into Blender.
1. Make sure that the textures are imported correctly. Many of 3D models use textures and they are distributed in a different file sometimes.
     We need to download them and map textures with those files correctly on Blender.

Motion captures
---
- [Mixamo](https://www.mixamo.com/#/): a web serivce to host animation model, with like fbx format.
