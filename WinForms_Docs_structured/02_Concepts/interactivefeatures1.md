---
title: interactivefeatures1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\interactivefeatures1.md
created_at: 2025-07-03
---








  









### Interactive Features {#interactive-features style="tab-stops: 0pt"}

[] 

This section elaborates on the following run time interactive features:

[] 

[·      ]Selection

[·      ]Sorting

[·      ]Column Sizing

[] 

1\. Selection Support

**[]** 

Grid Tree control has the following two types of selection support:

[] 

[·      ]**Whole Node selection**-Whole node selections involve selecting the entire row when a cell is clicked, and is enabled by setting the EnableNodeSelection property to true.  This is the default node selection type in the Grid Tree.

[·      ]**Cell Range selection**-The cell range selection support allows the selection of cell ranges within the Grid Tree control. This support is enabled by setting **EnableNodeSelection** property to ***false***.

[] 

Disabling the Selection

[] 

To disable all selection support in the Grid Tree control, set **GridTreeControl.EnableSelections** to ***false***.

[] 

Selection Features

[] 

Grid Tree control does not use the selection support inherited from the Grid control, because the selections in the Grid Tree need to be persisted, as the nodes are expanded/collapsed and sorted. The **GridTreeNode.IsSelected** property indicates whether the node is selected or not and the **GridTreeNode.SelectedColumns** property contains the names of the columns selected for the node. You can access selected nodes by using the **GridTreeControl.SelectedNodes** property.

The following code example illustrates cell range selections in the Grid Tree.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                             |
|                                                                                                                                                                                                 |
| [foreach][ ([GridTreeNode] node [in] treeGrid.SelectedNodes)] |
|                                                                                                                                                                                                 |
| [{]                                                                                                                                                         |
|                                                                                                                                                                                                 |
| [    [foreach] ([string] columnName [in] node.SelectedColumns)]                              |
|                                                                                                                                                                                                 |
| [    {]                                                                                                                                                     |
|                                                                                                                                                                                                 |
| [        [Console].Write([\"{0} \"], treeGrid.InternalGrid.GetValueFromNode(columnName, node));]            |
|                                                                                                                                                                                                 |
| [    }]                                                                                                                                                     |
|                                                                                                                                                                                                 |
| [    [Console].WriteLine();]                                                                                                        |
|                                                                                                                                                                                                 |
| [}]                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

2\. Sorting

[] 

You can enable sorting in the Grid Tree control by using **GridTreeControl.AllowSort** property. When this property is set to true, you can perform sorting on a column by clicking on the column header of the respective column. In addition, Grid Tree provides support to perform MultiColumn Sorting by holding down CTRL key and clicking the left mouse button.

 

The **GridTreeControl.InternalGrid.SortTree** method is used to sort a column in the Grid Tree programmatically. There are two overloads:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                     |
| [public][ [void] SortTree([string] colName, [ListSortDirection] dir)]                                        |
|                                                                                                                                                                                                                                                                                                     |
| [public][ [void] SortTree([string] colName, [ListSortDirection] dir, [bool] clearSort)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The first signature sorts the given column in the given direction clearing any existing sorting. The second signature gives you the option of not clearing the existing sorts, which enables multi-column sorting.

 

Here are additional members of **GridTreeControlImpl** that allows you to access sort information and provide support for customized sorting.

[] 

[·      ][public] [bool] IsPropertySorted([string] propertyName, [out] [SortState] state)[--determines whether a particular column has been sorted.]

[·      ][public] [IComparer]\<[GridTreeNode]\> SortComparer[--Allows customized sorting. The default implementation assumes the underlying node items implement IComparable and uses that implementation for the sorting comparisons within the columns. If your objects are not IComparable, then you need to provide a SortComparer that properly sorts the GridNodes depending upon the SortProperty value of **GridNode.Item**.]

[·      ][public] [string] SortProperty[-string that holds the column name to be sorted. You can specify a SortDirection by appending a space followed by either ASC or DESC. In addition, you can specify multicolumn sorts by passing several columns separated by commas. For example, \"Price ASC, Weight DESC\", which will indicate to first sort in ascending order by the Price column, and then sort in descending order by the Weight column.]

[·      ][public] [List]\<[SortState]\> SortStates[-is the list of the SortStates for the columns currently sorted in the Grid Tree control. The **SortState** class contains information regarding the direction and the property sorted, and it exposes static helper methods, which takes care of the changes between **SortStates** and the **SortProperty**.]

[] 

3\. Column Sizing

[] 

The Grid Tree control supports autosizing its columns such that the display of the tree occupies the entire width of the client area available in the Grid Tree. The sizing is done by columns occupying certain percentages of the available space. To implement this feature, the Grid Tree must be free to size with its parent.

[] 


{border="0"}Note: You cannot set the Width or HorizontalAlignment properties of the Grid Tree when this feature has been enabled.


[] 

You can enable this feature in two ways.

[] 

[·      ]The first is to set the **GridTreeControl.PercentSizingBehavior** to any value except "None".

[·      ]The second action is to populate the **GridTreeControl.Columns** collection, and to set the **GridTreeColumn.PercentWidth** property for each of the columns that have to be autosized as the Grid Tree is sized.

[] 

The following code example illustrates these settings.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion][:][GridTreeControl][ Name][=\"gridTreeControl2\"][ Grid.Row][=\"1\"][ RequestTreeItems][=\"gridTreeControl2_RequestTreeItems\"][ PercentSizingBehavior][=\"SizeUntouchedColumns\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    ][\<][syncfusion][:][GridTreeControl.Columns][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        ][\<][syncfusion][:][GridTreeColumn][ MappingName][=\"Title\"][ [ Width][=\"180\"/\>]]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        ][\<][syncfusion][:][GridTreeColumn][ MappingName][=\"FirstName\"][ PercentWidth][=\"1\"/\>]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        ][\<][syncfusion][:][GridTreeColumn][ MappingName][=\"LastName\"][ PercentWidth][=\"1\"/\>]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    ][\</][syncfusion][:][GridTreeControl.Columns][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][syncfusion][:][GridTreeControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

After setting the above properties, the Grid Tree will display three columns with the "Title" column having a fixed width of 180. The other two columns would be equally sized to fill the remaining client area.

 

When the **PercentWeight** property is enabled, the column will occupy a certain percentage of the remaining client area (after all the fixed-sized columns have been allocated). This percentage is calculated by dividing the PercentWeight property by the sum of all the PercentWeight's present in the **Columns** collection.

 

For example, in the preceding code, if you want the width of the LastName column to be three times the width of the FirstName column, then you have to set its PercentWeight property to 3.

[] 

The **PercentSizingBehavior** property provides the following options to size the columns. They are:

[] 

[·      ]**None**--No automatic sizing will be done. The displayed column width will either be the default value (gridTreeControl1.DefaultColumnWidth), or the width specified in the GridTreeColumn.Width property. This is the default behavior.

[·      ]**SizeUntouchedColumns**--This option will autosize the columns which have the PercentWidth property set, as long as the user does not explicitly change the width of this column through the UI. If the user changes the column size, the column width will not be changed as the Grid Tree is sized.

[·      ]**NoSizingIfAnyTouched**--If the user sets the size of any column through the UI, all autosizing stops and the column size will not be changed as the Grid Tree is sized.

[·      ]**SizeAlwaysPercent**--This option will not allow the user to size any column. The columns will always use the percentage sizing to determine their size as the Grid Tree is sized.

[]{#p273} 

[]{#related-topics}

