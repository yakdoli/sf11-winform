---
title: rotationtypes.md
original_path: WinForms_Docs/99_Uncategorized/rotationtypes.md
created_at: 2025-08-05
---






##### Rotation Types {#rotation-types style="tab-stops: 0pt"}

[] 

The Rotator control implements four types of rotation.

[] 


+-----------------------------------+-----------------------------------------------------------------------------+
| Property                          | Description                                                                 |
+-----------------------------------+-----------------------------------------------------------------------------+
| RotationType                      | Specifies the type of rotation to use. The options included are as follows: |
|                                   |                                                                             |
|                                   | [·      ]ContentScroll                         |
|                                   |                                                                             |
|                                   | [·      ]SmoothScroll                          |
|                                   |                                                                             |
|                                   | [·      ]RandomSlide                           |
|                                   |                                                                             |
|                                   | [·      ]SlideShow                             |
+-----------------------------------+-----------------------------------------------------------------------------+


[] 

[·      ]**ContentScroll**: this is the default RotationType

This type scrolls the slides continuously with the same speed.

[·      ]**SmoothScroll**: this type of scroll will have a transition of speed from high while starting to slow while ending

We can change the speed of SmoothScroll using the **SmoothScrollSpeed** property.


{border="0"}Note: To see the effect of ContentScroll and SmoothScroll rotation types, we must specify the interval speed greater than 0 using ScrollInterval property.


[] 

[·      ]**RandomSlide**: this type will display a single slide randomly every time a page is refreshed

[·      ]**SlideShow**: the slide shows can also be performed by setting **RotationType** to **SlideShow**

We can set the **HideEffect** and **ShowEffect** property to any style transition types.

[]{#p462} 

[]{#related-topics}

