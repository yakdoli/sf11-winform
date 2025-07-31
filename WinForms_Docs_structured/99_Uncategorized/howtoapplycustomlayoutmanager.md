---
title: howtoapplycustomlayoutmanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoapplycustomlayoutmanager.md
created_at: 2025-07-03
---








  









## How to apply custom LayoutManager?[] {#how-to-apply-custom-layoutmanager style="tab-stops: 0pt"}

[] 

This can be done by following the below given steps.

[] 

1.   Create and setup the LayoutManager.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [TableLayoutManager][ myLayout = [new] [TableLayoutManager](DiagramWebControl1.Model, 10, 10);] |
|                                                                                                                                                                                                                                |
| [myLayout.HorizontalSpacing = 40;]                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [myLayout.VerticalSpacing = 50;]                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [Dim][ myLayout [As] Syncfusion.Windows.Forms.Diagram.TableLayoutManager = [New] Syncfusion.Windows.Forms.Diagram.TableLayoutManager(DiagramWebControl1.Model, 10, 10)] |
|                                                                                                                                                                                                                                                                                                        |
| [myLay.HorizontalSpacing = 40]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| [myLay.VerticalSpacing = 50]                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Then, set it to the **LayoutManager** property.

[] 

+------------------------------------------------------------------------------------+
| **[\[C#\]]**                     |
|                                                                                    |
| []                                |
|                                                                                    |
| [DiagramWebControl1.LayoutManager = myLayout;] |
+------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                |
|                                                                                   |
| []                               |
|                                                                                   |
| [DiagramWebControl1.LayoutManager = myLayout] |
+-----------------------------------------------------------------------------------+

[] 

3.   Now, execute the client-side function or just call the **LayoutManager.UpdateLayout** function.

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                    |
|                                                                                                                   |
| []                                                               |
|                                                                                                                   |
| [DiagramWebControl1.DiagramLayout(5);]                                        |
|                                                                                                                   |
| []                                                                            |
|                                                                                                                   |
| [\' Call the LayoutManager.UpdateLayout function.]              |
|                                                                                                                   |
| [DiagramWebControl1.LayoutManager.UpdateLayout([null]);] |
+-------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                  |
|                                                                                                                     |
| []                                                                 |
|                                                                                                                     |
| [DiagramWebControl1.DiagramLayout(5)]                                           |
|                                                                                                                     |
| []                                                                              |
|                                                                                                                     |
| [// Call the LayoutManager.UpdateLayout function.]                |
|                                                                                                                     |
| [DiagramWebControl1.LayoutManager.UpdateLayout([Nothing])] |
+---------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

