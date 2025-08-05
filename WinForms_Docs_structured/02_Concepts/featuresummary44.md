---
title: featuresummary44.md
original_path: WinForms_Docs/02_Concepts/featuresummary44.md
created_at: 2025-08-05
---








  









## Feature Summary {#feature-summary style="tab-stops: 0pt"}

[This section will walk you through all the features of the Chart control.]

**Paging**

Essential Grid for Mobile MVC offers complete navigation support to easily switch between the pages through swipe-up and swipe-down actions on the grid content area. Also, a pager bar will be available at the bottom of the page and it will be visible only on swiping the grid content area. It facilitates splitting up huge grid data and displays viewable sets of grid rows on each page.

{border="0"}

Figure 32: Paging in a Grid

**Sorting**

Sorting is defined as the process of arranging items/records in some ordered sequence. Essential Grid for Mobile MVC supports arranging table data in ascending or descending order based on the column header that is touched. The order switches between ascending, descending, and clearing the sort order each time you touch a column header for sorting. It supports two types of sorting---normal and menu sorting.

 

{border="0"}

Figure 33: Normal Sorting in a Grid

 

 

{border="0"}

Figure 34: Menu Sorting in a Grid

 

**JSON Grid**

Essential Grid for Mobile MVC also supports a JSON mode in which you can perform all the grid operations. The performance of these operations in JSON mode will be much faster when compared to the server mode.

 

{border="0"}

Figure 35: JSON Grid

QueryCellAction

[Grid formatting can be applied to different grid cell elements dynamically at run time. This can be achieved by proper handling of the **QueryCellInfo** action. It provides the **Htmlattributes** object for a cell on demand.]

**[QueryCellInfo]**[ is raised every time a request is made to access the style information for a cell. You can do any type of cell formatting with this event.]

{border="0"}

Figure 36: Grid Customization Using QueryCell Action[]

**Conditional Formatting**

This feature is used to format grid content based on some condition specified by the user.

 

{border="0"}

Figure 37: Conditional Formatting in a Grid

 

[]{#related-topics}

