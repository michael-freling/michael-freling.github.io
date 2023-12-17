---
title: "Blender"
date: 2021-12-24
lastmod: 2023-12-16
draft: false
---

# Table of contents
- [Gradient color](/posts/2023/12/16/blender-animate-a-gradient-material/)


# Old contents

Written in December 2021, with Blender 2.93 or 3.0.

## Modeling

### Basics
- In order to set real-world size, enable **Viewport Overlays > Measurement > Edge length** during "Edit mode" and show the size of meshes.
  See [this StackExchange answer](https://blender.stackexchange.com/questions/164091/real-world-scale-size) for more details.
- To hide a mesh in an edit mode,
     - H: To hide the selected mesh
     - Shift H: To hide everything but the selected mesh
     - Alt H: To unhide everything
  This information is from [this article](https://www.blenderaid.com/post/40675509859/part-of-objects-mesh-hidden-in-object-mode).
  This is useful to edit meshes that are complicated.


### Change a mesh using another mesh

We can select faces from the shape of another object using `Knife Project`.
**Note that how to use seems to be changed in some point, probably Blender 2.8.**

1. Select an object you want to change
1. Go to "Edit Mode"
1. Select another object to cut
1. Select **Mesh > Knife Project**
1. The faces of the object will be selected on the object. Cut the face or extrude it as you like

See next video for how to use Knife project.
<iframe width="560" height="315" src="https://www.youtube.com/embed/rnDzzHAWEHQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Knife project cannot be used with a Link collection.


### Light

Light is an invisible object in Blender to emit lights.

#### Workaround to apply modifiers
Modifiers cannot be applied to Light objects directly, like Array or Mirror.
In order to apply them, use [`Faces of Instancing`](https://docs.blender.org/manual/en/latest/scene_layout/object/properties/instancing/faces.html).
- Create new meash like a face
- Make the mesh a parent of a lamp
- Select the mesh and go to **Properties Editor > Object Properties > Instaning** and select Faces
- Add a Modifier like Array into the mesh. Then the lamp should be created on each duplicated mesh

You can see more details in next video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/j6zf5eQ3D5E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



## Materials

### Basics

- In order to assign a different material on the face of a mesh from the other faces, go to Edit Mode, select the face, and assign the material.

### Use cases

#### Make a glass material

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



## Images

### Troubleshootings

#### How to find missing texture files and update them?
Go to **File > External Data > Find missing files** and select a correct directory for texture files.

This solution is from [this answer in Stack Exchange](https://blender.stackexchange.com/questions/96587/how-to-re-link-missing-blender-files).

#### How to remove images completely from a blender file?
Even if you delete a material using an image file, it can still be selected on a Mateiral.
In order to delete it completely, Go to **Outliner Editor > Orphan Data Display Mode**.
Then delete images you want, or click Purge to delete every data, including images.

This solution is from [this answer in Stack Exchange](https://blender.stackexchange.com/a/142340), and there is an image in the answer.



## 3D animation

During 3D animation, a 3D model keeps changing temporarily.
There are mainly 2 ways to achieve this, using bones or shape keys.
Bones are objects while shape keys aren't.


Basics with bones,

1. In order to add an object into your Timeline Editor, choose an object, right click, and click to **_Insert Keyframe** and select one of them like **Location and Rotation**.
1. Set a parent into an object
    1. Click a child object and then click a parent object
    1. Select **Object > Parent > Object**
        Now you can see the child object under the parent object in the Outliner editor.
    You can see the details of parent objects in [the manual](https://docs.blender.org/manual/en/3.0/scene_layout/object/editing/parent.html?highlight=parent).
1. To animate objects based on an arbitary axis instead of the world origin,
    - the origin of an object can be updated.
        1. Select an object you wanna change the axis
        1. Go to Edit Mode
        1. Select **Mesh > Snap > Cursor to Selected**
        1. Go to Object mode
        1. Select **Object > Set Origin > Origin to 3D Cursor**
        Now the object will move, rotate, or scale based on the 3D cursor you set.
        In order to move the 3D cursor back, **Object > Snap > Cursor to World Origin**.
        This is from [the answer of StackExchange](https://blender.stackexchange.com/questions/127152/rotation-animation-isnt-fixed-on-the-pivot-point).
    - There is a way to update the default configuration for [orbit around](https://www.versluis.com/2019/11/how-to-orbit-around-selections-in-blender/) under **Edit > Preference > Navigation > Orbit and Pan** and turn on Orbit Around Selection.
      But I couldn't rotate an object from another object using this configuration.

Basics with shape keys
- In order to animate a model using shape keys, go to **Dope Sheet Editor > Shape Key Editor Mode**
- In order to control shape keys by bones, use [Drivers](https://docs.blender.org/manual/en/latest/animation/drivers/introduction.html). See next video for more details for how to configure. Briefly explaning,
    - Go to **Object Data Properties > Shape Keys** and right cilck the value of a shape key.
    - Choose "Add Driver" to add the driver for the shape key.
    - Edit property like Object, Bone, Type, or Space
    - They can be also edited on **Drivers Editor > Drivers tool menu** 

    <iframe width="560" height="315" src="https://www.youtube.com/embed/cc3uoHMo7pA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


See [this article](https://all3dp.com/2/blender-shape-keys-simply-explained/) for more details about shape keys.



### Rigging

- During pose mode, to reset all poses, select **Pose > Clear Transform > All**.


### Action

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
- If one action starts from the locations of the end of another action
    - No smart way. Some people recommended to use Delta transform in [this answer](https://blender.stackexchange.com/questions/223194/creating-actions-based-on-local-location-rotation-scale-of-an-object) or [this answer](https://blender.stackexchange.com/questions/139234/how-to-change-an-action-starting-position).



### Camera

In order to switch Active Camera during animation, makers are helpful.
- In the timeline, add a marker by **Marker > Add Marker**
- Select a camera you want to activate
- Select **Marker > Bind Camera to Markers** to set a camera on your animation scene


### Output

Go to **Properties Editor > Output Properties > Output** and change outputs to
- File Format
- Container
- Video Codec
- Audio Codec

See [this answer](https://blender.stackexchange.com/questions/15142/how-to-render-an-animation-as-video-in-blender) for more details.

In order to view rendering result, go to **Image Editor** and see Render Result.
Or **Render > Render animation** to output your animation.
If rendering result turns out pure black, then something might be wrong, like in a Composition Editor, Render Layers doesn't connect to Composite Node.

See these answers for more details.
- [Possible causes for blank output on rendering](https://blender.stackexchange.com/questions/53632/render-result-is-completely-blank)
- [Render turns black when finished](https://blender.stackexchange.com/questions/14377/render-turns-black-when-finished).


### Multiple scenes

On Blender, multiple scenes can be created from a menu bar.

To animate and switch the scenes, 
- Create another Scene
- Use Video Editing Layout or Video Sequencer Editor
- Add each scenes on the Sequencer view


To make a better transition on each scenes
- Select multiple scenes' strips on Sequencer
- Go to **Add > Transition** and choose a Transition suits for your animation, like Cross


However, there is a bug at least on v3.0 to use other scenes.
That is when there are multiple strips of the same scene but different input, camera and sequencer, it doesn't play any audio.
[This](https://developer.blender.org/T69444) is a bug report in Blender.


## Working on multiple blender files

In order to share materials from other blender files, use [Link or Append](https://docs.blender.org/manual/en/3.0/files/linked_libraries/link_append.html).
It's better to import Collection from an blender file instead of Objects.

- Link: Creates a reference to the data. When an original file is changed, the imported data by Link is also updated
    - If objects are imported, they cannot be change the location, rotation, or scale. But if collections are imported, they can
    - In order to reload the new changes of a source blender file, go to **Outliner Editor > Blender File Display Mode**, right click a link file, and select "Reload".
- Append: Make a full copy of data. Unlike Link, the imported data isn't updated when an original file is updated


See next video for how to use Link and Append.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ldHOfvE52QA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


And in order to edit bones for linked models, select the object and go to **Object > Relations > Make Library Override**.
Then the bones can be edited and the model can be animated.
For the details of Library Overrides, see an [official manual](https://docs.blender.org/manual/en/latest/files/linked_libraries/library_overrides.html).

However, a few things cannot be edited.
For example, it looks Materials cannot be updated directly, though for some properties of Materials like color, there is a [workaround](https://blender.stackexchange.com/questions/215663/override-a-material-on-a-linked-object-2-92).


## Examples

### Door

#### Modeling
There are a few things to consider before modeling a door
1. The aspect ratio: According to [this article](https://interiordesignassist.wordpress.com/2019/02/25/door-proportions/), most of doors have either of following aspect ratios:
    - Two squares: `1:2`
    - Golden proportion: `1:1.61`
1. Swing direction: A door is designed differently if it's for a right hand or left hand as well as it is opened to an inward or outward direction. See [this article](https://ezhangdoor.com/how-to-determine-door-swing-direction/#:~:text=To%20determine%20the%20door%20swing%20while%20replacing%20an%20existing%20door,the%20door%20is%20left%20handed.) for each case.


##### Handle
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

##### Board
See [this article](https://thilakanathanstudios.com/2014/10/beginner-tutorial-how-to-create-and-setup-a-door-for-animation-in-blender/) for each step.

##### Animation
- Parent objects are important to rotate 
- The handle must be a child of the main board
- The mainboard should rotate around one of the edge. There should be an object for the edge so that it can be rotated around it


### Character

#### Lip sync

There are multiple addons for Lip sync.

- [Blender Market: Syncnix: Blender Lip Sync Action](https://blendermarket.com/products/syncnix
    - $5 to buy
- [GitHub: Blender Rhubarb Lip Sync](https://github.com/scaredyfish/blender-rhubarb-lipsync)
    - Requires software Rhubarb
    - Requires 9 mouth positions in a pose library
    - Uses a sound file and an optional script file for an animation. It's recommended to use a script file
- [GitHub: io_import_lipSync-blender2.8](https://github.com/iCEE-HAM/io_import_lipSync-blender2.8)
    - Requires software Papagayo-NG
    - Requires mouth positions in a pose library, and there are rules for the names of each pose and the pose library
    - Use Papagayo to generate a dat file


I used Rhubarb Lip Sync addon because it's free and also it's easier to use than Papagayo.

##### Rhubarb Lip Sync

This addon requires a pose library [as of January 2022](https://github.com/scaredyfish/blender-rhubarb-lipsync/issues/28).
In order to animate a model by shape keys, drivers of shape keys with bones have to be set.
See next video for how to.

<iframe width="560" height="315" src="https://www.youtube.com/embed/vZVtUEEssxQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


###### Troubleshootings

If you face an issue and couldn't see any messages on the Blender, a blender should start from CLI like Windows Powershell in order to figure out what happens.

```
PS C:\path> blender.exe
```


####### The file format isn't supported

The audio file format must be either of a wav or ogg.

If you start a Blender from Powershell and try to read an audio file other than the above two formats, you can see an error message like next.

```
{ "type": "start", "file": "C:\\path\\to\\Recording.m4a", "log": { "level": "Info", "message": "Application startup. Input file: C:\\path\\to\\Recording.m4a." } }
{ "type": "failure", "reason": "Error processing file C:\\path\\to\\Recording.m4a.\nCould not open sound file C:\\path\\to\\Recording.m4a.\nUnsupported file extension '.m4a'. Supported extensions are '.wav' and '.ogg'.", "log": { "level": "Fatal", "message": "Application terminating with error: Error processing file C:\\path\\to\\Recording.m4a.\nCould not open sound file C:\\path\\to\\Recording.m4a.\nUnsupported file extension '.m4a'. Supported extensions are '.wav' and '.ogg'." } }

Error!!!
```


####### File sampling rate is too low

The sampling rate of an audio file format must be equal to 16K Hz or more.

Otherwise, you'll see an error message on Powershell like next.

```
{ "type": "start", "file": "C:\\path\\to\\Recording.wav", "log": { "level": "Info", "message": "Application startup. Input file: C:\\path\\to\\Recording.wav." } }
{ "type": "progress", "value": 0.00, "log": { "level": "Trace", "message": "Progress: 0%" } }
{ "type": "progress", "value": 0.01, "log": { "level": "Trace", "message": "Progress: 1%" } }
{ "type": "progress", "value": 0.02, "log": { "level": "Trace", "message": "Progress: 2%" } }
{ "type": "progress", "value": 0.03, "log": { "level": "Trace", "message": "Progress: 3%" } }
{ "type": "progress", "value": 0.04, "log": { "level": "Trace", "message": "Progress: 4%" } }
{ "type": "progress", "value": 0.05, "log": { "level": "Trace", "message": "Progress: 5%" } }
{ "type": "progress", "value": 0.06, "log": { "level": "Trace", "message": "Progress: 6%" } }
{ "type": "failure", "reason": "Error processing file C:\\path\\to\\Recording.wav.\nError performing speech recognition via PocketSphinx tools.\nUpsampling not supported. Input sample rate must not be below 16000Hz.", "log": { "level": "Fatal", "message": "Application terminating with error: Error processing file C:\\path\\to\\Recording.wav.\nError performing speech recognition via PocketSphinx tools.\nUpsampling not supported. Input sample rate must not be below 16000Hz." } }

Error!!!
```


### Particle animation

The next video was helpful to see how to set a particle animation.

<iframe width="560" height="315" src="https://www.youtube.com/embed/2bv973aqx-w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In order to do a similar thing
- Add a "Particle System" into a Modifier of an object
- Change these parameters in **Properties Editor > Particle Properties**
    - To stop particles falling down, set **Field Weights > Gravitiy** to 0
    - To increase the number of particles, set **Emission > Number**
    - To change the mesh of eacah particle, set **Render > Render As** from Halo to others like Object
    - To change the the size of each article, set **Render > Scale**
- To change how each particle moves, add one of Force Field mesh, like Turbulence



## Use other tools or services

### [Mixamo](https://www.mixamo.com/#/)

Mixamo hosts character animaitons and they can be downloaded used.
Their animations can be downloaded like a fbx file format and they can be imported into Blender.
There is also an addon for [Blender](https://substance3d.adobe.com/plugins/mixamo-in-blender/) to reuse animations with the same model easily.
See next video for more details for how to use this addon.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yDc-E-o_I-c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



### [VRoid Studio](https://vroid.com/en/studio)

VRoid Studio is a tool to make 3D character very easily.

In order to import the `.vrm` file exported from VRoid Studio, Use [VRM Addon for Blender](https://github.com/saturday06/VRM_Addon_for_Blender) addon.
After importing, it can also validate a model or add rigs automatically.

Once it's imported, there are some data in the model

- Facial expressions: Face mesh has shape keys for facial expressions.


#### With Mixamo
I failed to apply Mixamo animation to a VRoid model.
These are issues I faced


- Import a VRoid model to Mixamo
    - Failed to import the model with a fbx file, but sometimes, it succeeds for some reasons
        - Exporting a fbx file with "Apply Transform" didn't help
    - Failed to import the model after exporting a fbx file with "Copy Path" Mode and "Embed Textures", to export materials
- Import a Mixamo animation into Blender
    - Failed to apply animation to the original Armature from imported Mixamo animation. Some animations succeeded for some reasons, though
        - Importing a fbx file with "Apply Transform" or "Manual Operation" didn't help


### Other addons

There are many free addons for Blender.
For example, the next video explains 15 free addons.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ggrict0I_M8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- [Text FX addon by Monaime](https://blender-addons.org/text-fx-addon/)
    - Animate a text easily
- [MB-Lab](https://mb-lab-community.github.io/MB-Lab.github.io/)
    - Model a human character
- [Building Tools](https://github.com/ranjian0/building_tools)
    - Model an architecture easily
- [Drop it](https://andreasaust.gumroad.com/l/drop_it)
    - Drop an object to a surface

Paid
- [Blender-Archipack](https://blender-archipack.org/)
    - Build an architecture like a door easily
- [Neoner](https://blendermarket.com/products/neoner)
    - Make a neon light effect


## Free materials

### 3D Models

In each model, it usually has a license so if you plan to use it for non-personal use, you need to check the license and whether it can be used or not.

- [cgtrader](https://www.cgtrader.com/)
- [Free 3D](https://free3d.com/)
- [Sketchfab](https://sketchfab.com/feed)
- [TURBOSQUID](https://www.turbosquid.com/)


#### Note to import 3D models

1. Make sure that 3D models can be imported into Blender. Some models are exported from other modeling tools and cannot be imported into Blender.
1. Make sure that the textures are imported correctly. Many of 3D models use textures and they are distributed in a different file sometimes.
     We need to download them and map textures with those files correctly on Blender.

### Animation

- [Mixamo](https://www.mixamo.com/#/)



## Learning web site

- [LinkedIn Learning: Introducing Blender 2.8 for beginners](https://www.linkedin.com/learning/blender-2-8-essential-training-2/introducing-blender-2-8-for-beginners?autoplay=true)
