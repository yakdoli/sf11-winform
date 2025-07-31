---
title: cellcomments.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\cellcomments.md
created_at: 2025-07-03
---






#### Cell Comments {#cell-comments style="tab-stops: 0pt"}

[] 

[Essential Grid provides support to associate individual cells with ]**Cell Comments**. **Comments** are notes used to provide context to your data in grid cells. They are used to display information about a cell or range of cells. Text in the comments can be in placed as rich text format to emphasize a comment for a cell. [You can place any kind of content---such as text, image, or any control---into the ]comment host.

**[]** 

Comment Options

**[]** 

There are two options to set a Comment for the cells:

[] 

1.   Comment Property

2.   CommentTemplateKey Property.

**[]** 

Comment Property

**[]** 

**Comment** is a string type property. This property is used to display the default **Data Template** for the comment text.

The following code illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                    |
|                                                                                                             |
| [                style.Comment = style.Text;] |
+-------------------------------------------------------------------------------------------------------------+

**[]** 

When the code runs, the following output displays.

**[]** 

**[]** 

{border="0"}

 

Figure 68: Comment Property

**[]** 

CommentTemplateKey Property

**[]** 

Grid exposes a style property named **CommentTemplateKey** used for generating Comment. This is used to define the style content to be displayed in the comment. Users can define this template in **XAML** and assign its name to the **style.CommentTemplateKey** property.

Display a customized text block in the comment host, by using the following code.

[] 

1.   Define a Template for Comments.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][DataTemplate][ x][:][Key][=\"tooltip\"\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\<][Border][    [ Background][=\"{][StaticResource][ BackBrush][}\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                       [ BorderBrush][=\"{][StaticResource][ SolidBorderBrush][}\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [           [ Name][=\"Border\"]     ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [           [ BorderThickness][=\"1\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [           [ \>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][\<][TextBlock][ Text][=\"{][Binding][ Path][=CellValue}\"][ Padding][=\"2\"][ Height][=\"30\"][ Width][=\"Auto\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\</][Border][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][DataTemplate][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

2.   Associating the above template with the Grid Cell.

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| **[]**                                                                                                                                                |
|                                                                                                                                                                                                         |
| [var style = model\[1, 2\];]                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [style.CellValue = customer.ContactName;]                                                                                                             |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [var cust = customer.Orders.Select(o =\> o.OrderDetails.Select(od =\> od.Products).Select(p =\> p.Categories)).ToList();]                             |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [var finalList = cust.Select(c =\> new]                                                                                                               |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [{]                                                                                                                                                   |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [    Count = c.Count(),]                                                                                                                              |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [    Categories = c]                                                                                                                                  |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [}).ToList();]                                                                                                                                        |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [style.ItemsSource = finalList;]                                                                                                                      |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [// Assign template.]                                                                                                                                 |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [style.CommentTemplateKey = \"][ tooltip][ \";] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays.

[] 

**[]** 

{border="0"}

Figure 69: Customized Comment

**[]** 

**[]** 

CommentAlignment

**[]** 

Users can align comments position using **CommentAlignment** property.

Alignment Options:

[] 

[·      ]Top-left

[·      ]Top-right

[·      ]Bottom-left

[·      ]Bottom-right corners.

[] 

[] 

Align the comment, by using the following code.


          {border="0"}Note: cell comment is aligned to the bottom left.


[] 

+------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                             |
|                                                                                                            |
| []                                                       |
|                                                                                                            |
| [style.CommentAlignment = CommentAlignment.Bottom-Left;] |
+------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                            |
|                                                                                                           |
| []                                                      |
|                                                                                                           |
| [style.CommentAlignment = CommentAlignment.Bottom-Left] |
+-----------------------------------------------------------------------------------------------------------+

**[]** 

When the code runs, the following output displays.

[] 

[] 

{border="0"}

 

Figure 70: Comment Alignment

[]{#p193} 

[]{#related-topics}

