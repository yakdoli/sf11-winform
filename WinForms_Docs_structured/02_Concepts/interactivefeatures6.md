---
title: interactivefeatures6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\interactivefeatures6.md
created_at: 2025-07-03
---






##### Interactive Features {#interactive-features style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

User can determine whether the particular GroupView Item is selected or not using the ButtonView and ClipSelectionBounds properties. ButtonView displays the selected GroupView Item in the pressed state.

 

ButtonView can be enabled in the GroupView control at design-time by setting the SelectedItem property to integer values which in turn represents the GroupView Item. ClipSelectionBounds displays a white border around the selected GroupView Item.

[] 


  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------
  GroupView Property    Description
  ButtonView            Setting this property to \'True\' will make the GroupView Items behave like button objects with a distinct selection state that is retained between item clicks.
  ClipSelectionBounds   Specifies whether the selection bounds of the GroupView Item are clipped around it\'s image and text.
  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------


 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                              |
|                                                                                                                                                             |
|                                                                                                                                                             |
|                                                                                                                                                             |
| [this][.groupView1.ButtonView = [true];]          |
|                                                                                                                                                             |
| [this][.groupView1.ClipSelectionBounds = [true];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                                        |
|                                                                                                                                                                        |
|                                                                                                                                                                        |
| [Me][.groupView1.ButtonView = [True]][] |
|                                                                                                                                                                        |
| [Me][.groupView1.ClipSelectionBounds = [True]]               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 921: ButtonView of the \'Cut\' Item**[]**

 

[]{#p650} 

 

###### 3.6.2.4.5.1      ToolTips {#tooltips style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The **ToolTipText** property of the GroupView control can be used to set the text of the tooltip. The **ShowToolTips** property must be set to \'True\' in order to make the tooltip visible.

[] 


  -------------------- ----------------------------------------------------------------------------
  GroupView Property   Description
  ToolTipText          Gets / sets the text of the tooltip.
  ShowToolTips         Sets the visibility of the tooltip. The default value is set to \'False\'.
  -------------------- ----------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [// Set the tooltip text for the GroupView Item. ]                                                                                    |
|                                                                                                                                                                                         |
| [this][.groupView1.GroupViewItems\[0\].ToolTipText = [\"GroupViewItem1\"];] |
|                                                                                                                                                                                         |
| [this][.groupView1.ShowToolTips = [true];]                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                 |
|                                                                                                                                                                                    |
| []                                                                                                                               |
|                                                                                                                                                                                    |
| [\' Set the tooltip text for the GroupView Item. ]                                                                               |
|                                                                                                                                                                                    |
| [Me][.groupView1.GroupViewItems(0).ToolTipText = [\"GroupViewItem1\"]] |
|                                                                                                                                                                                    |
| [Me][.groupView1.ShowToolTips = [True]]                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 922: ToolTip displayed for \"Copy\" Item

 

 

[]{#p651} 

 

[]{#related-topics}

