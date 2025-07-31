---
title: howtodisplaytooltipsforthesymbols.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodisplaytooltipsforthesymbols.md
created_at: 2025-07-03
---








  









## How To Display ToolTips For the Symbols {#how-to-display-tooltips-for-the-symbols style="tab-stops: 0pt"}

[] 

ToolTips can be displayed using the Model\'s **MouseEnter** and **MouseLeave** events. Here is a sample where tooltips are displayed only for nodes of the type \'MySymbol\'.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                        |
| [private][ [void] Model_MouseEnter([object] sender, [NodeMouseEventArgs] evtArgs)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [    [if] (evtArgs.Node.GetType() == [typeof](MySymbol))]                                                                                                |
|                                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [        [this].toolTip1.SetToolTip([this].diagram1, evtArgs.Node.Name.ToString());]                                                                     |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [        [this].toolTip1.Active = [true];]                                                                                                               |
|                                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [private][ [void] Model_MouseLeave([object] sender, [NodeMouseEventArgs] evtArgs)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [    [this].toolTip1.Active = [false];]                                                                                                                  |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] Model_MouseEnter([ByVal] sender [As] [Object], [ByVal] evtArgs [As] Syncfusion.Windows.Forms.Diagram.NodeMouseEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                               |
| [If][ evtArgs.Node.Name.StartsWith([\"MySymbol\"]) [Then]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.toolTip1.SetToolTip([Me].Diagram1, evtArgs.Node.Name.ToString())]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.toolTip1.Active = [True]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [If]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] Model_MouseLeave([ByVal] sender [As] [Object], [ByVal] evtArgs [As] Syncfusion.Windows.Forms.Diagram.NodeMouseEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.toolTip1.Active = [False]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p82} 

 

[]{#related-topics}

