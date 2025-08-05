---
title: groupviewsettings.md
original_path: WinForms_Docs/99_Uncategorized/groupviewsettings.md
created_at: 2025-08-05
---






##### GroupView Settings {#groupview-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section discusses the various settings that can be applied to define the look and behavior of the GroupView control.

 

It includes the below given topics.

[] 

[] 

###### 3.6.2.4.1.1      Appearance Settings {#appearance-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The following table describes the properties that enhance the appearance of the GroupView control.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------+
| GroupView Property                | Description                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| FlatLook                          | Specifies whether the control is displayed with a flat look.                               |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| BorderStyle                       | Gets / sets the border style for the GroupView control. It includes the following options: |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   | [·      ]None,                                                |
|                                   |                                                                                            |
|                                   | [·      ]FixedSingle and                                      |
|                                   |                                                                                            |
|                                   | [·      ]Fixed3D.                                             |
+-----------------------------------+--------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [this][.groupView1.FlatLook = [true];]                                            |
|                                                                                                                                                                                             |
| [this][.groupView1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                               |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [Me][.groupView1.FlatLook = [True]]                                    |
|                                                                                                                                                                                  |
| [Me.][groupView1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle ] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The border of the GroupView Items can be changed by drawing the border without the 3-dimensional edge which can be attained by setting the **FlatLook** property to \'True\'.

[] 

{border="0"}

[] 

Figure 898: Flat Look of GroupView Control Illustrated

[] 

We can specify the border style for the GroupView control using the **BorderStyle** property.

[] 

{border="0"}

[] 

Figure 899: GroupView with BorderStyle set to \"FixedSingle\"

 

[]{#p641} 

 

###### 3.6.2.4.1.2      Behavior Settings {#behavior-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section discusses the properties that determine the behavior of the GroupView control.

[] 

Drag-and-Drop Effect

[] 

This explains the drag-and-drop settings supported by the GroupView control.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| GroupView Property                | Description                                                                                                                                 |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| AllowDragDrop                     | The property determines whether the control will permit user-interactive drag-and-drop of GroupView Items.                                  |
|                                   |                                                                                                                                             |
|                                   |                                                                                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| AllowDragAnyObject                | Setting this property permits the user to drag any object inside the GroupView control, provided AllowDragDrop property is set to \'True\'. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [this][.groupView1.AllowDragDrop = [true];]      |
|                                                                                                                                                            |
| [this][.groupView1.AllowDragAnyObject = [true];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                      |
|                                                                                                                                                         |
| []                                                                                                    |
|                                                                                                                                                         |
| [Me][.groupView1.AllowDragDrop = [True]]      |
|                                                                                                                                                         |
| [Me][.groupView1.AllowDragAnyObject = [True]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Spacing

[] 

Spacing can be provided between the GroupView Items, and between the GroupView control\'s left border and the GroupView Items using the properties given below.

[] 


  -------------------- ----------------------------------------------------------------------------------------------------
  GroupView Property   Description
  ItemXSpacing         It sets the horizontal distance between a GroupView Item and the GroupView control\'s left border.
  ItemYSpacing         It sets the height between adjacent GroupView Items.
  -------------------- ----------------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                              |
|                                                                                                                             |
| []                                                                        |
|                                                                                                                             |
| [this][.groupView1.ItemXSpacing = 5;]  |
|                                                                                                                             |
| [this][.groupView1.ItemYSpacing = 10;] |
+-----------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                       |
|                                                                                                                          |
| []                                                                      |
|                                                                                                                          |
| [Me][.groupView1.ItemXSpacing = 5]  |
|                                                                                                                          |
| [Me][.groupView1.ItemYSpacing = 10] |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

*[]* 

Figure 900: GroupBar with ItemXSpacing = \"5\" and

ItemYSpacing = \'\"10\"**[]**

 

 

[]{#p642} 

 

###### 3.6.2.4.1.3 Scroll Settings {#scroll-settings style="tab-stops: 0pt"}

[] 

We can specify scrolling for the GroupBar control to view the set of GroupView Items back and forth. This can be achieved by setting the **IntegratedScrolling** property to \'True\'**.**

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GroupView Property                | Description                                                                                                                                                                                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Integrated Scrolling              | Setting this property will delegate the GroupView\'s scrolling to the Parent GroupBar control. This mode is exclusive to the VS .NET toolbox type interface where the GroupBar provides the scrolling support for it\'s GroupView Child controls. |
|                                   |                                                                                                                                                                                                                                                   |
|                                   | On disabling this property, scrollbars are set inside the GroupView control to scroll through the GroupView Items.                                                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [this][.groupView2.IntegratedScrolling = [False];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [Me][.groupView1.IntegratedScrolling = [False]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 901: Integrated Scrolling set to \"False\" in the Parent Control

 

 

[]{#p643} 

 

[]{#related-topics}

