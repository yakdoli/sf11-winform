---
title: appearanceoptions.md
original_path: WinForms_Docs/02_Concepts/appearanceoptions.md
created_at: 2025-08-05
---






##### Appearance Options {#appearance-options style="tab-stops: 0pt"}

[] 

The simplest way to check exactly which cells are affected by setting one of these properties is to use the Preview and Edit verb to display a Grid Grouping control and then set the property to view the effect.

 

When using the Preview tool at design-time, there is a cell tip that is displayed over each cell which, gives information regarding that cell. In particular, the first line of the tip will give the exact **Appearance** property that this cell is based on. In addition, it will also list the Appearance properties that the cell inherits. Here is a graphic showing some cell tip samples.

[] 

{border="0"}

[] 

*[Figure ][318][: Cell Tips Listing Appearance Inheritances Using Preview at Design-Time]*

[] 


 

{border="0"}Note:

When using Preview, make sure that you set ThemesEnabled to False, if you want to see the effect of setting the property on a header cell or a button type cell. If you do not, then the theme appearance will supersede the appearance properties you set here.

Some of the properties are not applicable unless the item they affect is used in the grid. For example, properties that affect nested tables or summaries will not change the appearance of a Grid Grouping control that does not have either of these items. In later tutorials, you will be able to test such properties.


[] 

[] 

List of Appearance Properties

[] 


  ------------------------------ ----------------------------------------------------------------------------------
  Appearance Property            Description
  AddNewRecordFieldCell          Style information for any cell in a new record row.
  AddNewRecordRowHeaderCell      Style information for header cell for any new record.
  AlternateRecordFieldCell       Style information for any cell in alternate record rows.
  AlternateRecordRowHeaderCell   Style information for any header cell in alternate record rows.
  AnyCell                        Style information for any cell in the Grid.
  AnyGroupCell                   Style information for any cell in a Group item.
  AnyHeaderCell                  Style information for any header cell.
  AnyIndentCell                  Style information for any indent cell.
  AnyNestedTableCell             Style information for any nested table cell.
  AnyPreviewCell                 Style information for any preview cell.
  AnyRecordFieldCell             Style information for any record cell.
  AnySummaryCell                 Style information for any summary cell.
  ColumnHeaderCell               Style information for any column header cell.
  ColumnHeaderWithFilterCell     Style information for any column header cell with filter.
  EmptyCell                      Style information for any empty cell.
  EmptySectionRowHeaderCell      Style information for any row header cell in an empty section.
  FilterBarCell                  Style information for any filter bar cell.
  FilterBarRowHeaderCell         Style information for any filter bar rowheader cell.
  GroupCaptionCell               Style information for any cell in a group caption.
  GroupCaptionPlusMinusCell      Style information for any plus-minus cell in a group caption.
  GroupCaptionRowHeaderCell      Style information for any row header cell in a group caption.
  GroupCaptionSummaryCell        Style information for any summary cell in a group caption.
  GroupFooterIndentCell          Style information for any indent cell in a group footer.
  GroupFooterRowHeaderCell       Style information for any header cell in a group footer.
  GroupFooterSectionCell         Style information for any section cell in a group footer.
  GroupHeaderIndentCell          Style information for any indent cell in a group.
  GroupHeaderRowHeaderCell       Style information for any cell in a group header.
  GroupHeaderSectionCell         Style information for any section cell in a group header.
  GroupIndentCell                Style information for any indent cell in a group.
  GroupIndentICell               Style information for any indent cell with no connected item.
  GroupIndentLCell               Style information for any indent cell with a bottom connected item.
  GroupIndentTCell               Style information for any indent cell with a middle connected item.
  GroupPreviewCell               Style information for any preview cell.
  GroupPreviewRowHeaderCell      Style information for any header cell in a preview row.
  NestedTableCell                Style information for any cell in a nested table.
  NestedTableIndentCell          Style information for any indent cell in a nested table.
  NestedTableIndentICell         Style information for any nested table indent cell with a bottom connected item.
  NestedTableIndentLCell         Style information for any nested table indent cell with a middle connected item.
  NestedTableIndentTCell         Style information for any nested table indent cell with no connected item.
  NestedTableRowHeaderCell       Style information for any row header cell in a nested table.
  RecordFieldCell                Style information for any field cell in a record row.
  RecordPlusMinusCell            Style information for any plus-minus cell in a record row.
  RecordPreviewCell              Style information for any preview cell in a record row.
  RecordPreviewRowHeaderCell     Style information for any header cell in a record preview row
  RecordRowHeaderCell            Style information for any header cell in a record row.
  RowHeaderCell                  Style information for any row header cell.
  SummaryEmptyCell               Style information for any empty cell in a summary row.
  SummaryFieldCell               Style information for any field cell in a summary row.
  SummaryFillRowCell             Style information for any fill cell in a summary row.
  SummaryRowHeaderCell           Style information for any header cell in a summary row.
  SummaryTitleCell               Style information for any title cell in a summary row.
  TopLeftHeaderCell              Style information for any top left header cell.
  ------------------------------ ----------------------------------------------------------------------------------


 

