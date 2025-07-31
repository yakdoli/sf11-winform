---
title: styleelement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\styleelement.md
created_at: 2025-07-03
---








  









### STYLE Element {#style-element style="tab-stops: 0pt"}

[] 

The **STYLE** element is used to implement custom style in a document. It occurs inside the head section. An external style sheet is linked by using the **\<link\>** tag in a HTML document. The **StyleElementImpl** class is invoked for defining the properties and methods of the style element.

[] 

Properties

[] 

[·      ]**IsVisible**: Gets / sets a value indicating whether the link is shown / hidden

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [// Gets a value indicating whether the link is visible or not.]                                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| [Hashtable][ htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                           |
|                                                                                                                                                                                                                                                                               |
| [StyleElementImpl][ link = htmlelements\[[\"style\"]\] [as] [StyleElementImpl];] |
|                                                                                                                                                                                                                                                                               |
| [this][.label1.Text = [\"\\nLink(IsVisible):\"] + link.IsVisible.ToString();]                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Gets a value indicating whether the link is visible or not.]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ htmlelements [As] Hashtable = [Me].HtmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ link [As] StyleElementImpl = [CType](IIf([TypeOf] htmlelements([\"style\"]) [Is] StyleElementImpl, htmlelements([\"style\"]), [Nothing]), StyleElementImpl)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Me].label1.Text = Constants.vbLf & [\"Link(IsVisible):\"] &  link.IsVisible.ToString()]                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Methods

[] 

[·      ]**GetCssStream**: Returns a stream of inner CSS data of the style element

[]{#p64} 

[]{#related-topics}

