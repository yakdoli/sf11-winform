---
title: howtopreventthefocusrectanglefrombeingdrawninthetabs.md
original_path: WinForms_Docs/99_Uncategorized/howtopreventthefocusrectanglefrombeingdrawninthetabs.md
created_at: 2025-08-05
---






#### How to prevent the Focus Rectangle from being drawn in the Tabs {#how-to-prevent-the-focus-rectangle-from-being-drawn-in-the-tabs style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

You can easily do this by handling the **DrawItem** event, adjusting the **DrawTabEventArgs** and delegating drawing to the default drawing logic.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [private][ [void] TabControlExt_DrawItem([object] sender, Syncfusion.Windows.Forms.Tools.[DrawTabEventArgs] drawItemInfo)] |
|                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                |
| [// To indicate that the tab gets drawn as if it's not focused (without the focus rect).]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [drawItemInfo.State &= \~[DrawItemState].Focus;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [// Then forward drawing to default drawing logic.]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [drawItemInfo.DrawBackground();]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [drawItemInfo.DrawInterior();]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| [drawItemInfo.DrawBorders();]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                    |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [\'To indicate that the tab gets drawn as if it's not focused (without the focus rect).]                          |
|                                                                                                                                                                     |
| [Dim][ & [As] drawItemInfo.State = \~DrawItemState.Focus] |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [\'Then forward drawing to default drawing logic.]                                                                |
|                                                                                                                                                                     |
| [drawItemInfo.DrawBackground()]                                                                                                 |
|                                                                                                                                                                     |
| [drawItemInfo.DrawInterior()]                                                                                                   |
|                                                                                                                                                                     |
| [drawItemInfo.DrawBorders()]                                                                                                    |
|                                                                                                                                                                     |
| [End][ [Sub]]                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p897} 

[]{#related-topics}

