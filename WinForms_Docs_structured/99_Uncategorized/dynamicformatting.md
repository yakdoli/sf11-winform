---
title: dynamicformatting.md
original_path: WinForms_Docs/99_Uncategorized/dynamicformatting.md
created_at: 2025-08-05
---






#### Dynamic Formatting {#dynamic-formatting style="tab-stops: 0pt"}

[] 

This section illustrates how to apply the styles for a specific cell as opposed to a group of cells. First handle the QueryCellStyleInfo event. It is raised to let you customize the GridStyleInfo object containing the style info for a given cell.

 

Hook up the QueryCellStyleInfo event, as shown below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [this][.GridGroupingControl1.QueryCellStyleInfo += [new] GridTableCellStyleInfoEventHandler(GridGroupingControl1_QueryCellStyleInfo);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [Private][ [Me].GridGroupingControl1.QueryCellStyleInfo+= [New] GridTableCellStyleInfoEventHandler(GridGroupingControl1_QueryCellStyleInfo)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Define the handler for this event.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [protected][ [void] GridGroupingControl1_QueryCellStyleInfo([object] sender, GridTableCellStyleInfoEventArgs e)] |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [    [if] (e.TableCellIdentity.TableCellType == GridTableCellType.RecordFieldCell)]                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [        [if] (e.TableCellIdentity.ColIndex % 2 == 0)]                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            [// Apply back color and font style for the record field cell]]                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [            e.Style.BackColor = Color.FromArgb(255, 187, 111);]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            e.Style.Font.FontStyle = FontStyle.Bold;]                                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [        [else]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            e.Style.TextColor = Color.White;]                                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [            e.Style.BackColor = Color.FromArgb(55, 91, 114);]                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [    [else] [if] (e.TableCellIdentity.TableCellType == GridTableCellType.AlternateRecordFieldCell)]                                                               |
|                                                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [        [if] (e.TableCellIdentity.ColIndex % 2 == 0)]                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            [// Apply font style, back color and text color for an alternate row]]                                                                                                   |
|                                                                                                                                                                                                                                                 |
| [            e.Style.Font.FontStyle = FontStyle.Underline;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            e.Style.BackColor = Color.FromArgb(0, 21, 84);]                                                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [            e.Style.TextColor = Color.White;]                                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [        [else]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [            e.Style.BackColor = Color.FromArgb(255, 188, 112);]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            e.Style.Font.FontStyle = FontStyle.Italic;]                                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                              |
| [Protected][ [Sub] GridGroupingControl1_QueryCellStyleInfo([ByVal] sender [As] [Object], [ByVal] e [As] GridTableCellStyleInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [If] e.TableCellIdentity.TableCellType = GridTableCellType.RecordFieldCell [Then]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [If] e.TableCellIdentity.ColIndex [Mod] 2 = 0 [Then]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            [\' Apply back color and font style for the record field cell]]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            e.Style.BackColor = Color.FromArgb(255, 187, 111)]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            e.Style.Font.FontStyle = FontStyle.Bold]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [Else]]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            e.Style.TextColor = Color.White]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            e.Style.BackColor = Color.FromArgb(55, 91, 114)]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [End] [If]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [ElseIf] e.TableCellIdentity.TableCellType = GridTableCellType.AlternateRecordFieldCell [Then]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [If] e.TableCellIdentity.ColIndex [Mod] 2 = 0 [Then]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            [\' Apply font style, back color and text color for an alternate row]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            e.Style.Font.FontStyle = FontStyle.Underline]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            e.Style.BackColor = Color.FromArgb(0, 21, 84)]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            e.Style.TextColor = Color.White]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [Else]]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            e.Style.BackColor = Color.FromArgb(255, 188, 112)]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            e.Style.Font.FontStyle = FontStyle.Italic]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [End] [If]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [End] [If]]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 120[]{#p102}

[]{#related-topics}