[]{#p448} 

 

###### 4.3.4.4.1.1 Styles At Table Level {#styles-at-table-level style="tab-stops: 0pt"}

 

This section demonstrates how to provide different appearances to the tables at different levels. Properties set through grid.**TableDescriptor.Appearance** property will be applied to the top level table(parent). To control the appearance of individual child tables, you need to first get the TableDescriptor of the desired Child Table. You can then use **ChildTableDescriptor.Appearance** property to provide the appearances to the respective child table.

 

**Example**

**[]** 

This implementation applies unique styles to the tables at different levels (Parent and Child). The grouping grid is bound to an hierarchical dataset with two tables. Below is the code to customize the appearance of these tables.

[] 

1.   Set styles to the Parent Table.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [// Column Header Cell styles.]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridGroupingControl1.Appearance.ColumnHeaderCell.CellTipText = [\"ColumnHeader\"];]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridGroupingControl1.Appearance.ColumnHeaderCell.Interior = [new] BrushInfo(GradientStyle.Vertical, [Color].FromArgb(214, 220, 232), [Color].FromArgb(106, 111, 151));]                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridGroupingControl1.Appearance.ColumnHeaderCell.TextColor = System.Drawing.[Color].White;]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [// Record Field Cell style.]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridGroupingControl1.Appearance.RecordFieldCell.Interior = [new] BrushInfo([Color].Lavender);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [// Row Header Cell styles.]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridGroupingControl1.Appearance.RowHeaderCell.Interior = [new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [SystemColors].Window, [Color].FromArgb(206, 213, 231));] |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridGroupingControl1.Appearance.RowHeaderCell.Themed = [false];]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [// Top Left Header Cell style.]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridGroupingControl1.Appearance.TopLeftHeaderCell.Interior = [new] BrushInfo(GradientStyle.PathRectangle, [SystemColors].Window, [Color].FromArgb(255, 228, 221));]                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [\' Column Header Cell styles.]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                   |
| [Me][.gridGroupingControl1.Appearance.ColumnHeaderCell.CellTipText = [\"ColumnHeader\"]]                                                                             |
|                                                                                                                                                                                                                                                                                   |
| [Me][.gridGroupingControl1.Appearance.ColumnHeaderCell.Interior = [new] BrushInfo(GradientStyle.Vertical, Color.FromArgb(214, 220, 232),Color.FromArgb(106, 111, 151))] |
|                                                                                                                                                                                                                                                                                   |
| [Me][.gridGroupingControl1.Appearance.ColumnHeaderCell.TextColor = Color.White]                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [\' Record Field Cell style.]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| [Me][.gridGroupingControl1.Appearance.RecordFieldCell.Interior = [new] BrushInfo(Color.Lavender)]                                                                       |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [\' Row Header Cell styles.]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| [Me][.gridGroupingControl1.Appearance.RowHeaderCell.Interior = [new] BrushInfo(GradientStyle.Horizontal, SystemColors.Window, Color.FromArgb(206, 213, 231))]           |
|                                                                                                                                                                                                                                                                                   |
| [Me][.gridGroupingControl1.Appearance.RowHeaderCell.Themed = [false]]                                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [\' Top Left Header Cell style.]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| [Me][.gridGroupingControl1.Appearance.TopLeftHeaderCell.Interior = [new] BrushInfo(GradientStyle.PathRectangle, SystemColors.Window, Color.FromArgb(255, 228, 221))]    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Apply styles to the Child Table.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                     |
| [GridTableDescriptor][ gtd = [this].gridGroupingControl1.GetTableDescriptor([\"Orders\"]);]                                                                                    |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [// Record Field Cell styles.]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                     |
| [gtd.Appearance.AnyRecordFieldCell.BackColor = [Color].FromArgb(223, 247, 252);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                     |
| [gtd.Appearance.AlternateRecordFieldCell.BackColor = [Color].FromArgb(255, 229, 201);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [// Column Header Cell styles.]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [gtd.Appearance.ColumnHeaderCell.Interior = [new] BrushInfo(GradientStyle.Vertical, [Color].FromArgb(203, 201, 202), [Color].FromArgb(253, 247, 215));]                                                    |
|                                                                                                                                                                                                                                                                                                                     |
| [gtd.Appearance.ColumnHeaderCell.TextColor = [Color].Black;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [// Group Caption Cell styles.]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [gtd.Appearance.GroupCaptionCell.Interior = [new] BrushInfo([Color].FromArgb(255, 238, 220));]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [gtd.Appearance.GroupCaptionCell.Borders.Bottom = [new] [GridBorder]([GridBorderStyle].Solid, [Color].FromArgb(242, 158, 32), [GridBorderWeight].Medium);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [Dim][ gtd [As] GridTableDescriptor = [Me].gridGroupingControl1.GetTableDescriptor([\"Orders\"])] |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [\' Record Field Cell styles.]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [gtd.Appearance.AnyRecordFieldCell.BackColor = Color.FromArgb(223, 247, 252)]                                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [gtd.Appearance.AlternateRecordFieldCell.BackColor = Color.FromArgb(255, 229, 201)]                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [\' Column Header Cell styles.]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [gtd.Appearance.ColumnHeaderCell.Interior = [New] BrushInfo(GradientStyle.Vertical, Color.FromArgb(203, 201, 202), Color.FromArgb(253, 247, 215))]                                              |
|                                                                                                                                                                                                                                                          |
| [gtd.Appearance.ColumnHeaderCell.TextColor = Color.Black]                                                                                                                                                            |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [\' Group Caption Cell styles.]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [gtd.Appearance.GroupCaptionCell.Interior = [New] BrushInfo(Color.FromArgb(255, 238, 220))]                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [gtd.Appearance.GroupCaptionCell.Borders.Bottom = [New] GridBorder(GridBorderStyle.Solid, Color.FromArgb(242, 158, 32), GridBorderWeight.Medium)]                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Here is a sample screenshot.

[] 

{border="0"}

[] 

*[Figure ][319][: Customized Appearance of Tables at Different Levels]*

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Appearance\\Table Style Demo


 

[]{#p449} 

 

###### 4.3.4.4.1.2 Styles At Group Level {#styles-at-group-level style="tab-stops: 0pt"}

[] 

This section lets you customize the appearances of different group elements. You can provide unique appearances to every element of a group such as GroupCaptionCell and Group Header / Footer Cells by setting the following properties under Appearance section: **GroupCaptionCell**, **GroupCaptionPlusMinusCell, GroupHeaderSectionCell, GroupIndentCell, GroupFooterSectionCell, GroupPreviewCell** and the like.

 

**Example**

**[]** 

Below is the code to apply different styles to various group members.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.Appearance.AnyGroupCell.Interior = [new] BrushInfo([Color].White);]                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.Appearance.AnyGroupCell.Themed = [false];]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.Appearance.GroupCaptionCell.Borders.Bottom = GridBorder([GridBorderStyle].Solid, [Color].FromArgb(157, 179, 200));]                                               |
|                                                                                                                                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.Appearance.GroupCaptionRowHeaderCell.Interior = [new] BrushInfo(GradientStyle.BackwardDiagonal, [SystemColors].Window, [Color].DarkOrange);] |
|                                                                                                                                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.Appearance.GroupFooterSectionCell.Interior = [new] BrushInfo(GradientStyle.Horizontal, [Color].White, [Color].FromArgb(192, 255, 192));]     |
|                                                                                                                                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.Appearance.GroupHeaderRowHeaderCell.Interior = [new] BrushInfo(GradientStyle.Vertical, [SystemColors].Window, [Color].LightPink);]           |
|                                                                                                                                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.Appearance.GroupHeaderSectionCell.Interior = [new] BrushInfo(GradientStyle.Horizontal, [Color].White, [Color].FromArgb(255, 199, 190);]      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [gridGroupingControl1.Appearance.AnyGroupCell.Interior = [New] BrushInfo(Color.White)]                                                                        |
|                                                                                                                                                                                                                        |
| [gridGroupingControl1.Appearance.AnyGroupCell.Themed = [False]]                                                                                               |
|                                                                                                                                                                                                                        |
| [gridGroupingControl1.Appearance.GroupCaptionCell.Borders.Bottom = GridBorder(GridBorderStyle.Solid, Color.FromArgb(157, 179, 200))]                                               |
|                                                                                                                                                                                                                        |
| [gridGroupingControl1.Appearance.GroupCaptionRowHeaderCell.Interior = [New] BrushInfo(GradientStyle.BackwardDiagonal, SystemColors.Window, Color.DarkOrange)] |
|                                                                                                                                                                                                                        |
| [gridGroupingControl1.Appearance.GroupFooterSectionCell.Interior = [New] BrushInfo(GradientStyle.Horizontal, Color.White, Color.FromArgb(192, 255, 192))]     |
|                                                                                                                                                                                                                        |
| [gridGroupingControl1.Appearance.GroupHeaderRowHeaderCell.Interior = [New] BrushInfo(GradientStyle.Vertical, SystemColors.Window, Color.LightPink)]           |
|                                                                                                                                                                                                                        |
| [gridGroupingControl1.Appearance.GroupHeaderSectionCell.Interior = [New] BrushInfo(GradientStyle.Horizontal, Color.White, Color.FromArgb(255, 199, 190)]      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Here is a sample screen shot.

[] 

[{border="0"}][]

[] 

*[Figure ][320][: Customized Appearance of Groups at Different Levels]*

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Appearance\\Group Style Demo


 

[]{#p450} 

 

###### 4.3.4.4.1.3 ColumnStyles {#columnstyles style="tab-stops: 0pt"}

[] 

Grid Grouping control allows you to do **Column-Based formatting**. With this feature, you can provide an unique appearance to different grid columns. Grid columns can be customized by setting the **GridColumnDescriptor.Appearance** property.

 

ColumnFormatting can be done at design time. Once the data source is set, select TableDescriptor.Columns property in the property window of the grid grouping control. This will open the GridColumnDescriptor collection editor that is populated with the columns in the datasource. You can modify the appearance of the desired column by setting the Appearance property of that column in this editor. The following picture shows this process.

[] 

{border="0"}

[] 

*[Figure ][321][: GridColumnDescriptor Collection Editor]*

 

**Programmatically**

**[]** 

You can control the appearance of the columns through code also. Below is the code that applies different styles to the various columns in the grid.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [GridColumnDescriptor][ desc1 = [new] [GridColumnDescriptor]();] |
|                                                                                                                                                                                                       |
| [desc1.MappingName = [\"ProductName\"];]                                                                                                  |
|                                                                                                                                                                                                       |
| [desc1.Appearance.RecordFieldCell.Interior = [new] BrushInfo([Color].FromArgb(237, 240, 246));]                      |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [GridColumnDescriptor][ desc2 = [new] [GridColumnDescriptor]();] |
|                                                                                                                                                                                                       |
| [desc2.MappingName = [\"SupplierID\"];]                                                                                                   |
|                                                                                                                                                                                                       |
| [desc2.Appearance.RecordFieldCell.Interior = [new] BrushInfo([Color].FromArgb(218, 229, 245));]                      |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [GridColumnDescriptor][ desc3 = [new] [GridColumnDescriptor]();] |
|                                                                                                                                                                                                       |
| [desc3.MappingName = [\"CategoryID\"];]                                                                                                   |
|                                                                                                                                                                                                       |
| [desc3.Appearance.RecordFieldCell.Interior = [new] BrushInfo([Color].FromArgb(102, 110, 152));]                      |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [GridColumnDescriptor][ desc4 = [new] [GridColumnDescriptor]();] |
|                                                                                                                                                                                                       |
| [desc4.MappingName = [\"QuantityPerUnit\"];]                                                                                              |
|                                                                                                                                                                                                       |
| [desc4.Appearance.RecordFieldCell.Interior = [new] BrushInfo([Color].FromArgb(252, 172, 38));]                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                  |
|                                                                                                                                                                                                     |
| []                                                                                                                                                 |
|                                                                                                                                                                                                     |
| [Dim][ desc1 [As] GridColumnDescriptor = [New] GridColumnDescriptor] |
|                                                                                                                                                                                                     |
| [desc1.MappingName = [\"ProductName\"]]                                                                                                 |
|                                                                                                                                                                                                     |
| [desc1.Appearance.RecordFieldCell.Interior = [New] BrushInfo(Color.FromArgb(237, 240, 246))]                                               |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [Dim][ desc1 [As] GridColumnDescriptor = [New] GridColumnDescriptor] |
|                                                                                                                                                                                                     |
| [desc1.MappingName = [\"ProductName\"]]                                                                                                 |
|                                                                                                                                                                                                     |
| [desc1.Appearance.RecordFieldCell.Interior = [New] BrushInfo(Color.FromArgb(218, 229, 245))]                                               |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [Dim][ desc1 [As] GridColumnDescriptor = [New] GridColumnDescriptor] |
|                                                                                                                                                                                                     |
| [desc1.MappingName = [\"SupplierID\"]]                                                                                                  |
|                                                                                                                                                                                                     |
| [desc1.Appearance.RecordFieldCell.Interior = [New] BrushInfo(Color.FromArgb(102, 110, 152))]                                               |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [Dim][ desc1 [As] GridColumnDescriptor = [New] GridColumnDescriptor] |
|                                                                                                                                                                                                     |
| [desc1.MappingName = [\"QuantityPerUnit\"]]                                                                                             |
|                                                                                                                                                                                                     |
| [desc1.Appearance.RecordFieldCell.Interior = [New] BrushInfo(Color.FromArgb(252, 172, 38))]                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Given below is a sample screen shot.

[] 

{border="0"}

***[]*** 

*[Figure ][322][: Customized Appearance of Grid Columns]*


 

\\{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Appearance\\Column Style Demo


 

[]{#p451} 

 

[]{#related-topics}

