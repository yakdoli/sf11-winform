---
title: subitems.md
original_path: WinForms_Docs/99_Uncategorized/subitems.md
created_at: 2025-08-05
---






##### SubItems {#subitems style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Adding SubItems

**[]** 

You can add SubItems for the nodes using the SubItems Collection available in Nodes Collection Editor.

[] 

{border="0"}

[] 

Figure 1179: Accessing the SubItems Collection Dialog Box

**[]** 

{border="0"}

**[]** 

Figure 1180: Setting the text, BorderSingle and BorderStyle Property for the SubItem

**[]** 

Properties for Customizing the SubItems

[] 

The below properties lets you customize the subitems using the SubItems Collection dialog.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------+
| TreeNodeAdvSubItem Property       | Description                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| Alignment                         | Sets the alignment of the SubItem text.                                                    |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| Background                        | Sets the background for the subitem.                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| LineAlignment                     | Sets the vertical alignment of the subitem text.                                           |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| Text                              | Sets the text for the SubItem.                                                             |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| TextColor                         | Sets the color for the SubItem text.                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| Visible                           | Sets the visibility of the subitem.                                                        |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| BaseStyle                         | Specifies the BaseStyle that it should inherit from.                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| Border3DStyle                     | Specifies the 3D style for the border.                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| BorderColor                       | Sets the border color.                                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| BorderSides                       | Specifies the sides which should have borders.                                             |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| BorderSingle                      | Specifies the 2D style for the border when BorderStyle is set to FixedSingle. Options are, |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   | [·      ]Dotted,                                              |
|                                   |                                                                                            |
|                                   | [·      ]Dashed,                                              |
|                                   |                                                                                            |
|                                   | [·      ]Solid,                                               |
|                                   |                                                                                            |
|                                   | [·      ]Inset and                                            |
|                                   |                                                                                            |
|                                   | [·      ]Outset.                                              |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| BorderStyle                       | Sets the border style, either FixedSingle or Fixed 3D                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------+


**[]** 

The below image displays subitems with similar settings in the property grid above.

**[]** 

{border="0"}

**[]** 

Figure 1181: SubItems with Italic Style; Solid, FixedSingle Border Style

**[]** 

StyleSettings for all the sub Items can be specified using **TreeNodeAdvSubItemStyleInfo** class. It is a default base style which can be accessed in the BaseStyles Collection Editor. See [[SubItem Styles]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_SubItem_Styles).

[] 

See Also

[] 

[[Column Styles]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Column_Styles)[, ]{.UGHyperlink}[[MultiColumnTreeView Appearance]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_MultiColumnTreeView_Appearance)[]{.UGHyperlink}

 

 

 

 

[]{#related-topics}

