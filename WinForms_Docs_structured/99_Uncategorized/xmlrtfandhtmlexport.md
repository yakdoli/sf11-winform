---
title: xmlrtfandhtmlexport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\xmlrtfandhtmlexport.md
created_at: 2025-07-03
---








  









### XML, RTF and HTML Export {#xml-rtf-and-html-export style="tab-stops: 0pt"}

[] 

Edit Control has the ability to export its contents and its associated [syntax highlighting]{.UGHyperlink} information into XML, RTF or HTML formats. This allows the user to share text associated with the Edit Control along with its attributes such as syntax highlighting, line numbers, underlines and many such useful features in universally accepted formats like XML, RTF and HTML.

 

The following methods can implemented for this purpose.

 


  --------------------- ----------------------------------------------------------------------------------------------
  Edit Control Method   Description
  SaveAsXML             Export the Edit Control\'s contents into XML format and save it into any desired XML file.
  SaveAsRTF             Export the Edit Control\'s contents into RTF format and save it into any desired RTF file.
  SaveAsHTML            Export the Edit Control\'s contents into HTML format and save it into any desired HTML file.
  --------------------- ----------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                     |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [// Export the Edit Control\'s contents into XML format and save it into a XML file.]                            |
|                                                                                                                                                                    |
| [this][.editControl1.SaveAsXML([\"testXML.xml\"]);]    |
|                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                    |
| [// Export the Edit Control\'s contents into RTF format and save it into a RTF file.]                            |
|                                                                                                                                                                    |
| [this][.editControl1.SaveAsRTF([\"testRTF.rtf\"]);]    |
|                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                    |
| [// Export the Edit Control\'s contents into HTML format and save it into a HTML file.]                          |
|                                                                                                                                                                    |
| [this][.editControl1.SaveAsHTML([\"testHTML.html\"]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                              |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [\' Export the Edit Control\'s contents into XML format and save it into a XML file.]                         |
|                                                                                                                                                                 |
| [Me][.editControl1.SaveAsXML([\"testXML.xml\"])]    |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [\' Export the Edit Control\'s contents into RTF format and save it into a RTF file.]                         |
|                                                                                                                                                                 |
| [Me][.editControl1.SaveAsRTF([\"testRTF.rtf\"])]    |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [\' Export the Edit Control\'s contents into HTML format and save it into a HTML file.]                       |
|                                                                                                                                                                 |
| [Me][.editControl1.SaveAsHTML([\"testHTML.html\"])] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Edit Control is also capable of providing XML, RTF and HTML source code for generating documents in the corresponding formats by using the following methods.

[] 


  --------------------- ----------------------------------------------------------------------------------
  Edit Control Method   Description
  GetTextAsRTF          Gets the source code to generate XML document for the text in the Edit Control.
  GetTextAsXML          Gets the source code to generate RTF document for the text in the Edit Control.
  GetTextAsHTML         Gets the source code to generate HTML document for the text in the Edit Control.
  --------------------- ----------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [// Gets the source code to generate XML document.]                                                        |
|                                                                                                                                                              |
| [this][.editControl1.GetTextAsXML();]                                   |
|                                                                                                                                                              |
| []                                                                                                                       |
|                                                                                                                                                              |
| [// Gets the source code to generate XML document for the text range specified.]                           |
|                                                                                                                                                              |
| [this][.editControl1.GetTextAsXML(coordinatePoint1, coordinatePoint2);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [\' Gets the source code to generate XML document.]                                                     |
|                                                                                                                                                           |
| [Me][.editControl1.GetTextAsXML()]                                   |
|                                                                                                                                                           |
| []                                                                                                                    |
|                                                                                                                                                           |
| [\' Gets the source code to generate XML document for the text range specified.]                        |
|                                                                                                                                                           |
| [Me][.editControl1.GetTextAsXML(coordinatePoint1, coordinatePoint2)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample demonstrating the above feature is available in the below sample installation path.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Text Export\\ExportDemo***

[]{#p84} 

[]{#related-topics}

