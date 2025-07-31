---
title: streamsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\streamsupport.md
created_at: 2025-07-03
---








  









### Stream Support {#stream-support style="tab-stops: 0pt"}

[]{#p32} 

Essential DocIO provides support to open or save the created Word document into the **Memory Stream** and **File Stream**. Using this, you can open or save the document in the database or make changes to the document without saving to disk.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                            |
|                                                                                                                                                            |
| **[]**                                                                                                   |
|                                                                                                                                                            |
| [//Create a Memory Stream.]                                                                              |
|                                                                                                                                                            |
| [MemoryStream memStream = new MemoryStream();                       ]                                                  |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [//Save the document into memory stream.]                                                                |
|                                                                                                                                                            |
| [document.Save ( memStream );]                                                                                         |
|                                                                                                                                                            |
| []                                                                                                     |
|                                                                                                                                                            |
| [//Move the pointer to the first position]                                                               |
|                                                                                                                                                            |
| [memStream.Seek ( 0 , SeekOrigin.Begin );]                                                                             |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [//Create a file Stream]                                                                                 |
|                                                                                                                                                            |
| [FileStream fs = new FileStream(\"Sample.doc\",FileMode.Create);]                                                      |
|                                                                                                                                                            |
| [memStream.WriteTo(fs);]                                                                                               |
|                                                                                                                                                            |
| []                                                                                                                     |
|                                                                                                                                                            |
| [//Open the Word document from stream]                                                                   |
|                                                                                                                                                            |
| [WordDocument sourceDoc = [new] WordDocument([memStream], FormatType.Doc);] |
|                                                                                                                                                            |
| []                                                                                                                     |
|                                                                                                                                                            |
| [//Close the Streams.]                                                                                   |
|                                                                                                                                                            |
| [memStream.Close();]                                                                                                   |
|                                                                                                                                                            |
| []                                                                                                                     |
|                                                                                                                                                            |
| [fs.Close();]                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [\'Create a Memory Stream.]                                                                                                                                             |
|                                                                                                                                                                                                                           |
| [Dim][ memStream [As] [New] MemoryStream()]                                                |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\'Save the document into memory stream.]                                                                                                                               |
|                                                                                                                                                                                                                           |
| [ document.Save(memStream)]                                                                                                                                                           |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\'Move the pointer to the first position]                                                                                                                              |
|                                                                                                                                                                                                                           |
| [ memStream.Seek(0, SeekOrigin.Begin)]                                                                                                                                                |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\'Create a file Stream]                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [Dim][ fs [As] [New] FileStream([\"Sample.doc\"], FileMode.Create)] |
|                                                                                                                                                                                                                           |
| [ memStream.WriteTo(fs)]                                                                                                                                                              |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\'Open the Word document from stream]                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [Dim][ sourceDoc [As] [New] WordDocument(memStream, FormatType.Doc)]                       |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\'Close the Streams.]                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [ memStream.Close()]                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [ fs.Close()]                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

