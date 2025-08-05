---
title: textareaelement.md
original_path: WinForms_Docs/99_Uncategorized/textareaelement.md
created_at: 2025-08-05
---








  









### TEXTAREA Element {#textarea-element style="tab-stops: 0pt"}

[] 

The **TEXTAREA** element is used to define a multiline textbox, allowing the user to enter unlimited characters. The **TEXTAREAElementImpl** class is invoked to define the properties and methods of the element.

[] 

Properties

**[]** 

[·      ]**UserControl**: Gets / sets the user control instance for the particular input element declared by the user

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [// UserControl property gets the user control instance for the particular input element declared by the  // user.]                                                                                            |
|                                                                                                                                                                                                                                                                                  |
| [Hashtable][ htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                              |
|                                                                                                                                                                                                                                                                                  |
| [TEXTAREAElementImpl][ txt = htmlelements\[[\"txt\"]\] [as] [TEXTAREAElementImpl];] |
|                                                                                                                                                                                                                                                                                  |
| [this][.txt.UserControl.CustomControl.Text = [\"This is a multiline textBox\"];]                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' UserControl property gets the user control instance for the particular input element declared by the      \'  user.]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ htmlelements [As] Hashtable = [Me].HtmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ txt [As] TEXTAREAElementImpl = [CType](IIf([TypeOf] htmlelements([\"txt\"]) [Is] TEXTAREAElementImpl, htmlelements([\"txt\"]), [Nothing]), TEXTAREAElementImpl)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Me].txt.UserControl.CustomControl.Text= [\"This is a multiline textBox\"]]                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p67} 

[]{#related-topics}

