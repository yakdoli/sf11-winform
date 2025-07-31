---
title: basestyles.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\basestyles.md
created_at: 2025-07-03
---






##### BaseStyles {#basestyles style="tab-stops: 0pt"}

[] 

Grid control supports another parent-type style, **BaseStyles**, which is used to customize a cell\'s appearance. BaseStyles are **GridStyleInfo** objects which can be associated with an arbitrary collection of cells. In a Word Processing software, there is the common task of defining a particular style (such as style Header1 representing a bold, 20-point Helvetica font), and then using it repeatedly in your document whenever you need a \'Header1\' type. BaseStyles play the same role within Grid control. You can define a BaseStyle named Header1 as having certain properties, and then you can place these properties onto any cell just by applying this BaseStyle Header1 to the cell. More importantly, if you want to change Header1 (for example, changing its **BackColor** property from white to red), you can make the change one time by just changing the Header1 BaseStyle, and not having to relabel every other cell assigned to this BaseStyle.

[] 

Since BaseStyles are considered as parent styles, where do they fit within the precedence hierarchy that we have discussed above? BaseStyles are applied between the tablestyle and the standardstyle. Thus, they are the \'weakest\' style other than the fully populated standardstyle. BaseStyles are stored in the **GridControl.BaseStylesMap** class. In addition to the standardstyle, other BaseStyles used by all Essential Grids include Row Header, Header and Column Header. You can define and apply your own BaseStyles as well.

[] 

To work with BaseStyles from within the Visual Studio designer, you need to use the **Edit base styles** verb that appears at the bottom of the Grid control\'s property grid.

[] 

{border="0"}

**[]** 

*[Figure ][98][: PropertyGrid with Edit BaseStyles Option]*

[] 

When you click the Edit base styles verb, the **GridBaseStyle Collection Editor** dialog box is displayed. You can use the GridBaseStyle Collection Editor to edit the existing BaseStyles or add new ones.

[] 

{border="0"}

 

*[Figure ][99][: GridBaseStyle Collection Editor]*

[] 

The following code example illustrates how to create a BaseStyle. When you define a BaseStyle you can apply it to any cell (or row or column) by just setting the **GridStyleInfo.BaseStyle** for that cell to the name used to define the BaseStyle.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                           |
| [// Add a new base style.]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                           |
| [GridBaseStyle][ gridBaseStyle1 = [new] [GridBaseStyle]([\"BackColorTest\"], [false]);] |
|                                                                                                                                                                                                                                                                                                           |
| [gridBaseStyle1.StyleInfo.BackColor = [Color].SkyBlue;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                           |
| [gridBaseStyle1.StyleInfo.TextColor = [Color].RosyBrown;]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                           |
| [gridControl1.BaseStylesMap.AddRange([new] [GridBaseStyle]\[\]{gridBaseStyle1});]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| [\...]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| [// Apply this base style to a couple of cells.]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| [gridControl1\[1,2\].BaseStyle = [\"BackColorTest\"];]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| [gridControl1\[4,2\].BaseStyle = [\"BackColorTest\"];]                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                           |
| [ [\' Add a new base style.]]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                           |
| [Dim][ gridBaseStyle1 [As] GridBaseStyle = [New] GridBaseStyle([\"BackColorTest\"], [False])] |
|                                                                                                                                                                                                                                                                                                           |
| [gridBaseStyle1.StyleInfo.BackColor = Color.SkyBlue]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [gridBaseStyle1.StyleInfo.TextColor = Color.RosyBrown]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                           |
| [gridControl1.BaseStylesMap.AddRange([New] GridBaseStyle() {gridBaseStyle1})]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| [\...]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| [\' Apply this base style to a couple of cells.]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| [gridControl1(1, 2).BaseStyle = [\"BackColorTest\"]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| [gridControl1(4, 2).BaseStyle = [\"BackColorTest\"]]                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p75} 

 

[]{#related-topics}

