---
title: xmlwithbinaryformat.md
original_path: WinForms_Docs/99_Uncategorized/xmlwithbinaryformat.md
created_at: 2025-08-05
---






##### XML with Binary Format {#xml-with-binary-format style="tab-stops: 0pt"}

 

The DockingManager enables you to save or load the states of the elements on an XML file in binary format. To save the state in XML using binary format, use the following code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                              |
| [//Save state in XML using Binary Format.][]       |
|                                                                                                                                                                              |
| [BinaryFormatter formatter1 = [new] BinaryFormatter();]                                           |
|                                                                                                                                                                              |
| [DocManager1.SaveDockState(formatter1, StorageFormat.Xml, [@\"C:\\docking_xml.xml\"]);]        |
|                                                                                                                                                                              |
| [//Load state saved in XML using Binary Format.][] |
|                                                                                                                                                                              |
| [BinaryFormatter formatter1 = [new] BinaryFormatter();]                                           |
|                                                                                                                                                                              |
| [DocManager1.LoadDockState(formatter1, StorageFormat.Xml, [@\"c:\\docking_xml.xml\"]);]        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

