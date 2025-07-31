---
title: selectelement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\selectelement.md
created_at: 2025-07-03
---








  









### SELECT Element {#select-element style="tab-stops: 0pt"}

[] 

The **SELECT** element is used to define a drop-down list. The user can specify the number of items to include in the drop-down list. The **SELECTElementImpl[ ]**class defines the properties and methods for this element.

[] 

Properties

[] 

[·      ]**UserControl**: Gets / sets the user control instance to the particular element

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                 |
| [// UserControl property gets or sets the user control instance to the particular element.]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                 |
| [Hashtable][ htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                                                                             |
|                                                                                                                                                                                                                                                                                                                                 |
| [this][.select = htmlelements\[[\"select\"]\] [as] [SELECTElementImpl];]                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| [this][.label1.Text = [\"\\nSelect(UserControl):\"] + [this].UserControl.DefaultSize.ToString(); ][                     ] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\'  UserControl property gets or sets the user control instance to the particular element.]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Private][ htmlelements [As] Hashtable = [Me].HtmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.Select = [CType](IIf([TypeOf] htmlelements([\"select\"]) [Is] SELECTElementImpl, htmlelements([\"select\"]), [Nothing]), SELECTElementImpl)] |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.label1.Text = Constants.vbLf & [\"Select(UserControl):\"] & [Me].Select.UserControl.DefaultSize.ToString()]                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Methods

[] 

[·      ]**InfillFromXMLElement**: Detects the type of control and creates the particular control

[]{#p61} 

[]{#related-topics}

