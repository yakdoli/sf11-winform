---
title: gridformatcelldialog.md
original_path: WinForms_Docs/04_Controls/Grid/gridformatcelldialog.md
created_at: 2025-08-05
---






##### GridFormatCellDialog {#gridformatcelldialog style="tab-stops: 0pt"}

[] 

GridFormatCellDialog simulates the FormatCells dialog feature of MS Excel. It provides numerous formatting options such as Font, Alignment, Background and Number, which aid in formatting the grid cells dynamically. It is now available as an add-on feature for Essential Grid control.

 

The GridFormatCellDialog class accepts an instance of the Grid control to be formatted, and exposes the above mentioned formatting options to operate on the grid cells that are selected. Below image illustrates such a sample dialog.

[] 

{border="0"}

[] 

*[Figure ][144][: Format Cell Dialog Box]*

[] 

Setting up GridFormatCellDialog

[] 

This GridFormatCellDialog can be enabled by instantiating the GridFormatCellDialog class, and invoking its **ShowDialog** method.

[] 


{border="0"}Note: You must select the cells to be formatted before activating this dialog.


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [GridFormatCellDialog][ formatDialog = [new] [GridFormatCellDialog]([this].gridControl1);] |
|                                                                                                                                                                                                                                                      |
| [formatDialog.ShowDialog();]                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [Dim][ formatDialog [As] GridFormatCellDialog = [New] GridFormatCellDialog([Me].gridControl1)] |
|                                                                                                                                                                                                                                                    |
| [formatDialog.ShowDialog()]                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Formatting Options

[] 

**Font Tab**

[] 

This provides options to set the font, font style, font size, font effects and font color for the desired grid cells.

[] 

{border="0"}

***[]*** 

*[Figure ][145][: Font customization options in the Format Cell Dialog Box]*

[] 

[] 

**Number Tab**

 

This allows you to specify a text format for the grid cells. The possible options are Number, Currency, Percentage, Date, Time, Scientific and Text.

[] 

{border="0"}

[] 

*[Figure ][146][: Text Format options in the Format Cell Dialog Box]****[]***

[] 

[] 

**Background Tab**

 

This allows you to set the background color for the grid cells. You can set gradient shades and pattern styles as well.

[] 

{border="0"}

*[]* 

*[Figure ][147][: Background customization options in the Format Cell Dialog Box]*

[] 

[] 

**Alignment Tab**

 

This provides various cell alignment options such as Horizontal Alignment, Vertical Alignment, Merge Cells, Wrap Text, and so on.

[] 

{border="0"}

***[]*** 

*[Figure ][148][: Alignment options in the Format Cell Dialog Box]*

 

[]{#p316} 

 

[]{#related-topics}

