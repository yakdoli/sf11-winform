---
title: dynamicformatting1.md
original_path: WinForms_Docs/99_Uncategorized/dynamicformatting1.md
created_at: 2025-08-05
---






##### Dynamic Formatting {#dynamic-formatting style="tab-stops: 0pt"}

[] 

Style Settings can be applied to different grid elements dynamically at run time. This can be achieved by proper handling of the **QueryCellStyleInfo** event. It provides the GridStyleInfo object for a cell on demand.

 

**QueryCellStyleInfo** is raised every time a request is made to access the style information for a cell. You can do any type of formatting cells with this event. It accepts **GridTableCellStyleInfoEventArgs** as one of its parameters which can be used to customize the cells of the grouping grid control. For instance, you can apply style settings for a given CellType by using the **TableCellIdentity.TableCellType** property on the instances of GridTableCellStyleInfoEventArgs. style for a given cell.

 

Here is an example code that applies different styles to different cells in the grouping grid.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [// Hook up the event.]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [this][.gridGroupingControl1.QueryCellStyleInfo += [new] [GridTableCellStyleInfoEventHandler](gridGroupingControl1_QueryCellStyleInfo);] |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [// QueryCellStyleInfo event : To Format Cell by Cell Basis on demand.]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [private][ [void] gridGroupingControl1_QueryCellStyleInfo([object] sender, [GridTableCellStyleInfoEventArgs] e)]    |
|                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [    [if](e.TableCellIdentity.TableCellType == [GridTableCellType].RecordFieldCell)]                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [        [if](e.TableCellIdentity.ColIndex %2 == 0)]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [            e.Style.BackColor = [Color].FromArgb(255, 187, 111);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [            e.Style.Font.FontStyle = [FontStyle].Bold;]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [        [else]]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [            e.Style.TextColor = [Color].White;]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [            e.Style.BackColor = [Color].FromArgb(55, 91, 114);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [    [else] [if]( e.TableCellIdentity.TableCellType == [GridTableCellType].AlternateRecordFieldCell)]                                                                |
|                                                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [        [if](e.TableCellIdentity.ColIndex%2==0)]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [            e.Style.Font.FontStyle = [FontStyle].Underline;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [            e.Style.BackColor = [Color].FromArgb(0, 21, 84);]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [            e.Style.TextColor = [Color].White;]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [        [else]]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [            e.Style.BackColor = [Color].FromArgb(255, 188, 112);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [            e.Style.Font.FontStyle = [FontStyle].Italic;]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' Hook up the event.]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                            |
| [AddHandler][ gridGroupingControl1.QueryCellStyleInfo, [AddressOf] gridGroupingControl1_QueryCellStyleInfo]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' QueryCellStyleInfo event : To Format Cell by Cell Basis on demand. ]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] gridGroupingControl1_QueryCellStyleInfo([ByVal] sender [As] [Object], [ByVal] e [As] GridTableCellStyleInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                            |
| [If][ e.TableCellIdentity.TableCellType = GridTableCellType.RecordFieldCell [Then]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                            |
| [If][ e.TableCellIdentity.ColIndex [Mod] 2 = 0 [Then]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                            |
| [e.Style.BackColor = Color.FromArgb(255, 187, 111)]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                            |
| [e.Style.Font.FontStyle = FontStyle.Bold]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Else]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                            |
| [e.Style.TextColor = Color.White]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                            |
| [e.Style.BackColor = Color.FromArgb(55, 91, 114)]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [If]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [ElseIf][ e.TableCellIdentity.TableCellType = GridTableCellType.AlternateRecordFieldCell [Then]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                            |
| [If][ e.TableCellIdentity.ColIndex [Mod] 2 = 0 [Then]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                            |
| [e.Style.BackColor = Color.FromArgb(0, 21, 84)]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                            |
| [e.Style.Font.FontStyle = FontStyle.Underline]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                            |
| [e.Style.TextColor = Color.White]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Else]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                            |
| [e.Style.BackColor = Color.FromArgb(255, 188, 112)]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                            |
| [e.Style.Font.FontStyle = FontStyle.Italic]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [If]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [If]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Given below is a sample screen shot.

[] 

{border="0"}

[] 

*[Figure ][326][: Dynamic Formatting applied to the Grid Grouping Control]****[]***

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Appearance\\Dynamic Formatting Demo


 

[]{#p453} 

 

[]{#related-topics}

