---
title: brbreakelement.md
original_path: WinForms_Docs/99_Uncategorized/brbreakelement.md
created_at: 2025-08-05
---








  









### BR - Break Element {#br---break-element style="tab-stops: 0pt"}

[] 

The **BR** element is used for inserting a line break after a particular line. This is implemented using the **\<br\>** tag in the HTML document. The **BRElementImpl** class contains the properties and methods for this element\'s behavior.

[] 

Properties

[] 

[·      ]**IsVisible**: Gets / sets a boolean value to indicate whether the control is shown / hidden.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [// Get the Boolean value to indicate whether the control is visible or not.]                                                                                                                    |
|                                                                                                                                                                                                                                                                    |
| [Hashtable][ htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                |
|                                                                                                                                                                                                                                                                    |
| [BRElementImpl][ br = htmlelements\[[\"br\"]\] [as] [BRElementImpl];] |
|                                                                                                                                                                                                                                                                    |
| [this][.label1.Text = [\"\\nBR(IsVisible):\"] + [this].br.IsVisible.ToString(); ]                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Get the Boolean value to indicate whether the control is visible or not.]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ htmlelements [As] Hashtable = [Me].HtmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ br [As] BRElementImpl = [CType](IIf([TypeOf] htmlelements([\"br\"]) [Is] BRElementImpl, htmlelements([\"br\"]), [Nothing]), BRElementImpl)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.label1.Text = Constants.vbLf & [\"BR(IsVisible):\"] & [Me].br.IsVisible.ToString()]                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p41} 

[]{#related-topics}

