---
title: binarywithsoapformat.md
original_path: WinForms_Docs/99_Uncategorized/binarywithsoapformat.md
created_at: 2025-08-05
---






##### Binary with SOAP Format {#binary-with-soap-format style="tab-stops: 0pt"}

 

You can save or load the states of the docking elements from a binary file in SOAP format. To save or load the states of the elements from or to the binary file with SOAP format, use the following code.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [///][Save state in Binary file using SOAP Format][] |
|                                                                                                                                                                                                                                                   |
| [SOAPFormatter formatter1 = [new] SOAPFormatter();]                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [DocManager1.SaveDockState(formatter1, StorageFormat.Binary, [@\"c:\\docking_bin.bin\"]);]                                                                          |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [//Load state saved in Binary file using SOAP Format][]                                                                 |
|                                                                                                                                                                                                                                                   |
| [SOAPFormatter formatter1 = [new] SOAPFormatter();]                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [DocManager1.LoadDockState(formatter1, StorageFormat.Xml, [@\"c:\\docking_bin.bin\"]);]                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

