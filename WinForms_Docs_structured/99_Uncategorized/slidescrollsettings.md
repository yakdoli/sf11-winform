---
title: slidescrollsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\slidescrollsettings.md
created_at: 2025-07-03
---






##### Slide Scroll Settings {#slide-scroll-settings style="tab-stops: 0pt"}

[] 

Some fundamental properties we can use in rotation types like **ContentScroll**, **SmoothScroll** and **SlideShow** to potentiate the effects on visual aspects are as follows.

[] 

Display start and looping functionalities

[] 

The slides can automatically be started to move through the control, at runtime, by setting the **AutoStart** property. When this property is disabled, then the slides will not rotate until it\'s initiated.

 

The entire set of slides can be repeated, in cycle, by setting the **Loop** property. This repeats the slides without pausing after the first time.

[] 


  ----------- -------------------------------------------------------------------------------------------------------------------
  Property    Description
  AutoStart   Specifies whether the scroll should automatically start when the page gets loaded. Default value is true.
  Loop        Specifies whether to repeat the slides after a complete tour of slides has been exhibited. Default value is true.
  ----------- -------------------------------------------------------------------------------------------------------------------


[] 

Scroll Behavior

[] 

The scroll effects can be controlled by setting scroll behavior properties.

The direction in which the scroll slide has to proceed can be set through **ScrollDirection** properties that allows the scroll to slide in one of the four directions.

The speed of the scroll can be customized using the **SmoothScrollSpeed** property.

The **ScrollInterval** property allows you to set the duration that you prefer after which the next slide should appear.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                                                                                                   |
|                                   |                                                                                                                                                                                                   |
| Property                          | Description                                                                                                                                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ScrollDirection                   | Specifies the direction of scrolling. The options included are as follows:                                                                                                                        |
|                                   |                                                                                                                                                                                                   |
|                                   | [·      ]Up                                                                                                                                                          |
|                                   |                                                                                                                                                                                                   |
|                                   | [·      ]Down                                                                                                                                                        |
|                                   |                                                                                                                                                                                                   |
|                                   | [·      ]Left                                                                                                                                                        |
|                                   |                                                                                                                                                                                                   |
|                                   | [·      ]Right                                                                                                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ScrollInterval                    | Specifies the interval speed of scrolling. For ContentScroll and SmoothScroll, this property should be greater than 0 to scroll the contents. The time interval can be specified in milliseconds. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SmoothScrollSpeed                 | Specifies the speed of the smooth scroll effect. The options included are as follows:                                                                                                             |
|                                   |                                                                                                                                                                                                   |
|                                   | [·      ]Slow                                                                                                                                                        |
|                                   |                                                                                                                                                                                                   |
|                                   | [·      ]Medium                                                                                                                                                      |
|                                   |                                                                                                                                                                                                   |
|                                   | [·      ]Fast                                                                                                                                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

Slide pause options

[] 

A slide can be paused on mouse hover by setting the **PauseOnMouseOver** property, which stalls that slide until the mouse is moved away from it.

When a slide is displayed, it could be held back for a certain time frame, before the next slide is displayed, by setting the **SlidePause** property.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                                     |
|                                   |                                                                                                                                     |
| Property                          | Description                                                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| SlidePause                        | Specifies the \'Time Span\' the slide is held before exhibiting the next slide. The time interval can be specified in milliseconds. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| PauseOnMouseOver                  | Specifies whether to pause the scroll when the mouse is sustained over the slide.                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+


[] 

ClientObjectID

[] 

The client object id can be used to access the control only on client side. **ClientObjectId** can effectively be used to refer the control\'s objects when used with Master pages and Callback controls. This client id can be effectively used in such scenarios instead of the default id with which the control have to be denoted, thereby eliminating any such ambiguity with the references.

[] 


  ---------------- ------------------------------------------------------------------------
  Property         Description
  ClientObjectID   Specifies the user defined id for accessing the object on client side.
  ---------------- ------------------------------------------------------------------------


[] 

Programmatically the ClientObjectID can be set as follows.

[  ]

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                                         |
| []                                                     |
|                                                                                                                         |
| [rotator1.ClientObjectID = [\"Custom ID\"];] |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                                   |
| []                                                                                                                               |
|                                                                                                                                                                                                   |
| [Private][ rotator1.ClientObjectID = [\"Custom ID\"]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p461} 

[]{#related-topics}

