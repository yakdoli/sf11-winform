---
title: docimportexportanddocximportexport.md
original_path: WinForms_Docs/99_Uncategorized/docimportexportanddocximportexport.md
created_at: 2025-08-05
---






#####  Doc Import/Export and Docx Import/Export {#doc-importexport-and-docx-importexport style="tab-stops: 0pt"}

The .doc and .docx import features allow users to import .doc files and .docx files into the RichTextBoxAdv. It renders the content of the document as MS Word would render it. The .doc export and .docx export features actually expose the RichTextBoxAdv's document as a .doc or .docx file. To enable the .doc and .docx import/export feature in an application you should add **Syncfusion.RichTextDocIOParser.Silverlight dll** in the project. This DLL exposes the following methods to make use of the feature.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                        |
| [        RichTextBox.Document = [DocxImporting].ConvertToDocumentAdv(Stream, FormatType);]                                                                 |
|                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                        |
| **[\[C#\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                        |
| **[      ]**[DocxExporting][.ConvertToDocument(RichTextBox.Document, Stream, FormatType);] |
|                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Methods

  ------------------------ --------------------------------------------------- ------------------------------------ ------ -------------
  Method                   Description                                         Parameters                           Type   Return Type
  ConvertToDocumentAdv()   Converts .doc or .docx stream into DocumentAdv.     FormatType and doc or docx stream.   NA     DocumentAdv
  ConvertToDocument()      Returns the rich-text content as a Word document.   NA                                   NA     Void
  ------------------------ --------------------------------------------------- ------------------------------------ ------ -------------

###### 3.32.3.8.2.1         Limitations {#limitations style="tab-stops: 0pt"}

The .doc import/export and .docx import/export features have the following limitations:

1.  Hyperlinks do not work for tables of contents.

[]{#related-topics}

