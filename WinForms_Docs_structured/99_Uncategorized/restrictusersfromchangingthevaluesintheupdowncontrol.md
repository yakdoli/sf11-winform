---
title: restrictusersfromchangingthevaluesintheupdowncontrol.md
original_path: WinForms_Docs/99_Uncategorized/restrictusersfromchangingthevaluesintheupdowncontrol.md
created_at: 2025-08-05
---






#### Restrict users from changing the values in the UpDown control {#restrict-users-from-changing-the-values-in-the-updown-control style="tab-stops: 0pt"}

You can restrict users from changing the values in the UpDown control by cancelling the ValueChanging event, as shown in the following code snippet.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                        |
| [void][ upDown_ValueChanging([object] sender, [ValueChangingEventArgs] e)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [    e.Cancel = [true];]                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

