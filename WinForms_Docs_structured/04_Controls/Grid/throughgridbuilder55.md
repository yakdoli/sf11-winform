---
title: throughgridbuilder55.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridbuilder55.md
created_at: 2025-07-03
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

The steps to work with the auto wrap feature through **GridBuilder** are as follows:

1.   Create a model in the application.

2.   Create a strongly typed view.

3.   In the view, use the **Model** property in the **Datasource()** to bind the data source.

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Grid\<[EditableOrder]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                  |
| [       .Datasource(Model)]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                  |
| [       .Caption([\"Orders\"])]                                                                                                                                                      |
|                                                                                                                                                                                                                                                  |
| [       \-\-\-\-\-\-\--]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                  |
| [       \-\-\-\-\-\-\--]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                  |
| [.AutoFormat([Skins].Sandune) ]                                                                                                                                                      |
|                                                                                                                                                                                                                                                  |
| [       .AllowResizing([true])]                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [       .AllowAutoWrap([true)]]                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [       .ResizeSettings(resize =\> {]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                  |
| [               resize.ResizeToFit([true]);]                                                                                                                                            |
|                                                                                                                                                                                                                                                  |
| [               resize.ClipContent([true]);]                                                                                                                                            |
|                                                                                                                                                                                                                                                  |
| [        })   ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                  |
| [%\>]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                          |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\@{][Html.Grid\<[EditableOrder]\>([\"Grid1\"])] |
|                                                                                                                                                                                              |
| [       .Datasource(Model)]                                                                                                                              |
|                                                                                                                                                                                              |
| [       .Caption([\"Orders\"])]                                                                                                  |
|                                                                                                                                                                                              |
| [       \-\-\-\-\-\-\--]                                                                                                                                 |
|                                                                                                                                                                                              |
| [       \-\-\-\-\-\-\--]                                                                                                                                 |
|                                                                                                                                                                                              |
| [.AutoFormat([Skins].Sandune) ]                                                                                                  |
|                                                                                                                                                                                              |
| [       .AllowResizing([true])]                                                                                                     |
|                                                                                                                                                                                              |
| [       .AllowAutoWrap([true])]                                                                                                     |
|                                                                                                                                                                                              |
| [       .ResizeSettings(resize =\> {]                                                                                                                    |
|                                                                                                                                                                                              |
| [               resize.ResizeToFit([true]);]                                                                                        |
|                                                                                                                                                                                              |
| [               resize.ClipContent([true]);]                                                                                        |
|                                                                                                                                                                                              |
| [        }).Render();   ]                                                                                                                                |
|                                                                                                                                                                                              |
| [}]                                                                                                                                  |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                 |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [public][ ActionResult AutoWrap()]                                              |
|                                                                                                                                                                      |
| [{]                                                                                                                              |
|                                                                                                                                                                      |
| [            [return] View([OrderRepository].GetAllRecords());]                     |
|                                                                                                                                                                      |
| [}]                                                                                                                              |
|                                                                                                                                                                      |
| [\[AcceptVerbs(HttpVerbs.Post)\]]                                                                                                |
|                                                                                                                                                                      |
| [public][ ActionResult AutoWrap(PagingParams args)]                             |
|                                                                                                                                                                      |
| [{]                                                                                                                              |
|                                                                                                                                                                      |
| [     [IEnumerable] data = [new] NorthwindDataContext().Orders.Take(200).ToList();] |
|                                                                                                                                                                      |
| [     [return] data.GridActions\<Order\>();]                                                                |
|                                                                                                                                                                      |
| [}]                                                                                                                              |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| []                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

