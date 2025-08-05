---
title: howtodisablesortingwhilerecordadded.md
original_path: WinForms_Docs/99_Uncategorized/howtodisablesortingwhilerecordadded.md
created_at: 2025-08-05
---








  









### How to Disable Sorting While Record Added {#how-to-disable-sorting-while-record-added style="tab-stops: 0pt"}

 

When GridDataBoundGrid's data source is *BindingList*, you can perform sorting only using the *[WrapperClasses]*[. ]

In the following example the *CellClick* event is used to customize sorting with [the WrapperClasses:]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                               |
| [void][ gridDataBoundGrid1_CellClick([object] sender, [GridCellClickEventArgs] e)]          |
|                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                               |
|                                                                                                                                                                                                                               |
| [            [if] (e.RowIndex == 0 && e.ColIndex \> 0)]                                                                                                              |
|                                                                                                                                                                                                                               |
| [            {]                                                                                                                                                                           |
|                                                                                                                                                                                                                               |
| [                [int] filed = [this].gridDataBoundGrid1.Binder.ColIndexToField(e.ColIndex);]                                                   |
|                                                                                                                                                                                                                               |
| [                [string] name = [this].gridDataBoundGrid1.Binder.InternalColumns\[filed\].MappingName;]                                        |
|                                                                                                                                                                                                                               |
| [                [WrapperClass] lw = [this].gridDataBoundGrid1.DataSource [as] [WrapperClass];] |
|                                                                                                                                                                                                                               |
| [                lw.Sort(name, [true]);]                                                                                                                             |
|                                                                                                                                                                                                                               |
| [                e.Cancel = [true];]                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [                [this].gridDataBoundGrid1.Refresh();]                                                                                                               |
|                                                                                                                                                                                                                               |
| [            }   ]                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [        }][]                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] gridDataBoundGrid1_CellClick([ByVal] sender [As] [Object], [ByVal] e [As] [GridCellClickEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [            [If] e.RowIndex = 0 [AndAlso] e.ColIndex \> 0 [Then]]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [                [Dim] filed [As] [Integer] = [Me].gridDataBoundGrid1.Binder.ColIndexToField(e.ColIndex)]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [                [Dim] name [As] [String] = [Me].gridDataBoundGrid1.Binder.InternalColumns(filed).MappingName]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [                [Dim] lw [As] [WrapperClass] = [TryCast]([Me].gridDataBoundGrid1.DataSource, [WrapperClass])]                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [                lw.Sort(name, [True])]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [                e.Cancel = [True]]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [                [Me].gridDataBoundGrid1.Refresh()]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [            [End] [If]]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [        [End] [Sub]]                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

 

[]{#related-topics}

