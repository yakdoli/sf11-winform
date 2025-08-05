---
title: closingevent1.md
original_path: WinForms_Docs/99_Uncategorized/closingevent1.md
created_at: 2025-08-05
---






#### Closing Event {#closing-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The TabPageAdv.Closing event is raised when a Tabpage is closing.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                |
| [private][ [void] tabPageAdv1_Closing([object] sender, [TabPageAdvClosingEventArgs] args)] |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [    tabControlAdv1.BorderStyle = [BorderStyle].FixedSingle;]                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [    tabControlAdv1.BorderColor = [Color].Red;]                                                                                                                                       |
|                                                                                                                                                                                                                                                |
| [    [//Cancels the tab page closing]]                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| [   args.Cancel = [true];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] tabPageAdv1_Closing([ByVal] sender [As] [Object], [ByVal] args [As] [TabPageAdvClosingEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    tabControlAdv1.BorderStyle = BorderStyle.FixedSingle]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    tabControlAdv1.BorderColor = Color.Red]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [\'Cancels the tab page closing ]]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    args.Cancel = [True]]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1079: Border settings for TabControlAdv when TabPageAdv1 is Closed

 

 

 

[]{#p887} 

[]{#related-topics}

