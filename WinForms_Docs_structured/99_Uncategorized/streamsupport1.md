---
title: streamsupport1.md
original_path: WinForms_Docs/99_Uncategorized/streamsupport1.md
created_at: 2025-08-05
---






#### Stream Support {#stream-support style="tab-stops: 0pt"}

 

Essential PDF provides support to open or save the created PDF document into a memory stream or file stream. MemoryStream and FileStream classes can be used for this purpose.

 

This feature enables the following:

 

[·      ]Open or save the PDF document in the database

[·      ]Make changes to your document without saving it to disk

 

The following code illustrates how to create a memory stream or file stream and save the pdf document into those streams.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [//Create a Memory Stream.]                                                                                                           |
|                                                                                                                                                                                         |
| [System.IO.[MemoryStream] memStream = [new] MemoryStream();]                                              |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [//Save the Stream to memory.]                                                                                                        |
|                                                                                                                                                                                         |
| [document.Save(memStream);]                                                                                                                         |
|                                                                                                                                                                                         |
| [memStream.Seek(0, SeekOrigin.Begin);]                                                                                                              |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [//Create a file Stream]                                                                                                              |
|                                                                                                                                                                                         |
| [System.IO.[FileStream] fs = [new] FileStream([\"Sample.pdf\"], FileMode.Create);] |
|                                                                                                                                                                                         |
| [memStream.WriteTo(fs);]                                                                                                                            |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [//Close the Streams.]                                                                                                                |
|                                                                                                                                                                                         |
| [memStream.Close();]                                                                                                                                |
|                                                                                                                                                                                         |
| [fs.Close();]                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [\'Create a Memory Stream.]                                                                                                                                                          |
|                                                                                                                                                                                                                                        |
| [Dim][ memStream [As] MemoryStream = [New] MemoryStream()]                                              |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [\'Save the Stream to memory.]                                                                                                                                                       |
|                                                                                                                                                                                                                                        |
| [document.Save (memStream, FormatType.Doc)]                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
| [memStream.Seek (0, SeekOrigin.Begin)]                                                                                                                                                             |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [\'Create a file Stream]                                                                                                                                                             |
|                                                                                                                                                                                                                                        |
| [Dim][ fs [As] FileStream = [New] FileStream([\"Sample.doc\"], FileMode.Create)] |
|                                                                                                                                                                                                                                        |
| [memStream.WriteTo(fs)]                                                                                                                                                                            |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [\'Close the Streams.]                                                                                                                                                               |
|                                                                                                                                                                                                                                        |
| [memStream.Close()]                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [fs.Close()]                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

