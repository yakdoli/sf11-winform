---
title: basestyles1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\basestyles1.md
created_at: 2025-07-03
---






##### BaseStyles {#basestyles style="tab-stops: 0pt"}

 

In addition to the parent styles discussed in the previous topics, Essential Grid supports one other parent-type style which, can contribute to a cell\'s appearance, they are BaseStyles of GridStyleInfo objects which, can be associated with an arbitrary collection of cells.

 

BaseStyles provide the way to create StyleTemplates that can be applied to the cells. It allows you to apply styles with ease and in faster manner. For example, in a word processing software, there is the common task of defining a particular style (such as style Header1 representing a bold, 20-point Helvetica font) and then using it repeatedly in your document whenever you need a \'Header1\' type.

 

BaseStyles play the same role within Essential Grid. You can define a BaseStyle named Header1 as having certain properties and then you can place these properties onto any cell just by applying this BaseStyle Header1 to the cell. More importantly is that if later on you want to change what Header1 means (for example, changing its BackColor property from white to red), you can make the change one time by just changing the Header1 BaseStyle and not having to relabel every other cell assigned to this BaseStyle.

 

BaseStyles are stored in the GridGroupingControl.TableModel.BaseStylesMap class. In addition to the standardstyle, other BaseStyles used by all Essential Grids include Row Header, Header and Column Header. You can define and apply your own BaseStyles as well.

 

Users can add base styles to the engine and inherit the style settings through GridStyleInfo.BaseStyle property. You can create any number of style templates through BaseStyles.

 

Applying BaseStyles

[] 

1.   To add style templates at design time, you need to access the BaseStyles property in the property editor. This will open the GridTableStyle Collection Editor that lists the StyleInfo properties that can be associated to a grid cell. Here is a property editor that shows the creation of two style templates named BaseStyle1 and BaseStyle2.

 

{border="0"}

 

*[Figure ][327][: GridTableBaseStyle Collection Editor]*

 

2.   Your next step is to set the base styles created above, to the grid cells as required. Suppose if you want to set BaseStyle1 for alternate record field cells and BaseStyle2 for the remaining cells, then this can be specified by setting Appearance.AlternateRecordFieldCell.BaseStyle property to BaseStyle1 and Appearance.AnyCell.BaseStyle property to BaseStyle2 as shown in the image below.

 

 

{border="0"}

 

*[Figure ][328][: Setting the Base Styles to the respective Grid Cells]*

 

3.   Here is a sample screenshot.

 

 

{border="0"}

*[Figure ][329][: Base Styles applied to the Grid Grouping Control]*

 

Programmatically

[] 

Base styles can also be set through code. The following code example illustrates how to create and apply the above styles to the grouping grid.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [GridTableBaseStyle][ style1 = [new] [GridTableBaseStyle]([\"BaseStyle 1\"]);] |
|                                                                                                                                                                                                                                             |
| [style1.Name = [\"BaseStyle 1\"];]                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [style1.StyleInfo.Font.Facename = [\"Verdana\"];]                                                                                                                               |
|                                                                                                                                                                                                                                             |
| [style1.StyleInfo.Interior = [new] BrushInfo([Color].FromArgb(255, 128, 0));]                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [GridTableBaseStyle][ style2 = [new] [GridTableBaseStyle]([\"BaseStyle 2\"]);] |
|                                                                                                                                                                                                                                             |
| [style2.Name = [\"BaseStyle 2\"];]                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [style2.StyleInfo.Font.Facename = [\"Arial\"];]                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [style2.StyleInfo.Interior = [new] BrushInfo([Color].FromArgb(192, 192, 255));]                                                                            |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [gridGroupingControl1.BaseStyles.AddRange([new] [GridTableBaseStyle]\[\] { style1, style2 });]                                                             |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [gridGroupingControl1.Appearance.AlternateRecordFieldCell.BaseStyle = [\"BaseStyle 1\"];]                                                                                       |
|                                                                                                                                                                                                                                             |
| [gridGroupingControl1.Appearance.AnyCell.BaseStyle = [\"BaseStyle 2\"];]                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [Dim][ style1 [As] GridTableBaseStyle = [New] GridTableBaseStyle([\"BaseStyle 1\"])] |
|                                                                                                                                                                                                                                             |
| [style1.Name = [\"BaseStyle 1\"]]                                                                                                                                               |
|                                                                                                                                                                                                                                             |
| [style1.StyleInfo.Font.Facename = [\"Verdana\"]]                                                                                                                                |
|                                                                                                                                                                                                                                             |
| [style1.StyleInfo.Interior = [New] BrushInfo(Color.FromArgb(255, 128, 0))]                                                                                                         |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [Dim][ style2 [As] GridTableBaseStyle = [New] GridTableBaseStyle([\"BaseStyle 2\"])] |
|                                                                                                                                                                                                                                             |
| [style2.Name = [\"BaseStyle 2\"]]                                                                                                                                               |
|                                                                                                                                                                                                                                             |
| [style2.StyleInfo.Font.Facename = [\"Arial\"]]                                                                                                                                  |
|                                                                                                                                                                                                                                             |
| [style2.StyleInfo.Interior = [New] BrushInfo(Color.FromArgb(192, 192, 255))]                                                                                                       |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [gridGroupingControl1.BaseStyles.AddRange([New] GridTableBaseStyle() { style1, style2 });]                                                                                         |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [gridGroupingControl1.Appearance.AlternateRecordFieldCell.BaseStyle = [\"BaseStyle 1\"];]                                                                                       |
|                                                                                                                                                                                                                                             |
| [gridGroupingControl1.Appearance.AnyCell.BaseStyle = [\"BaseStyle 2\"];]                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p454} 

 

[]{#related-topics}

