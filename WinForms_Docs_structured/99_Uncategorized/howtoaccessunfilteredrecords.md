---
title: howtoaccessunfilteredrecords.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaccessunfilteredrecords.md
created_at: 2025-07-03
---






#### How to access unfiltered records {#how-to-access-unfiltered-records style="tab-stops: 0pt"}

[] 

This can be done using the following code snippet.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [foreach][(Record r [in] [this].gridGroupingControl1.Table.Records)] |
|                                                                                                                                                                                                     |
| [{]                                                                                                                                                             |
|                                                                                                                                                                                                     |
| [      [foreach](Record fr [in] [this].gridGroupingControl1.Table.FilteredRecords)]              |
|                                                                                                                                                                                                     |
| [      {]                                                                                                                                                       |
|                                                                                                                                                                                                     |
| [            [if](r!=fr)]                                                                                                                  |
|                                                                                                                                                                                                     |
| [            {]                                                                                                                                                 |
|                                                                                                                                                                                                     |
| [                  Console.WriteLine(r.Info);]                                                                                                                  |
|                                                                                                                                                                                                     |
| [            }]                                                                                                                                                 |
|                                                                                                                                                                                                     |
| [      }]                                                                                                                                                       |
|                                                                                                                                                                                                     |
| [}]                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [For][ [Each] r [As] Record [In] [Me].gridGroupingControl1.Table.Records] |
|                                                                                                                                                                                                                                                    |
| [    [For] [Each] fr [As] Record [In] [Me].gridGroupingControl1.Table.FilteredRecords]                |
|                                                                                                                                                                                                                                                    |
| [        [If] [Not] r [Is] fr [Then]]                                                                                      |
|                                                                                                                                                                                                                                                    |
| [            Console.WriteLine(r.Info)]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        [End] [If]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [    [Next] fr]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [Next][ r]                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p698} 

 

[]{#related-topics}

