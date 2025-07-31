---
title: docxsupport1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\docxsupport1.md
created_at: 2025-07-03
---








  









## Docx Support {#docx-support style="tab-stops: 0pt"}

 

Microsoft introduced the .docx file format in its new Office and Word applications to replace the commonly used doc format. Essential DocIO now provides support for.docx files. Docx files are created using the same APIs as for .doc files using Essential DocIO. Essential DocIO provides support for:

 

[·      ]Creating a .docx file from scratch

[·      ]Read/Modify a .docx file

 

Creating a .docx file

To create a .docx file:

1.   Create a word document using Essential DocIO APIs.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
|                                                                                                                                                                                          |
|                                                                                                                                                                                          |
| [WordDocument][ document = [new] [WordDocument]();] |
|                                                                                                                                                                                          |
| [//Add a new section to the document.]                                                                                                 |
|                                                                                                                                                                                          |
| [IWSection][ section = document.AddSection();]                                                   |
|                                                                                                                                                                                          |
| [//Adding a new paragraph to the section.]                                                                                             |
|                                                                                                                                                                                          |
| [IWParagraph][ paragraph = section.AddParagraph();]                                              |
|                                                                                                                                                                                          |
| [//Insert Text into the paragraph]                                                                                                     |
|                                                                                                                                                                                          |
| [paragraph.AppendText( [\"Hello World!\"] );]                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Create an instance of SaveFile dialog.

 

The following lines of code create an instance of SaveFile Dialog and set the properties and display the Save dialog on the screen.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
|                                                                                                                                                                                        |
|                                                                                                                                                                                        |
| [SaveFileDialog][ sfd = [new] [SaveFileDialog]()] |
|                                                                                                                                                                                        |
| [{]                                                                                                                                                |
|                                                                                                                                                                                        |
| [   Filter = [\"Docx files (\*.docx)\|\*.docx\|All files (\*.\*)\|\*.\*\"],]                                               |
|                                                                                                                                                                                        |
| [   DefaultExt = [\".docx\"],]                                                                                             |
|                                                                                                                                                                                        |
| [   FilterIndex = 1]                                                                                                                               |
|                                                                                                                                                                                        |
| [};]                                                                                                                                               |
|                                                                                                                                                                                        |
| [if][ (sfd.ShowDialog() == [true])]                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

3.   Save the document as .docx format.

 

The following code snippet will save the Word document.

 

+---------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                |
|                                                                                                               |
|                                                                                                               |
|                                                                                                               |
| [{]                                                                       |
|                                                                                                               |
| [   [using] (Stream stream = sfd.OpenFile())]        |
|                                                                                                               |
| [   {]                                                                    |
|                                                                                                               |
| [      document.Save(stream, [FormatType].Docx);] |
|                                                                                                               |
| [   }]                                                                    |
|                                                                                                               |
| [}]                                                                       |
+---------------------------------------------------------------------------------------------------------------+

 

4.   Run the application. The .doc file is converted to .docx file.

 

The same can be achieved using the VB.Net code as well.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                        |
|                                                                                                                                                                           |
|                                                                                                                                                                           |
|                                                                                                                                                                           |
| [Dim][ document [As] [New] WordDocument()] |
|                                                                                                                                                                           |
| [\'Add a new section to the document. ]                                                                                 |
|                                                                                                                                                                           |
| [Dim][ section [As] IWSection = document.AddSection()]          |
|                                                                                                                                                                           |
| [Adding a new paragraph to the section. ]                                                                               |
|                                                                                                                                                                           |
| [Dim][ paragraph [As] IWParagraph = section.AddParagraph()]     |
|                                                                                                                                                                           |
| [\'Insert Text into the paragraph ]                                                                                     |
|                                                                                                                                                                           |
| [paragraph.AppendText([\"Hello World!\"])]                                                                    |
|                                                                                                                                                                           |
| [Dim][ sfd [As] [New] SaveFileDialog()]    |
|                                                                                                                                                                           |
| [If][ sfd.ShowDialog() = [True] [Then]]    |
|                                                                                                                                                                           |
| [  [Using] stream [As] Stream = sfd.OpenFile()]                                             |
|                                                                                                                                                                           |
| [       document.Save(stream, FormatType.Docx)]                                                                                       |
|                                                                                                                                                                           |
| [   [End] [Using]]                                                                          |
|                                                                                                                                                                           |
| [End][ [If]]                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Saving a .doc File as .docx

DocIO also has the ability to save the doc files into .docx format (i.e, Microsoft Word 2007 files format). All the elements supported by .Doc are supported in Docx. Some of the supported elements are listed below.

1.   Creating an instance of Word document.

The following code snippet creates an instance of the word document and opens the word document named SourceDocument.doc. The FormatType.Doc specifies that the document is of type Word 97-2003.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
|                                                                                                                                                                                          |
|                                                                                                                                                                                          |
| [WordDocument][ document = [new] [WordDocument]();] |
|                                                                                                                                                                                          |
| [document.Open("SourceDocument.doc", [FormatType].Doc);]                                                                     |
|                                                                                                                                                                                          |
| [SaveFileDialog][ sfd = [new] [SaveFileDialog]()]   |
|                                                                                                                                                                                          |
| [{]                                                                                                                                                  |
|                                                                                                                                                                                          |
| [   Filter = [\"Docx files (\*.docx)\|\*.docx\|All files (\*.\*)\|\*.\*\"],]                                                 |
|                                                                                                                                                                                          |
| [   DefaultExt = [\".docx\"],]                                                                                               |
|                                                                                                                                                                                          |
| [   FilterIndex = 1]                                                                                                                                 |
|                                                                                                                                                                                          |
| [};]                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Save the document as .docx format.

 

The following code snippet will display the Save dialog on the screen and save the Word document.

+-----------------------------------------------------------------------+
| **[\[C#\]]**        |
|                                                                       |
|                                                                       |
|                                                                       |
| if (sfd.ShowDialog() == true)                                         |
|                                                                       |
| {                                                                     |
|                                                                       |
|    using (Stream stream = sfd.OpenFile())                             |
|                                                                       |
|    {                                                                  |
|                                                                       |
|       document.Save(stream, FormatType.Docx);                         |
|                                                                       |
|    }                                                                  |
|                                                                       |
| }                                                                     |
+-----------------------------------------------------------------------+

3.   Run the application. The .doc file is converted to .docx file.

The same can be achieved using the VB.Net code as well.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                        |
|                                                                                                                                                                           |
| [Dim][ document [As] [New] WordDocument()] |
|                                                                                                                                                                           |
| [document.Open([\"SourceDocument.doc\"], FormatType.Doc)]                                                     |
|                                                                                                                                                                           |
| [Dim][ sfd [As] [New] SaveFileDialog()]    |
|                                                                                                                                                                           |
| [If][ sfd.ShowDialog() = [True] [Then]]    |
|                                                                                                                                                                           |
| [   [Using] stream [As] Stream = sfd.OpenFile()]                                            |
|                                                                                                                                                                           |
| [       document.Save(stream, FormatType.Docx)]                                                                                       |
|                                                                                                                                                                           |
| [   [End] [Using]]                                                                          |
|                                                                                                                                                                           |
| [End][ [If]]                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Reading/Modifying .docx File

Once a file is saved into .docx format, Essential DocIO provides support for reading and modifying .docx files. Docx files can be read using the same API as that of .doc files; except for the format in which it is opened.

The control uses the following API to read the .docx format.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [WordDocument][ doc = [new] [WordDocument]([\"sample.docx\"], [FormatType].Docx);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [Dim][ doc [As] [New] WordDocument([\"sample.docx\"], FormatType.Docx)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the file. You will be able to open and edit a .docx file.

[]{#related-topics}

