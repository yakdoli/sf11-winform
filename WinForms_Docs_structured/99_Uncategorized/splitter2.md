---
title: splitter2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\splitter2.md
created_at: 2025-07-03
---






##### Splitter {#splitter style="tab-stops: 0pt"}

[] 

A dynamic-splitter window can be embedded in Essential Grid to show multiple views of the same grid by using a Splitter. This MS Excel-like feature enables you to view more than one copy of a worksheet, and scroll through each pane of the worksheet independently. The panes work simultaneously, i.e., the changes made in one pane are reflected in the other. The splitter can be scrolled by placing the mouse pointer over it, holding down the left mouse button and dragging it to the required position. It can be split horizontally and vertically.

 

Following are the events associated with the Splitter control.

[] 


  ------------- -------------------------------------------------------------------------------------------------------------------------------
  Event         Description
  PaneCreated   This event is triggered when the splitter is moved across the Grid.
  PaneClosing   This event is triggered either when the splitter is moved to the end/beginning or when it cannot be located on the worksheet.
  ------------- -------------------------------------------------------------------------------------------------------------------------------


[] 

The splitter can be created in a worksheet by using the following code:

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [this][.splitterControl1.Controls.Add([this].gridControl1);]                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [// PaneCreated event.]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [private][ [void] splitterControl1_PaneCreated([object] sender, Syncfusion.Windows.Forms.[SplitterPaneEventArgs] e)] |
|                                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [Console][.WriteLine([\"Created: \"] + e.ToString());]                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [// PaneClosing event.]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [private][ [void] splitterControl1_PaneClosing([object] sender, Syncfusion.Windows.Forms.[SplitterPaneEventArgs] e)] |
|                                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [Console][.WriteLine([\"Closed: \"] + e.ToString());]                                                                                                       |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [Me][.splitterControl1.Controls.Add([Me].gridControl1)]                                                          |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [\' PaneCreated event.]                                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [private][ void splitterControl1_PaneCreated([Object] sender, Syncfusion.Windows.Forms.SplitterPaneEventArgs e)] |
|                                                                                                                                                                                                                            |
| [Console.WriteLine([\"Created: \"] & e.ToString())]                                                                                                            |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [\' PaneClosing event.]                                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [private][ void splitterControl1_PaneClosing([Object] sender, Syncfusion.Windows.Forms.SplitterPaneEventArgs e)] |
|                                                                                                                                                                                                                            |
| [Console.WriteLine([\"Closed: \"] & e.ToString())]                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][121][: Splitter]*

 

[]{#p111} 

 

[]{#related-topics}

