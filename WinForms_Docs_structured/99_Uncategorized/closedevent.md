---
title: closedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\closedevent.md
created_at: 2025-07-03
---






#### Closed Event {#closed-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The TabPageAdv.Closed event is raised when a TapPage is closed using close button.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [private][ [void] tabPageAdv1_Closed([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [    [this].tabPageAdv5 = [new] Syncfusion.Windows.Forms.Tools.[TabPageAdv]();]                                        |
|                                                                                                                                                                                                                           |
| [    [this].tabPageAdv5.Text = [\"New Tab\"];]                                                                                            |
|                                                                                                                                                                                                                           |
| [    [this].tabControlAdv1.TabPages.Add([this].tabPageAdv5);]                                                                               |
|                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] tabPageAdv1_Closed([ByVal] sender [As] [Object], [ByVal] e [As] [EventArgs])] |
|                                                                                                                                                                                                                                                                                                                                         |
| [Me][.tabPageAdv5 = [New] Syncfusion.Windows.Forms.Tools.TabPageAdv() ]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                         |
| [Me][.tabPageAdv5.Text = [\"New Tab\"] ]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [Me][.tabControlAdv1.TabPages.Add([Me].tabPageAdv5)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1078: TabPageAdv1 is Closed and \"New Tab\" is added to the TabControlAdv

 

 

 

[]{#p886} 

[]{#related-topics}

