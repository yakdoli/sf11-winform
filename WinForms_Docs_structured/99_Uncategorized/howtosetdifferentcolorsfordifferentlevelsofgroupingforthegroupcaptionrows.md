---
title: howtosetdifferentcolorsfordifferentlevelsofgroupingforthegroupcaptionrows.md
original_path: WinForms_Docs/99_Uncategorized/howtosetdifferentcolorsfordifferentlevelsofgroupingforthegroupcaptionrows.md
created_at: 2025-08-05
---








  









## How to set different colors for different levels of grouping for the GroupCaption rows {#how-to-set-different-colors-for-different-levels-of-grouping-for-the-groupcaption-rows style="tab-stops: 0pt"}

[] 

You can set different colors for different levels of grouping for the GroupCaption rows by accessing the **QueryCellStyleInfo** event. The following code example illustrates this.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [protected][ [void] GridGroupingControl1_QueryCellStyleInfo([object] sender, [GridTableCellStyleInfoEventArgs] e)] |
|                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [if][ (e.TableCellIdentity.TableCellType == [GridTableCellType].GroupCaptionCell && e.TableCellIdentity.GroupedColumn != [null])]       |
|                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [GridCaptionRow][ captionRow = e.TableCellIdentity.DisplayElement [as] [GridCaptionRow];]                                            |
|                                                                                                                                                                                                                                                                           |
| [//Set color of GroupCaption Cell for Level 0 ]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                           |
| [if][ (captionRow.ParentGroup.GroupLevel == 0)]                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [e.Style.BackColor = [Color].LightGoldenrodYellow;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [//Set color of GroupCaption Cell for Level 1 ]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                           |
| [if][ (captionRow.ParentGroup.GroupLevel == 1)]                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [e.Style.BackColor = [Color].Red;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [} ]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [Protected][ [Sub] GridGroupingControl1_QueryCellStyleInfo([ByVal] sender [As] [Object], [ByVal] e [As] GridTableCellStyleInfoEventArgs)]                        |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [If][ e.TableCellIdentity.TableCellType = GridTableCellType.GroupCaptionCell [AndAlso] [Not] e.TableCellIdentity.GroupedColumn [Is] [Nothing] [Then]]                                 |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [Dim][ captionRow [As] GridCaptionRow = [CType](IIf([TypeOf] e.TableCellIdentity.DisplayElement [Is] GridCaptionRow, e.TableCellIdentity.DisplayElement, [Nothing]), GridCaptionRow)] |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [\'Set color of GroupCaption Cell for Level 0 ]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [If][ captionRow.ParentGroup.GroupLevel = 0 [Then]]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [e.Style.BackColor = Color.LightGoldenrodYellow]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [If]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [\'Set color of GroupCaption Cell for Level 1 ]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [If][ captionRow.ParentGroup.GroupLevel = 1 [Then]]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [e.Style.BackColor = Color.Red]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [If]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [If]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p125} 

[]{#related-topics}

