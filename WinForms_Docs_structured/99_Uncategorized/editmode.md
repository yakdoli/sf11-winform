---
title: editmode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\editmode.md
created_at: 2025-07-03
---








  









### Edit Mode {#edit-mode style="tab-stops: 0pt"}

[] 

Custom Editing with GridEngine

[] 

You can also use the GridEngine to start off the editing process. If you decide to write a custom implementation of the editing, you just need to call some functions which will render the Grid accordingly.

 

Create a**[ ]CurrentTable** property to get the GridEngine\'s current table instance.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [protected][ [GridTable] CurrentTable {]                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [get][ {]                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| [Element][ elem = [this].GridGroupingControl1.Engine.Table.CurrentElement;]                                                                     |
|                                                                                                                                                                                                                                                           |
| [while][ ( elem != [null] && !( elem.IsRecord() \|\| elem.IsCaption() \|\| elem [is] [GridGroup] ) )] |
|                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [elem = ( ([NestedTable])elem ).ChildTable.ParentTable.CurrentElement;]                                                                                                                          |
|                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [GridTable][ table = elem != [null] ? ([GridTable])elem.ParentTable : [this].Engine.Table;]           |
|                                                                                                                                                                                                                                                           |
| [if][ ( table.CurrentRecordManager.UpdateHelper == [null] )]                                                                                    |
|                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [table.CurrentRecordManager.UpdateHelper = [new] UpdateHelper([this]);]                                                                                                     |
|                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [return][ table;]                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[  ]

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Protected][ [ReadOnly] [Property] CurrentTable() [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridTable]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Get]                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ elem [As] Syncfusion.Grouping.Element = [Me].GridGroupingControl1.Engine.Table.CurrentElement]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [While][ elem [IsNot] [Nothing] [AndAlso] [Not] (elem.IsRecord() [OrElse] elem.IsCaption() [OrElse] [TypeOf] elem [Is] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridGroup)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [elem = [DirectCast](elem, Syncfusion.Grouping.NestedTable).ChildTable.ParentTable.CurrentElement]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [While]]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ table [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridTable = IIf(elem [IsNot] [Nothing], [DirectCast](elem.ParentTable, Syncfusion.Web.UI.WebControls.Grid.Grouping.GridTable), [Me].Engine.Table)]                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [If][ table.CurrentRecordManager.UpdateHelper [Is] [Nothing] [Then]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [table.CurrentRecordManager.UpdateHelper = [New] UpdatePanel([Me])]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Return][ table]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Get]]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Property]]                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p83} 

[]{#related-topics}

