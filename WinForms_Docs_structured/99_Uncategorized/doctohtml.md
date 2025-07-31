---
title: doctohtml.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\doctohtml.md
created_at: 2025-07-03
---








  









### Doc to HTML {#doc-to-html style="tab-stops: 0pt"}

You can now open or create Word documents and save to the HTML format, enabling HTML conversion by using DocIO.

 

The following example illustrates how to save a Word document to HTML format.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [WordDocument][ doc = [new] WordDocument([@\"..\\..\\DocToHTML.doc\"]);] |
|                                                                                                                                                                                                            |
| [HTMLExport htmlExport = [new] HTMLExport();]                                                                                                     |
|                                                                                                                                                                                                            |
| [htmlExport.SaveAsXhtml(doc,  [\"doctohtml_res.html\"]);]                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [Dim][ doc [As] [New] WordDocument([\"..\\..\\DocToHTML.doc\"])] |
|                                                                                                                                                                                                                        |
| [Dim][ htmlExport [As] [New] HTMLExport()]                                              |
|                                                                                                                                                                                                                        |
| [htmlExport.SaveAsXhtml(doc, [\"doctohtml_res.html\"])]                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Document Elements

 

DocIO supports the following document elements.

[] 


  ------------------------ ------------------------------ ----------- ---------------------------------------------------------------------
  Document Element         Attribute                      Supported   Notes
  Bookmark                 Position                       Yes         \-
  Border                   Color                          Yes         \-
  Border                   Distance from text             Yes         \-
  Border                   Line style                     Partial     Some line styles are rendered as solid.
  Border                   Line width                     Yes         \-
  Document Properties                                     Yes         \-
  Drawing objects          Shapes                         Partial     Images and horizontal rules are exported.
  Drawing objects          Text                           Partial     Text from text boxes and other shapes is rendered in the main text.
  Drawing objects          Images                         \-          \-
  Field                                                   Yes         Current field result is output, but the result is not recalculated.
  Footnotes and Endnotes                                  Yes         \-
  Form Field               Text input                     Yes         \-
  Header / Footer          Different per section          Partial     Only primary header is output at the beginning of a section.
  Hyperlink                External URL                   Yes         \-
  Hyperlink                Local                          Yes         \-
  Image                    Cropping                       Yes         \-
  Image                    Inline                         Yes         \-
  Image                    Scale                          Yes         \-
  List                     Custom bullets                 Yes         \-
  List                     Multi-level                    Yes         \-
  List                     Numbered                       Yes         \-
  List                     Restart numbering              Yes         \-
  List                     Standard bullets               Yes         \-
  Paragraph                Alignment                      Yes         \-
  Paragraph                Borders                        Yes         See Borders, for more details.
  Paragraph                First line indent or hanging   Yes         \-
  Paragraph                Keep together                  Yes         \-
  Paragraph                Keep with next                 Yes         \-
  Paragraph                Left and right indent          Yes         \-
  Paragraph                Line spacing                   Partial     All line spacing is output as atleast line spacing.
  Paragraph                Line spacing                   Yes         \-
  Paragraph                Page break before              Yes         \-
  Paragraph                Shading                        Yes         See Shading, for more details.
  Paragraph                Spacing before and after       Yes         \-
  Paragraph                Window control                 Yes         Output as both windows and orphans.
  Shading                  Background color               Partial     Solid background colors are supported.
  Shading                  Foreground color               Partial     Solid foreground color is used when background color is auto.
  Styles                   Paragraph styles               Yes         \-
  Styles                   Character styles               Yes         \-
  Styles                   List styles                    Partial     Not all formatting has effect. Considered in only inline styles.
  Table                    Alignment                      Yes         \-
  Table                    Cell margins                   Yes         \-
  Table                    Column widths                  Yes         \-
  Table                    Indent from left               Yes         \-
  Table                    Preferred width                Yes         \-
  Table                    Spacing between cells          Yes         \-
  Table Cell               Borders                        Partial     See Borders, for more details.
  Table Cell               Cell margins                   Partial     Only default table cell margins left and right are supported.
  Table Cell               Horizontal merge               Yes         \-
  Table Cell               Shading                        Partial     See Shading, for more details.
  Table Cell               Text direction                 Yes         \-
  Table Cell               Vertical alignment             Yes         \-
  Table Cell               Vertical merge                 Yes         \-
  Table Row                Height                         Yes         \-
  Table Row                Padding                        Yes         \-
  Text                     All caps                       Yes         \-
  Text                     Bold                           Yes         \-
  Text                     Character spacing              Yes         \-
  Text                     Color                          Yes         \-
  Text                     Emboss                         Partial     Rendered as bold.
  Text                     Engrave                        Partial     Rendered as bold.
  Text                     Font                           Yes         \-
  Text                     Hidden                         Yes         \-
  Text                     Highlighting                   Yes         \-
  Text                     Imprint                        Partial     Rendered as bold.
  Text                     Italic                         Yes         \-
  Text                     Line breaks                    Yes         \-
  Text                     Outline                        Partial     Rendered as bold.
  Text                     Page breaks                    Yes         \-
  Text                     Shading                        Partial     See Shading, for more details.
  Text                     Small caps                     Yes         \-
  Text                     Special symbols                Yes         \-
  Text                     Strike out                     Yes         \-
  Text                     Subscript / Superscript        Yes         \-
  Text                     Underline                      Partial     Underline types and colors are ignored.
  ------------------------ ------------------------------ ----------- ---------------------------------------------------------------------



[]{#_Doc_to_PDF} 

{border="0"}Notes: Currently Doc to Html conversion is not supported in Silverlight application.

 


[]{#related-topics}

