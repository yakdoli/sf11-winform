---
title: columnsizing.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\columnsizing.md
created_at: 2025-07-03
---






#### Column Sizing {#column-sizing style="tab-stops: 0pt"}

The GridTree control supports autosizing its columns such that the display of the tree occupies the entire width of the client area available in the Grid Tree. The sizing is done by columns occupying certain percentages of the available space. To implement this feature, the Grid Tree must be free to size with its parent.

 


{border="0"}Note: You cannot set the Width or HorizontalAlignment properties of the Grid Tree when this feature has been enabled.


 

You can enable this feature in two ways.

 

The first is to set the GridTreeControl.PercentSizingBehavior to any value except "None".

The second action is to populate the GridTreeControl.Columns collection, and to set the GridTreeColumn.PercentWidth property for each of the columns that have to be autosized as the Grid Tree is sized.

 

The following code example illustrates these settings.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
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

 

After setting the above properties, the Grid Tree will display three columns with the "Title" column having a fixed width of 180. The other two columns would be equally sized to fill the remaining client area.

 

When the PercentWeight property is enabled, the column will occupy a certain percentage of the remaining client area (after all the fixed-sized columns have been allocated). This percentage is calculated by dividing the PercentWeight property by the sum of all the PercentWeight's present in the Columns collection.

 

For example, in the preceding code, if you want the width of the LastName column to be three times the width of the FirstName column, then you have to set its PercentWeight property to 3.

 

The PercentSizingBehavior property provides the following options to size the columns. They are:

 

[·      ]None--No automatic sizing will be done. The displayed column width will either be the default value (gridTreeControl1.DefaultColumnWidth), or the width specified in the GridTreeColumn.Width property. This is the default behavior.

[·      ]SizeUntouchedColumns--This option will autosize the columns which have the PercentWidth property set, as long as the user does not explicitly change the width of this column through the UI. If the user changes the column size, the column width will not be changed as the Grid Tree is sized.

[·      ]NoSizingIfAnyTouched--If the user sets the size of any column through the UI, all autosizing stops and the column size will not be changed as the Grid Tree is sized.

[·      ]SizeAlwaysPercent--This option will not allow the user to size any column. The columns will always use the percentage sizing to determine their size as the Grid Tree is sized.

 

[]{#p315} 

[]{#related-topics}

