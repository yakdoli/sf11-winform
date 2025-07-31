---
title: aanchorelement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\aanchorelement.md
created_at: 2025-07-03
---








  









### A - Anchor Element {#a---anchor-element style="tab-stops: 0pt"}

[] 

The **A** element is used in creating links to another document or in creating bookmarks within the same document. This element is defined by the **\<a\>** tag in the HTML code. The **AElementImpl** class contains the properties and methods related to this element. Some of the  important properties and methods are listed below:

[] 

Properties

[] 

[·      ]**IsVisited**: Gets a bool value (either true / false) indicating whether the link is visited or not. This may be used in changing the color of the links visited.

[·      ]**HoverFormat**: Gets the format of the **A** element when the user hovers the mouse pointer over the link.

[·      ]**VisitedFormat**: Gets the format of the **A** element visited recently.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [// IsVisited property gets the Boolean value indicating whether the link is visited or not ]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [// VisitedFormat property get the format of the A element visited recently. ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [Hashtable][ htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [AElementImpl][ a = htmlelements\[[\"a\"]\] [as] [AElementImpl];]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.label1.Text = [\"\\nA(IsVisited and VisitedFormat):\"] + [this].a.IsVisited.ToString() + [\",\"] + [this].a.VisitedFormat.BackgroundColor.Name.ToString(); ] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' IsVisited property gets the Boolean value indicating whether the link is visited or not ]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' VisitedFormat property get the format of the A element visited recently. ]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ htmlelements [As] Hashtable = [Me].HtmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ a [As] AElementImpl = [CType](IIf([TypeOf] htmlelements([\"a\"]) [Is] AElementImpl, htmlelements([\"a\"]), [Nothing]), AElementImpl)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Me].label1.Text=Constants.vbLf & [\"A(IsVisited and VisitedFormat):\"] & [Me].a.IsVisited.ToString()+[\",\"]+[Me].a.VisitedFormat.BackgroundColor.Name.ToString()]             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Methods

[] 

[·      ]**ResetVisited**: Excludes the element from the list containing the visited links.

[]{#p38} 

[]{#related-topics}

