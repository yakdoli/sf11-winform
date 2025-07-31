---
title: registry.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\registry.md
created_at: 2025-07-03
---






##### Registry {#registry style="tab-stops: 0pt"}

 

You can save or load the States of the DockingManager elements from the registry. To save or load the states to or from the system registry respectively, use the following code.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                  |
| [//Save state in System Registry.][]   |
|                                                                                                                                                                  |
| [BinaryFormatter formatter1 = [new] BinaryFormatter();]                               |
|                                                                                                                                                                  |
| [DocManager1.SaveDockState(formatter1);]                                                                   |
|                                                                                                                                                                  |
| []                                                                                                         |
|                                                                                                                                                                  |
| [//Load state from System Registry.][] |
|                                                                                                                                                                  |
| [BinaryFormatter formatter1 = [new] BinaryFormatter();]                               |
|                                                                                                                                                                  |
| [DocManager1.LoadDockState(formatter1);]                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

