---
title: messageboxadv1.md
original_path: WinForms_Docs/99_Uncategorized/messageboxadv1.md
created_at: 2025-08-05
---






#### MessageBoxAdv {#messageboxadv style="tab-stops: 0pt"}

**[]** 

Office2007 Style Message Box is available in Tools Windows. User can replace the .NET MessageBox with new MessageBoxAdv, which supports standard color schemes and custom color schemes in Office 2007 style, for consistent User Interface look and feel. Custom Icons support is also included in MessageBoxAdv. For showing the Message Box, call **MessageBoxAdv.Show** method.\
\

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [MessageBoxAdv.Office2007Theme = [Office2007Theme].Managed;]                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [Office2007Colors][.ApplyManagedColors([this], ][Color][.Red);] |
|                                                                                                                                                                                                                                                                      |
| [MessageBoxAdv.Show([\" Office 2007 Style with Black Color Scheme  \"], [\"MessageBox Adv\"], [MessageBoxButtons].OK);]                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [MessageBoxAdv.Office2007Theme = [Office2007Theme].Managed]                                                                                                            |
|                                                                                                                                                                                                                                  |
| [Office2007Colors][.ApplyManagedColors([Me], [Color].Red)]                                      |
|                                                                                                                                                                                                                                  |
| [MessageBoxAdv.Show([\" Office 2007 Style with Black Color Scheme  \"], [\"MessageBox Adv\"], [MessageBoxButtons].OK)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1458: Custom Color applied to MessageBoxAdv

[]{#related-topics}

