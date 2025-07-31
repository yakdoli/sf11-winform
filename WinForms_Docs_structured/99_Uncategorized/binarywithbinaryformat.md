---
title: binarywithbinaryformat.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\binarywithbinaryformat.md
created_at: 2025-07-03
---






##### Binary with Binary format {#binary-with-binary-format style="tab-stops: 0pt"}

 

DockingManager also supports saving and loading the states of its elements in a binary file with binary format. To save or load using binary file with binary format, use the following code.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                      |
| [//Save state in Binary file using Binary Format.][]       |
|                                                                                                                                                                                      |
| [BinaryFormatter formatter1 = [new] BinaryFormatter();]                                                   |
|                                                                                                                                                                                      |
| [DocManager1.SaveDockState(formatter1, StorageFormat.Binary, [@\"c:\\docking_bin.bin\"]);]             |
|                                                                                                                                                                                      |
| [//Load state saved in Binary file using Binary Format.][] |
|                                                                                                                                                                                      |
| [BinaryFormatter formatter1 = [new] BinaryFormatter();]                                                   |
|                                                                                                                                                                                      |
| [DocManager1.LoadDockState(formatter1, StorageFormat.Xml, [@\"c:\\docking_bin.bin\"]);]                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

