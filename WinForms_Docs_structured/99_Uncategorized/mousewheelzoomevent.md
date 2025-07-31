---
title: mousewheelzoomevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\mousewheelzoomevent.md
created_at: 2025-07-03
---






##### MouseWheelZoom Event {#mousewheelzoom-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

MouseWheelZoom event occurs when the user holds the Control Key and rolls the mouse wheel.

 

**Event Data**

 

The event handler receives an argument of type MouseWheelZoomEventArgs containing data related to this event. The following MouseWheelZoomEventArgs member provide information specific to this event.[]{#p1002}

 


  -------- --------------------------------------------------
  Member   Description
  Delta    Returns the number of rows or columns to scroll.
  -------- --------------------------------------------------


[]{#p1003}[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [private][ [void] treeViewAdv1\_[MouseWheelZoom]([object] sender, Syncfusion.Windows.Forms.Tools.[MouseWheelZoomEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [//This code prints the no of rows or columns to scroll]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [//This will be displayed in the output window at run time.]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| [Console][.Write([\"Delta Value :\"] + e.Delta.ToString());]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [}][]                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1004}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private Sub ][treeViewAdv1\_[MouseWheelZoom(][ByVal][ sender][ As Object][, ][ByVal][ e ][As][ Syncfusion.Windows.Forms.Tools.MouseWheelZoomEventArgs)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\'This code prints the no of rows or columns to scroll]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\'This will be displayed in the output window at run time.]                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Console][.Write([\"Delta Value :\"] + e.Delta.ToString())]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End Sub][]                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

