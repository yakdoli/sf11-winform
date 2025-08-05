---
title: doctortf.md
original_path: WinForms_Docs/99_Uncategorized/doctortf.md
created_at: 2025-08-05
---








  









### Doc to RTF {#doc-to-rtf style="tab-stops: 0pt"}

 

You can now open or create Word documents and save to the .RTF format, enabling RTF conversion by using DocIO.

 

The following example illustrates how to save a Word document to RTF format.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                |
| [WordDocument][ doc = [new] WordDocument([\"sample.doc\"]);] |
|                                                                                                                                                                                                |
| [doc.Save( [\"samplertf.rtf\"], [FormatType].Rtf );]                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                          |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                             |
| [Dim][ doc [As] [New] WordDocument([\"sample.doc\"])] |
|                                                                                                                                                                                                             |
| [doc.Save( [\"samplertf.rtf\"], [FormatType].Rtf )]                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Document Elements

 

DocIO supports the following document elements.

 

[·      ]Element Name

[·      ]Main Document and Document Properties

[·      ]Paragraph

[·      ]Table

[·      ]Picture

[·      ]Header / Footer

[·      ]Field (Simple)

[·      ]TOC Field

[·      ]Bookmark

[·      ]Break (Line, Page)

[·      ]Section Property

[·      ]Paragraph Format

[·      ]Table Format

[·      ]Character Format

[·      ]Text Box

[·      ]Form Fields

[·      ]Document Background

[·      ]Watermark

[·      ]Nested Table

[·      ]Footnote / Endnote

[·      ]Lists

[·      ]Hyperlink

[·      ]Symbols \[Not all symbols are supported\]

 

DocIO does not support the following document elements.

 

[·      ]OLE Object

[·      ]RTL

 


{border="0"}[]{#_Doc_to_HTML} Note: Currently Doc to RTF conversion is not supported in Silverlight application.Doc to HTML


[]{#related-topics}

