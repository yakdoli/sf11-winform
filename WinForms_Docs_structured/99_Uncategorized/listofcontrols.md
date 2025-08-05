---
title: listofcontrols.md
original_path: WinForms_Docs/99_Uncategorized/listofcontrols.md
created_at: 2025-08-05
---








  









## List of Controls {#list-of-controls style="tab-stops: 0pt"}

[] 

Essential Grid provides the following controls.

[] 

[·      ]**Grid Control**-This class is derived from GridControlBase. It is the primary class that encapsulates both the state persistence (including data persistence) and the rendering of the grid. Unless you are using one of the special grids (Grid Data Bound Grid, Grid Grouping control, or Grid List control), GridControl is the class you will use. This is a cell-oriented grid which will easily allow you to set both row and column properties, as well as set cell specific properties for the grid to hold the data. It can also be used in a virtual mode where the data is provided on demand or the Grid control can physically hold the data for you.

 

[·      ]**Grid Data Bound Grid**-This class is also derived from GridControlBase. This control is more column-oriented than the Grid control. It is primarily used as a grid bound to a data source that supports either IList or IListSource. Classes such as ArrayList, DataTable, and DataView are included in this collection of possible data sources. Grid Data Bound Grid has a collection property called GridBoundColumns, that maintains the column properties which is similar to the System.Windows.Forms.DataGridColumnStyle class. It is this property that allows Grid Data Bound Grid to be described as a column-oriented grid.

 

[·      ]**Grid Grouping Control**-This grouping control which is derived from the control class implements several interfaces that add Grouping support to this class. If you need grouping support, multi-column sort support, or true nested-table hierarchical support in a grid, then this control is the one to be used. You can easily add expression columns, filter columns, and summary rows to this grid, as well as bind it to any IList data source. It can be fully designed by using Visual Studio.

 

[·      ]**Grid List Control**-This class is derived from System.Windows.Forms.ListControl, but can display multiple columns in its list. It has a GridControl object as a property of the class. This Grid member gives you grid-like access to a ListControl, and also provides both the data and formatting for the list control. This control is easy to use, provided your data source has the exact data you want displayed. But if you need to customize this control by hiding columns in your data source or changing column names, then generally using either the Grid Data Bound Grid or the Grid control in the list box mode is a simpler solution. This control exists so it can serve as the drop list object for the combo box that serves as a cell control.

 

[·      ]**Grid Record Navigation Control**-This class provides MS Access-like navigation support. It is normally used in conjunction with the Grid Data Bound Grid to display record numbers, and to allow record scrolling within the grid through a record information window which is displayed at the lower-left corner of the grid. You can also use it in conjunction with a Grid control.

 

[·      ]**Grid Aware Text Box**-This class is derived from System.Windows.Forms.TextBox. It allows you to bind it to the CurrentCell of either a Grid control or a Grid Data Bound Grid. The standard use for such a text box is to provide a special edit bar for editing grid cells or to serve as a formula bar in a formula grid.

 

[]{#p35} 

 

[]{#related-topics}

