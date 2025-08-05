---
title: transformpdf.md
original_path: WinForms_Docs/99_Uncategorized/transformpdf.md
created_at: 2025-08-05
---








  









### Transform PDF {#transform-pdf style="tab-stops: 0pt"}

 

The pdf pages can be converted to PdfTemplate object if you want to create a  or just place a few pages onto a single page like an image. The template can be created using the below code.

 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                          |
| []                                                                                                   |
|                                                                                                                                          |
| [PdfTemplate][ template = lpage.CreateTemplate(); ] |
+------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                  |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [Dim][ template [As] PdfTemplate =  lpage.CreateTemplate()] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

{border="0"}Note: This template can be scaled, rotated, placed at different coordinates, and so on.


[] 

Restrictions

 

This above process can convert annotations also but with some limitations as follows

 

[·      ]It does not pay attention to the fields

[·      ]It takes the first appearance stream from the annotation\'s normal appearance dictionary, (if it isn\'t a stream)

[·      ]It places the appearance stream as a template on the page according to its states, say, on, off or some other states.

[·      ]This may lead to unexpected results.

 

For more details, see .

 

 

[]{#related-topics}

