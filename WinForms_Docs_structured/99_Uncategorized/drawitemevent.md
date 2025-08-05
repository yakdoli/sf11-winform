---
title: drawitemevent.md
original_path: WinForms_Docs/99_Uncategorized/drawitemevent.md
created_at: 2025-08-05
---






#### DrawItem Event {#drawitem-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is triggered whenever a particular item or area needs to be painted. Below is an example which draws the background and the interior by handling this event.

 

**Event Data**

 

This Event Handler receives an argument of type **DrawTabEventArgs** containing data related to this event. The following DrawTabEventArgs properties provide information specific to this event.

[] 


  ---------------- -----------------------------------------------------------------------------------
  Members          Description
  BackColor        Gets or sets the background color.
  Bounds           Returns the rectangle that represents the bounds of the item that is being drawn.
  BoundsInterior   Represents the interior of the tab minus the borders.
  Font             Gets / sets the font assigned to the tab that is being drawn.
  ForeColor        Gets / Sets the color of the text.
  Graphics         Returns the graphics surface on which the item has to be drawn.
  Index            Returns the index value of the item that is being drawn.
  State            Gets / sets the state of the item that is being drawn.
  TextBrush        Gets / sets the text brush to draw text in the tabs.
  ---------------- -----------------------------------------------------------------------------------


[] 


 

{border="0"} Note: The TabControlAdv.OnDrawItem() method raises the DrawItem event.[  ]


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [private][ [void] tabControlAdv1_DrawItem([object] sender, Syncfusion.Windows.Forms.Tools.[DrawTabEventArgs] drawItemInfo)] |
|                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [drawItemInfo.DrawBackground();]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [drawItemInfo.DrawInterior();]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [switch][([this].comboBox1.SelectedIndex)]                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [case][ 0:[this].Tab_DrawItemYahooMessengerLike(sender, drawItemInfo);]                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [break][;]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [case][ 1: [this].Tab_DrawItemMSNMessengerLike(sender, drawItemInfo);]                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| [break][;]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] tabControlExt1_DrawItem([ByVal] sender [As] System.Object, [ByVal] drawItemInfo [As] Syncfusion.Windows.Forms.Tools.DrawTabEventArgs) [Handles] tabControlExt1.DrawItem] |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [drawItemInfo.DrawBackground()]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [drawItemInfo.DrawInterior()]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Select][ [Case] [Me].comboBox1.SelectedIndex]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Case][ 0]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Me][.Tab_DrawItemYahooMessengerLike(sender, drawItemInfo)]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\'End Section]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Case][ 1]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Me][.Tab_DrawItemMSNMessengerLike(sender, drawItemInfo)]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\'End Section]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Select]]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

