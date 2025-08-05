---
title: delete.md
original_path: WinForms_Docs/99_Uncategorized/delete.md
created_at: 2025-08-05
---








  









### Delete {#delete style="tab-stops: 0pt"}

[] 

Delete Record

[] 

To delete the current record, use the following code snippet.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [if][ ([this].CurrentTable.CurrentRecord != [null])]            |
|                                                                                                                                                                                                |
| [        {]                                                                                                                                                |
|                                                                                                                                                                                                |
| [            [if] ([this].CurrentTable.CurrentRecordManager != [null])]                     |
|                                                                                                                                                                                                |
| [            {]                                                                                                                                            |
|                                                                                                                                                                                                |
| [                [if] (\![string].IsNullOrEmpty([this].GridGroupingControl1.DataSourceID))] |
|                                                                                                                                                                                                |
| [                {]                                                                                                                                        |
|                                                                                                                                                                                                |
| [                    [this].CurrentTable.CurrentRecordManager.DeleteCurrentRecord();]                                                 |
|                                                                                                                                                                                                |
| [                }]                                                                                                                                        |
|                                                                                                                                                                                                |
| [                [else]]                                                                                                              |
|                                                                                                                                                                                                |
| [                {]                                                                                                                                        |
|                                                                                                                                                                                                |
| [                    [this].CurrentTable.CurrentRecord.Delete();]                                                                     |
|                                                                                                                                                                                                |
| [                }]                                                                                                                                        |
|                                                                                                                                                                                                |
| [            }]                                                                                                                                            |
|                                                                                                                                                                                                |
| [            [else]]                                                                                                                  |
|                                                                                                                                                                                                |
| [            {]                                                                                                                                            |
|                                                                                                                                                                                                |
| [                [this].CurrentTable.CurrentRecord.Delete();]                                                                         |
|                                                                                                                                                                                                |
| [            }]                                                                                                                                            |
|                                                                                                                                                                                                |
| [}]                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [If][ [Me].CurrentTable.CurrentRecord [IsNot] [Nothing] [Then] ] |
|                                                                                                                                                                                                                                           |
| [    [If] [Me].CurrentTable.CurrentRecordManager [IsNot] [Nothing] [Then] ]                  |
|                                                                                                                                                                                                                                           |
| [        [If] [Not] [String].IsNullOrEmpty([Me].GridGroupingControl1.DataSourceID) [Then] ]  |
|                                                                                                                                                                                                                                           |
| [            [Me].CurrentTable.CurrentRecordManager.DeleteCurrentRecord() ]                                                                                                      |
|                                                                                                                                                                                                                                           |
| [        [Else] ]                                                                                                                                                                |
|                                                                                                                                                                                                                                           |
| [            [Me].CurrentTable.CurrentRecord.Delete() ]                                                                                                                          |
|                                                                                                                                                                                                                                           |
| [        [End] [If] ]                                                                                                                                       |
|                                                                                                                                                                                                                                           |
| [    [Else] ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [        [Me].CurrentTable.CurrentRecord.Delete() ]                                                                                                                              |
|                                                                                                                                                                                                                                           |
| [    [End] [If] ]                                                                                                                                           |
|                                                                                                                                                                                                                                           |
| [End][ [If] ]                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p85} 

[]{#related-topics}

