---
title: rtftodoc.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\rtftodoc.md
created_at: 2025-07-03
---








  









### RTF to Doc {#rtf-to-doc style="tab-stops: 0pt"}

 

Essential DocIO allows to import the RTF document directly into the word document.  

 

The following code illustrates how RTF file can be opened and saved as a word document.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [//Opening the RTF file]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [WordDocument][ doc = [new] [WordDocument]([\"Sample.rtf\"], [FormatType].Rtf);] |
|                                                                                                                                                                                                                                                                       |
| [//Saving the RTF file as a word document]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [doc.Save ([\"RtfToDoc_Res.doc\"],[FormatType].Doc);]                                                                                                                             |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [\'Opening the RTF file]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                        |
| [Dim][ doc [As] [New ]WordDocument([\"Sample.rtf\"], [FormatType].Rtf)] |
|                                                                                                                                                                                                                                                        |
| [\'Saving the RTF file as a word document]                                                                                                                                                           |
|                                                                                                                                                                                                                                                        |
| [doc.Save([\"RtfToDoc_Res.doc\"], FormatType.Doc);]                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Supported Elements

[ ]This feature provides support for the following elements:

 

[·      ]Paragraph and Character Formatting

[·      ]Tables

[·      ]Bookmarks

[·      ]Headers and Footers

[·      ]Images

[·      ]List

[·      ]Page setting

[·      ]Multi column text

[·      ]Breaks

[·      ]Document properties

[·      ]Fields

 

Fields

This feature supports the preservation of fields in Rtf to Doc conversion.[]

 

Paragraph and Character Formatting

This feature supports almost all the paragraph and character formatting. The supported formatting features are:[]

[] 

[·      ]Paragraph borders

[·      ]Indentation and Pagination

[·      ]Spacing and Tabs

[·      ]Left, Right and Center justification

[·      ]Font styles(Bold, Italic, Underline, Strike through)

[·      ]Font sizeand font name for the character

[·      ]Text highlighting and Text color    

 

+-----------------------------------------------------------------------+
| *[Known Limitation:]*                         |
|                                                                       |
| [·      ]Subscript and Superscript       |
|                                                                       |
| [·      ]Revision tracking               |
|                                                                       |
|                                                                       |
+-----------------------------------------------------------------------+

*[]* 

 

Tables

This feature supports both simple and the nested tables. This feature also provides support for Text formatting, Paragraph formatting and  images inside the tables

 

+-----------------------------------------------------------------------------------------------------+
| *[Known Limitation]*                                                        |
|                                                                                                     |
| [·      ]Tables styles and 3D border for the tables are not supported. |
+-----------------------------------------------------------------------------------------------------+

[] 

Bookmarks

This feature fully supports  the bookmark present in the document.

[] 

Headers and Footers

This feature supports page headers and footers.  The Page header and footer can contain paragraphs, tables and images.

 

Images

This feature support images present in the RTF document along with their position and size.

 

+------------------------------------------------------------------------------------------+
| *[Known Limitation:]*                                            |
|                                                                                          |
| [·      ]Image Present inside the shapes are not supported. |
|                                                                                          |
|                                                                                          |
+------------------------------------------------------------------------------------------+

 

List

This feature support bullets, numbered and multi level bulleted list along with their alignment and indentation.

 

+-----------------------------------------------------------------------+
| *[Known limitaion:]*                          |
|                                                                       |
| [·      ]Image bullets are not supported |
|                                                                       |
|                                                                       |
+-----------------------------------------------------------------------+

 

Page Settings

This feature support page settings such as Margin, Orientation, Paper size,Header distance and Footer distance.

 

+------------------------------------------------------------------------------------------------------------+
| *[Known Limitation:]*                      |
|                                                                                                            |
| [·      ]Background image and background color for the page is not supported. |
|                                                                                                            |
|                                                                                                            |
+------------------------------------------------------------------------------------------------------------+

[] 

Multi Column text

This feature fully supports multi column text within theRTF document.[]

 

Breaks

This feature supports breaks such as column break, section break, line break and page break.

 

Document properties

This feature supports  document properties present in the RTF document.

**[]** 

Unsupported elements

The following are the unsupported elements which will be supported in our future release:

[] 

[·      ]Shapes and Auto Shapes

[·      ]Footnotes and End notes

[·      ]Comments

[·      ]Table of contents

[·      ]Hyperlinks

[·      ]Table styles

[·      ]OLE objects

[·      ]Document protection

[·      ]RTL support

[·      ]Water marks

[·      ]Symbols


 

{border="0"}Notes: Currently RTF to Doc conversion is not supported in Silverlight application.

 


[]{#related-topics}

