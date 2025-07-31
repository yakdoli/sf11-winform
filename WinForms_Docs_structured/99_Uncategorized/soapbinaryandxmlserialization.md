---
title: soapbinaryandxmlserialization.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\soapbinaryandxmlserialization.md
created_at: 2025-07-03
---






##### SOAP, Binary and XML Serialization {#soap-binary-and-xml-serialization style="tab-stops: 0pt"}

[] 

Essential Grid control has support for serialization and de-serialization of the grid\'s schema information.


 

{border="0"}Note: Serialization is the process of saving the state of an object as a stream of bytes. The reverse of this process is called deserialization.


[] 

Grid control supports three different types of serialization techniques namely:

[] 

[·      ]**SOAP**-Helps convert the grid schema information to SOAP format.

[·      ]**Binary**-Helps convert the grid schema information to binary format.

[·      ]**XML**-Helps convert the grid schema information to XML format.

[] 

[·      ]**SOAP**

[] 

[o  ]Following code example illustrates serialization of grid schema information by using SOAP technique.

[] 

1.   Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                           |
|                                                                                                                                          |
| []                                                                                     |
|                                                                                                                                          |
| [this][.gridControl1.Model.SaveSoap(dlg.FileName);] |
+------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                    |
|                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                       |
| [Me][.gridControl1.Model.SaveSoap(dlg.FileName)] |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[o  ]Following code example illustrates deserialization of grid schema information by using SOAP technique.

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [this][.gridControl1.Model = [GridModel].LoadSoap(dlg.FileName);] |
|                                                                                                                                                                                |
| [this][.gridControl1.Refresh();    ]                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                |
|                                                                                                                                                   |
| []                                                                                              |
|                                                                                                                                                   |
| [Me][.gridControl1.Model = GridModel.LoadSoap(dlg.FileName)] |
|                                                                                                                                                   |
| [Me][.gridControl1.Refresh()]                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**Binary**

[] 

[o  ]Following code example illustrates serialization of grid schema information by using Binary technique.

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                             |
|                                                                                                                                            |
| []                                                                                       |
|                                                                                                                                            |
| [this][.gridControl1.Model.SaveBinary(dlg.FileName);] |
+--------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                       |
|                                                                                                                                          |
| []                                                                                     |
|                                                                                                                                          |
| [Me][.gridControl1.Model.SaveBinary(dlg.FileName);] |
+------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[o  ]Following code example illustrates deserialization of grid schema information by using Binary technique.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [this][.gridControl1.Model = [GridModel].LoadBinary(dlg.FileName);] |
|                                                                                                                                                                                  |
| [this][.gridControl1.Refresh();]                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [Me][.gridControl1.Model = GridModel.LoadBinary(dlg.FileName)] |
|                                                                                                                                                     |
| [Me][.gridControl1.Refresh()]                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**XML**

[] 

[o  ]Following code example illustrates serialization of grid schema information by using XML technique.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [Stream][ s = [null];]                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [s = [File].Create(dlg.FileName);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [XmlWriter][ xw = [new] [XmlTextWriter](s, System.Text.[Encoding].Default);]                                  |
|                                                                                                                                                                                                                                                                            |
| [XmlSerializer][ xs = [new] System.Xml.Serialization.[XmlSerializer]([this].gridControl1.Model.Data.GetType());] |
|                                                                                                                                                                                                                                                                            |
| [xs.Serialize(xw, [this].gridControl1.Model.Data);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [s.Close();]                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [Dim][ s [As] Stream = [Nothing]]                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| [s = File.Create(dlg.FileName)]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| [Dim][ xw [As] XmlWriter = [New] XmlTextWriter(s, System.Text.Encoding.Default)]                                                          |
|                                                                                                                                                                                                                                                                          |
| [Dim][ xs [As] XmlSerializer = [New] System.Xml.Serialization.XmlSerializer([Me].gridControl1.Model.Data.GetType())] |
|                                                                                                                                                                                                                                                                          |
| [xs.Serialize(xw, [Me].gridControl1.Model.Data)]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                          |
| [s.Close()]                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[o  ]Following code example illustrates deserialization of grid schema information by using XML technique.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [Stream][ s = [null];]                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [s = [File].OpenRead(dlg.FileName);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| [XmlReader][ xw = [new] [XmlTextReader](s);]                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [XmlSerializer][ xs = [new] System.Xml.Serialization.[XmlSerializer]([this].gridControl1.Model.Data.GetType());] |
|                                                                                                                                                                                                                                                                            |
| [s.Close();]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| [this][.gridControl1.Model.Data = ([GridData])xs.Deserialize(xw);]                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [this][.gridControl1.Refresh();]                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [Dim][ s [As] Stream = [Nothing]]                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| [s = File.OpenRead(dlg.FileName)]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                          |
| [Dim][ xw [As] XmlReader = [New] XmlTextReader(s)]                                                                                        |
|                                                                                                                                                                                                                                                                          |
| [Dim][ xs [As] XmlSerializer = [New] System.Xml.Serialization.XmlSerializer([Me].gridControl1.Model.Data.GetType())] |
|                                                                                                                                                                                                                                                                          |
| [s.Close()]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [Me][.gridControl1.Model.Data = [CType](xs.Deserialize(xw), GridData)]                                                                                         |
|                                                                                                                                                                                                                                                                          |
| [Me][.gridControl1.Refresh()]                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][143][: Serialization Illustrated]*

***[]*** 

A sample demonstrating this feature is available under the following sample installation path.

[] 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Serialization\\Serialize Grid Control Demo***

 

[]{#p303} 

 

[]{#related-topics}

