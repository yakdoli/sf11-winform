---
title: events83.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\events83.md
created_at: 2025-07-03
---






#### Events {#events style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Scroll

 

Occurs when the mouse moves any of the thumb over the channel.

                 

EventHandler for Scroll event

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                      |
|                                                                                                                                                                                                                               |
| [rangeSlider.Scroll += new EventHandler( rangeSlider1_Scroll);]                                                                                                                           |
|                                                                                                                                                                                                                               |
| [private][ [void] rangeSlider1_Scroll([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                       |
|                                                                                                                                                                                                                               |
| [    [//Code to handle the event]]                                                                                                                                  |
|                                                                                                                                                                                                                               |
| [}][]                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ValueChanged

                             

Occurs when the value of SliderMin or SliderMax changes.

     

EventHandler for ValueChanged event

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [rangeSlider.ValueChanged += new EventHandler( rangeSlider1_ValueChanged);]                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [private][ [void] rangeSlider1_ValueChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [     [//Code to handle]][ the ][event]                               |
|                                                                                                                                                                                                                                     |
| [}][]                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

