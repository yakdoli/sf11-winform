---
title: servermode13.md
original_path: WinForms_Docs/99_Uncategorized/servermode13.md
created_at: 2025-08-05
---








  









### Server Mode {#server-mode style="tab-stops: 0pt"}

[Essential Mobile Grid for ASP.NET MVC will perform service-side requests (HTTP POST) when doing operations like paging and sorting. This is called "server binding."]

[For the first request, bind the grid with data using the **Datasource** property and render the view. For subsequent paging and sorting actions you need to write a **Post** action method in your controller. The grid is fully AJAX enabled, so while calling grid actions such as paging and sorting, the entire view won't be rendered. It just calls the **MobGridHtmlActionResult** to update the grid.]

[This can be achieved in the following ways.]



]

More:







