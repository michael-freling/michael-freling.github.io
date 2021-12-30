---
title: "Blender"
date: 2021-12-24T13:08:16-08:00
draft: false
---

Written in December 2021, with Blender 2.93 or 3.0.

Modeling
===

Basics
---
- In order to set real-world size, enable **Viewport Overlays > Measurement > Edge length** during "Edit mode" and show the size of meshes.
  See [this StackExchange answer](https://blender.stackexchange.com/questions/164091/real-world-scale-size) for more details.


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
1. Set a parent into an object
    1. Click a child object and then click a parent object
    1. Select **Object > Parent > Object**
        Now you can see the child object under the parent object in the Outliner editor.
    You can see the details of parent objects in [the manual](https://docs.blender.org/manual/en/3.0/scene_layout/object/editing/parent.html?highlight=parent).
1. To animate objects based on an arbitary axis instead of the world origin, the origin of an object can be updated.
    1. Select an object you wanna change the axis
    1. Go to Edit Mode
    1. Select **Mesh > Snap > Cursor to Selected**
    1. Go to Object mode
    1. Select **Object > Set Origin > Origin to 3D Cursor**
    Now the object will move, rotate, or scale based on the 3D cursor you set.
    In order to move the 3D cursor back, **Object > Snap > Cursor to World Origin**.
    This is from [the answer of StackExchange](https://blender.stackexchange.com/questions/127152/rotation-animation-isnt-fixed-on-the-pivot-point).

Action
---

Action is a way to reuse a specific animation of one object.
There are two important editors to
- **Dope Sheet > Action Editor mode**: To edit an action itself. It's better to start an action from 1st frame
- **Nonlinear Animation**: To use multiple actions, animate a scene

To understand an action, see next informative video for how to use Action.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Vuph3QHDroI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

There are a few important things to use Action
- To change the speed of an action, go to **Strip > Action Clip** and set the "Playback Scale" value
- To repeat an action multiple times, go to **Strip > Action Clip** and set the "Repeat" value


Questions to me is
- Can an action be created for multiple objects? - It looks no.
- Is there any way to combine actions of multiple objects and use them? - I cannot find it.

Examples
===

Door
---

### Modeling
There are a few things to consider before modeling a door
1. The aspect ratio: According to [this article](https://interiordesignassist.wordpress.com/2019/02/25/door-proportions/), most of doors have either of following aspect ratios:
    - Two squares: `1:2`
    - Golden proportion: `1:1.61`
1. Swing direction: A door is designed differently if it's for a right hand or left hand as well as it is opened to an inward or outward direction. See [this article](https://ezhangdoor.com/how-to-determine-door-swing-direction/#:~:text=To%20determine%20the%20door%20swing%20while%20replacing%20an%20existing%20door,the%20door%20is%20left%20handed.) for each case.


#### Handle
I checked [this video](https://www.youtube.com/watch?v=FsVtNFY_jBY) to see how to make a model

1. If you can't choose a Single Vert mesh, go to **Edit > Preferences > Add-ons** and enable "Add Mesh: Extra Objects" at first
1. Design a handle using vertexes, so the shape will not be of cylinders.
    1. Select **Add > Mesh > Single Vert > Add Single Vert** and add the mesh
    1. Extrude the mesh to change the shape of a handle you wanna design
        - Note that it has to be Vertex select mode, not Edge select nor Face select mode to see extrude vertexes
1. From vertexes, convert them into the set of cylinders
    1. Change the mode to Object mode and select **Object > Convert > Curve**
    1. Go to **Properties Editor > Object Data Properties > Geometry > Bevel** and
        1. Increase the Depth
        1. Increase the Resolution
1. Edit the handle as a mesh and complete modeling
    1. Select the curve and then **Object > Convert > Mesh**
    
I checked [this slide](https://www.researchgate.net/publication/336988496_BLENDER_TUTORIAL_CREATING_DOOR_HANDLE_WITH_USING_90_EXTRUDE) or [this video](https://youtu.be/x0of3b6KGRE).

#### Board
See [this article](https://thilakanathanstudios.com/2014/10/beginner-tutorial-how-to-create-and-setup-a-door-for-animation-in-blender/) for each step.

#### Animation
- Parent objects are important to rotate 
- The handle must be a child of the main board
- The mainboard should rotate around one of the edge. There should be an object for the edge so that it can be rotated around it


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



Learning web site
===

- [LinkedIn Learning: Introducing Blender 2.8 for beginners](https://www.linkedin.com/learning/blender-2-8-essential-training-2/introducing-blender-2-8-for-beginners?autoplay=true)
