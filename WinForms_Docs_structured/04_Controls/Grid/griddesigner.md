---
title: griddesigner.md
original_path: WinForms_Docs/04_Controls/Grid/griddesigner.md
created_at: 2025-08-05
---






#### Grid Designer {#grid-designer style="tab-stops: 0pt"}

[] 

The Grid Grouping control has strong designer support. You can control all aspects of the grid\'s appearance through the designer. Additional commands (verbs) will let you save layouts and restore them. You can also use a preview feature that will let you load data into your control and then further set the Grid Grouping control properties that can be persisted as design-time properties.

 

Clicking the Preview and Edit verb will allow you to view the Grid Grouping control, populated with data along with a companion property grid as seen in the picture below. It also displays help description for the properties that are being selected. You can use the property grid to change the Grid Grouping control\'s properties and see the effect immediately upon the populated control. When you close the preview, you will have the option of saving any changed properties to the property grid in the designer. We will use this Preview and Edit support to see the effects of setting the various TableOption properties.

[] 

{border="0"}

[] 

*[Figure ][386][: Preview and Edit Support]*

[] 

Grid Designer presents populated Grid Grouping control along with a property grid listing out the related properties. It also includes an integrated help feature to display a brief description on the property selected. You will be able to set any kind of properties using the designer so that you could see the results immediately. Here is a brief discussion on how to work with grid elements through the designer.

[] 

**Grouping**

[] 

Designer provides full drag/drop capability so that you could be able to group the records by dragging a column header and dropping it into the GroupDropArea, provided the GroupDropArea is enabled by setting **ShowGroupDropArea** to true. Likewise you can group the data against any number of columns across the tables when multiple nested tables are used.

**[]** 

{border="0"}

[] 

*[Figure ][387][: Dragging a column header to group grid by that Column]*

[] 

{border="0"}

[] 

*[Figure ][388][: Grouped Grid]*

**[]** 

You can also use **TableDescriptor.GroupedColumns** property to add groups where you need to specify the column names based on which the table has to be grouped.

[] 

{border="0"}

***[]*** 

*[Figure ][389][: Grouping Columns by adding Groups]*

**[]** 

Sorting

 

Sorting can be done on the table data by simply clicking the desired column header by which the values need to be sorted. Once sorting is done, the grouping grid displays a ListSortIcon in the respective column header to indicate the Sort Direction. You could also make use of the TableDescriptor.SortedColumns property to perform sorting on table data wherein you need to provide the column to be sorted and a sort order.

**[]** 

{border="0"}

[] 

*[Figure ][390][: Sorted Grid highlighting the Sorted Column]****[s]***

[] 

{border="0"}

[] 

*[Figure ][391][: Sorted Grid showing the SortedColumns Editor]*

 

Summaries

[] 

Summaries can be added in the designer itself by accessing the property, TableDescriptor.SummaryRows property. You can add as many summary rows as you need, each with a desired number of summary columns where you can specify the type of summary, summary format, the column based on whose values the summary has to be calculated and the like for each of the summary columns.

**[]** 

{border="0"}

[] 

*[Figure ][392][: Adding Summary Rows]****[]***

[] 

{border="0"}

[] 

*[Figure ][393][: Grouping Grid displaying Summary]*

[] 

Record Filters

 

By using the TableDescriptor.RecordFilters property, you can add row filters for your grid table. Once you have specified the filter criteria and the column name whose values have to be checked against the given criteria, the grouping grid will display only the subset of records that satisfy the given criteria.

[] 

{border="0"}

[] 

*[Figure ][394][: Adding row filters through RecordFilters Property]****[]***

[] 

{border="0"}

[] 

*[Figure ][395][: Filtered Grid]*

**[]** 

Grid Grouping control provides an **AutoFilterRow** which can be enabled by setting the **ShowFilterBar** property to true. Once it is done, you must enable **AllowFilter** property for the desired columns to enable filtering on those columns.

[] 

{border="0"}

[] 

*[Figure ][396][: Grid with Auto-Filter Row Enabled]*

[] 

{border="0"}

[] 

*[Figure ][397][: Setting AllowFilter property for \'CompanyName\' Column]*

[] 

{border="0"}

[] 

*[Figure ][398][: FilterBar drop down showing filtering options for the column \'CompanyName\']*

[] 

Expression Fields

 

When there is a need to display calculated values based on the values on other fields in the same record, ExpressionFields would be the right choice to use. ExpressionFields can be created by using the TableDescriptor.ExpressionFields property. This will open an editor wherein you can add any number of expression fields each with its own expression used to calculate the results.

[] 

{border="0"}

[] 

*[Figure ][399][:  Adding an Expression Field]*

*[]* 

{border="0"}

[] 

*[Figure ][400][: Grouping Grid showing the ExpressionField \'Winning%\']*

[] 

Relations

 

It is possible to specify the relation to be used across the tables in case multiple tables are used. It can done by accessing the TableDescriptor.Relations property wherein you can specify the relation type, name of the child table, relation keys consisting of the keys in parent and child tables and other information necessary to setup the relation.

**[]** 

{border="0"}

[] 

*[Figure ][401][: Hierarchical Grid with RelationKind \'RelatedMasterDetails\']*

[] 

Appearance

 

The appearance of every grid element can be customized by accessing the Appearance property. It allows you to set GridStyleInfo properties like cell type, value, back color, font, etc. for grid cells. It holds a sub tree of different grid elements each with its own set of formatting properties. For instance, when you want to set appearance for alternate record field cell, you can make use of Appearance.AlternateRecordFieldCell property; if you want to customize summary cells, you will have to use Appearance.SummaryFieldCell or related property.

**[]** 

{border="0"}

[] 

*[Figure ][402][: Grid Designer showing the appearance settings for AlternateRecordFieldCell]*

 

Skins

 

You can change the appearance and behavior of every grid element to provide grid with a rich look and feel by setting skins. Grouping Grid currently offers five such skins: Office2007Blue, Office2007Silver, Office2007Black, Office2003 and SystemTheme(Default XP theme). To set a skin, the GridVisualStyles property which is under TableOptions section is used. It lists the possible skin options in a drop down, which will make the entire grid redrawn with the chosen style.

[] 

{border="0"}

[] 

*[Figure ][403][: Grid Designer displaying the possible skins in a Drop Down]*

[] 

See Also

**[]** 

[Grouping]{.UGHyperlink}[,][ Sorting]{.UGHyperlink}[,][ ][Summaries]{.UGHyperlink}[,][ ][Record Filters]{.UGHyperlink}[,][ ][Expression Fields]{.UGHyperlink}[,][ ][Relations]{.UGHyperlink}[,][ ][Appearance]{.UGHyperlink}[, ][Grid Skins]{.UGHyperlink}[]

 

[]{#p476} 

 

[]{#related-topics}

