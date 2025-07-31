---
title: inputelement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\inputelement.md
created_at: 2025-07-03
---








  









### INPUT Element {#input-element style="tab-stops: 0pt"}

[] 

The **INPUT** element is used for getting input from the user. It can be a text box, a button element or a check box which is determined by the type attribute of the **\<input\>** tag in the HTML document. The **INPUTElementImpl** class is used in determining the methods and properties for this element.

[] 

Properties

[] 

[·      ]**UserControl**: Gets / sets the user control instance for the particular input element declared by the user

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [// Sets the user control instance for the particular input element declared by the user.]                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [Hashtable][ htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                        |
|                                                                                                                                                                                                                                                                            |
| [INPUTElementImpl][ txt = htmlelements\[[\"txt\"]\] [as] [INPUTElementImpl];] |
|                                                                                                                                                                                                                                                                            |
| [this][.txt.UserControl.CustomControl.Text = [\"This is a textBox\"];]                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\'  User control property sets the user control instance for the particular input element declared by the user.]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ htmlelements [As] Hashtable = [Me].HtmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ txt [As] INPUTElementImpl = [CType](IIf([TypeOf] htmlelements([\"txt\"]) [Is] INPUTElementImpl, htmlelements([\"txt\"]), [Nothing]), INPUTElementImpl)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Me][.txt.UserControl.CustomControl.Text = [\"This is a textBox\"]]                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Methods

**[]** 

[·      ]**InfillFromXMLElement**: Detects the type of control from the **type** attribute and creates that control

[]{#p54} 

[]{#related-topics}

