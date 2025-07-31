---
title: preventmovingaspecifictabintabcontroladv.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\preventmovingaspecifictabintabcontroladv.md
created_at: 2025-07-03
---






##### Prevent moving a specific Tab in TabControlAdv  {#prevent-moving-a-specific-tab-in-tabcontroladv style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

TabControlAdv now allows to prevent a specific tab control from being moved on a TabControlAdv. This is achieved with the newly added API **TabMoving**.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                             |
| [// Prevents moving the tab.]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| [this][ this.tabControlAdv1.TabMoving += ][new][ Syncfusion.Windows.Forms.Tools.TabMovingEventHandler(tabControlAdv1_TabMoving);] |
|                                                                                                                                                                                                                                                                                                             |
| [void][ tabControlAdv1_TabMoving(][object][ sender, Syncfusion.Windows.Forms.Tools.TabMovingEventArgs e)]                         |
|                                                                                                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                             |
| [            ][if][(e.From == 1 \|\| e.Target == 1)]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                             |
| [                e.Cancel = true;]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                             |
| [        }     ][]                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                               |
| ['Prevents moving the tab.]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Me].tabControlAdv1.TabMoving += [New] Syncfusion.Windows.Forms.Tools.TabMovingEventHandler([AddressOf] tabControlAdv1_TabMoving)]                                                             |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] tabControlAdv1_TabMoving([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Tools.TabMovingEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                               |
| [If][ e.From = 1 [OrElse] e.Target = 1 [Then]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                               |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [If]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]][]                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

 

[]{#related-topics}

