---
title: xmlwithsoapformat.md
original_path: WinForms_Docs/99_Uncategorized/xmlwithsoapformat.md
created_at: 2025-08-05
---






##### XML with SOAP Format {#xml-with-soap-format style="tab-stops: 0pt"}

 

You can save or load the states of the docking elements using an XML file in a SOAP format. To save the state in XML file using SOAP format, use the following code.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                            |
| [//Save state in XML using SOAP Format.][]       |
|                                                                                                                                                                            |
| [SoapFormatter formatter1 = [new] SoapFormatter();]                                             |
|                                                                                                                                                                            |
| [DocManager1.SaveDockState(formatter1, StorageFormat.Xml, [@\"C:\\docking_xml_soap.xml\"]);] |
|                                                                                                                                                                            |
| []                                                                                                                   |
|                                                                                                                                                                            |
| [//Load state saved in XML using SOAP Format.][] |
|                                                                                                                                                                            |
| [BinaryFormatter formatter1 = [new] BinaryFormatter();]                                         |
|                                                                                                                                                                            |
| [DocManager1.LoadDockState(formatter1, StorageFormat.Xml, [@\"c:\\docking_xml_soap.xml\"]);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

