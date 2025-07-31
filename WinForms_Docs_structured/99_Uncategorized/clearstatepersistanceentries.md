---
title: clearstatepersistanceentries.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clearstatepersistanceentries.md
created_at: 2025-07-03
---






#### Clear StatePersistance Entries {#clear-statepersistance-entries style="tab-stops: 0pt"}

 

In **StatePersistence** of **DockingManager** we have five ways to store the state. Similarly, we have ways to clear those entries as given below

 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                   |
| [//Deletes the Registry Entries.]                                                               |
|                                                                                                                                                   |
| **[DockingManager]**[.DeleteDockState();]                                 |
|                                                                                                                                                   |
| [            ]                                                                                                |
|                                                                                                                                                   |
| [//Deletes the persistance file in Isolatedstorage location.]                                   |
|                                                                                                                                                   |
| **[DockingManager]**[.DeleteInternalIsolatedStorage();]                   |
|                                                                                                                                                   |
| [            ]                                                                                                |
|                                                                                                                                                   |
| [//Deletes the specified state file.]                                                           |
|                                                                                                                                                   |
| **[DockingManager]**[.DeleteDockState(filename);[]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

 

Refer Also

[]{.UGHyperlink}

[[]]{.UGHyperlink} 

[[]]{.UGHyperlink} 

[]{#related-topics}

