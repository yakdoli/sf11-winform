---
title: servermode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\servermode.md
created_at: 2025-07-03
---








  









### Server Mode {#server-mode style="tab-stops: 0pt"}

Essential Grid for ASP.NET MVC will perform service-side requests (HTTP POST) when doing paging, sorting, grouping, and filtering actions. This is called "server binding."

For the first request, bind the grid with data using the **Datasource** property and render the view. For subsequent paging, sorting, and filtering actions you need to write a post action method in your controller. The grid is fully AJAX enabled, so while calling grid actions such as paging, sorting, and filtering, the entire view won't be rendered. It just calls the **GridHtmlActionResult** to update the grid.

This can be achieved in the following ways.

More:







