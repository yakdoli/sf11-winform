---
title: behaviorsettings15.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\behaviorsettings15.md
created_at: 2025-07-03
---






##### Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

The behavior settings that are common to all the Layout Managers are discussed below.

[] 

AutoLayout

[] 

The Layout Manager, by default, listens to the Container\'s Layout events and performs the layout automatically.

[] 


  ------------------------ -----------------------------------------------------------------------------------
  LayoutManager Property   Description
  AutoLayout               Indicates whether the Layout Manager should layout automatically on Layout event.
  ------------------------ -----------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [this][.borderLayout1.AutoLayout = [true];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                 |
|                                                                                                                                                    |
| []                                                                                               |
|                                                                                                                                                    |
| [Me][.borderLayout1.AutoLayout = [True]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}] Note: The above process can be prevented by setting the AutoLayout property to \'False\' and invoking the layout explicitly through a call to the LayoutContainer() method.


[] 

ContainerControl

[] 

The Container control to be laid out by the Layout Manager can be specified using the below given property.

[] 


  ------------------------ ----------------------------------------------------------------------
  LayoutManager Property   Description
  ContainerControl         Specifies the Container control that the Layout Manager will layout.
  ------------------------ ----------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                              |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [this][.borderLayout1.ContainerControl = [this];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                     |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [Me][.borderLayout1.ContainerControl = [Me]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Custom Layout Bounds

[] 

The Layout Manager will, by default, layout the Child components within the Container control\'s client rectangle. However, you can specify any custom layout bounds using the property given below.

[] 


  ------------------------ -------------------------------------------------------------------------------------------------------------------------------------
  LayoutManager Property   Description
  CustomLayoutBounds       Specifies the custom layout bounds, if any, to be used for layout calculation instead of the Container control\'s client rectangle.
  ------------------------ -------------------------------------------------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [this][.borderLayout1.CustomLayoutBounds = [new] System.Drawing.[Rectangle](0, 0, 0, 0);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [Me][.borderLayout1.CustomLayoutBounds = [New] System.Drawing.Rectangle(0, 0, 0, 0)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}] Note: When you specify the custom layout bounds and the Container is resizable, you should also set the AutoLayout property to \'False\' and set a new custom layout bounds when the Container resizes.

 

{border="0"} Note: The layout is done within the Container\'s client rectangle, even if the Container has a scrollable display rectangle.


[]{#related-topics}

