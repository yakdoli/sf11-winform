---
title: linkelement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\linkelement.md
created_at: 2025-07-03
---








  









### LINK Element {#link-element style="tab-stops: 0pt"}

[] 

The **LINK** element is used to define links to other documents, style sheets, and so on. The **LinkElementImpl** is used to determine the methods and properties for the link element.

[] 

Properties

**[]** 

[·      ]**IsVisible**: Gets / sets a value indicating whether the link is shown / hidden

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [// Get the value indicating whether the link is visible or not.]                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [Hashtable][ htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                        |
|                                                                                                                                                                                                                                                                            |
| [LinkElementImpl][ link = htmlelements\[[\"link\"]\] [as] [LinkElementImpl];] |
|                                                                                                                                                                                                                                                                            |
| [this][.label1.Text = [\"\\nLink(IsVisible):\"] + [this].link.IsVisible.ToString();]                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\' Get the value indicating whether the link is visible or not.]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [As] Hashtable = [Me].htmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ link [As] LinkElementImpl = [CType](IIf([TypeOf] HtmlElement([\"link\"]) [Is] LinkElementImpl, htmlelements([\"link\"]), [Nothing]), LinkElementImpl)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.label1.Text = Constants.vbLf & [\"Link(IsVisible):\"] & [Me].link.IsVisible.ToString()]                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Methods

[] 

[·      ]**GetCssStream**: Returns a stream CSS data of the link element

[]{#p56} 

[]{#related-topics}

