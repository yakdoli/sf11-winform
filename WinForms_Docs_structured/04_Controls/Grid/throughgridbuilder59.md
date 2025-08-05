---
title: throughgridbuilder59.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder59.md
created_at: 2025-08-05
---






#### Through Grid Builder {#through-grid-builder style="tab-stops: 0pt"}

1.  Create a model in the application (Refer to ).

2.  Create a strongly typed view (Refer to ). In the view you can use its **Model** property in **Datasource()** in order to bind the data source. 

3.  To enable the paging feature for your grid you should use the **EnablePaging()** method.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml[\]]]**                                                                                             |
|                                                                                                                                                                                                                                   |
| [\@{][Html.MobSyncfusion().Grid\<[Standings]\>([\"grid\"])] |
|                                                                                                                                                                                                                                   |
| [           .Datasource(Model).Caption([\"Foot Ball Team Standings \"])]                                                                                 |
|                                                                                                                                                                                                                                   |
| [           .ActionMode([MobActionMode].Server)]                                                                                                         |
|                                                                                                                                                                                                                                   |
| [           .Column(col =\>]                                                                                                                                                     |
|                                                                                                                                                                                                                                   |
| [           {]                                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| [               col.Add(c =\> c.Team).HeaderText([\"Team\"]);]                                                                                           |
|                                                                                                                                                                                                                                   |
| [               col.Add(c =\> c.Won).HeaderText([\"W\"]);]                                                                                               |
|                                                                                                                                                                                                                                   |
| [               col.Add(c =\> c.Loss).HeaderText([\"L\"]);]                                                                                              |
|                                                                                                                                                                                                                                   |
| [               col.Add(c =\> c.Percent).HeaderText([\"PCT\"]);]                                                                                         |
|                                                                                                                                                                                                                                   |
| [               col.Add(c =\> c.L10).HeaderText([\"L10\"]);]                                                                                             |
|                                                                                                                                                                                                                                   |
| [           })]                                                                                                                                                                  |
|                                                                                                                                                                                                                                   |
| [          **.EnablePaging()**]                                                                                                                                                  |
|                                                                                                                                                                                                                                   |
| **[                       .PageSettings(p =\> p.ShowPager([true]).PageSize(12))]**                                                                          |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [              .Render();]                                                                                                                                                       |
|                                                                                                                                                                                                                                   |
| [}][]                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                    |
| [\<%][=][Html.MobSyncfusion().Grid\<[Standings]\>([\"grid\"])] |
|                                                                                                                                                                                                                                                                                                    |
| [            .Datasource(Model).Caption([\"Foot Ball Team Standings\"])]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                    |
| [           .ActionMode([MobActionMode].Server)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                    |
| [           .Column(col =\> ]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                    |
| [           {]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                    |
| [               col.Add(c =\> c.Team).HeaderText([\"Team\"]);]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                    |
| [               col.Add(c =\> c.Won).HeaderText([\"W\"]);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                    |
| [               col.Add(c =\> c.Loss).HeaderText([\"L\"]);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [               col.Add(c =\> c.Percent).HeaderText([\"PCT\"]);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                    |
| [               col.Add(c =\> c.L10).HeaderText([\"L10\"]);]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                    |
| [           })]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                    |
| [             **.EnablePaging()**]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                    |
| **[                       .PageSettings(p =\> p.ShowPager([true]).PageSize(12))]**                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                    |
| [     [%\>]]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.  Set its data source and render the view.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  **[Controller]**                                                                                                                                                           |
|                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                               |
| [///][ ][\<summary\>]                                                     |
|                                                                                                                                                                                                                               |
| [        [///][ Used to bind the Grid.]]                                                                                                       |
|                                                                                                                                                                                                                               |
| [        [///][ ][\</summary\>]]                                                                                          |
|                                                                                                                                                                                                                               |
| [        [///][ ][\<returns\>][View page, it displays the Grid][\</returns\>]] |
|                                                                                                                                                                                                                               |
| [       ][public][ [ActionResult] Index()]         |
|                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                  |
|                                                                                                                                                                                                                               |
| [            [var] data = [StandingsDetails].GetData();]                                                                        |
|                                                                                                                                                                                                                               |
| [            [return] View(data);]                                                                                                                      |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.  In order to work with paging and sorting actions, create a **Post** method for **Index** actions and bind the data source to the grid as shown in the following code.

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [  ///][ ][\<summary\>][]                    |
|                                                                                                                                                                                                                                      |
| [        [///][ Paging/sorting Requests are mapped to this method. This method invokes the MobHtmlActionResult]]                                      |
|                                                                                                                                                                                                                                      |
| [        [///][ from the grid. Required response is generated.]]                                                                                      |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</summary\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties. ][\</param\>]] |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<returns\>]]                                                                                                  |
|                                                                                                                                                                                                                                      |
| [        [///][ MobHtmlActionResult returns the data displayed on the grid.]]                                                                         |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</returns\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                    |
|                                                                                                                                                                                                                                      |
| [       [public] [ActionResult] Index([MobGridParams] args)]                                                                |
|                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [            [var] data = [StandingsDetails].GetData();]                                                                                            |
|                                                                                                                                                                                                                                      |
| [            [return] data.MobGridJSONActions\<[Standings]\>();]                                                                                    |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.  Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 42: Grid---Paging

 

7.  Swipe up on the content area to navigate to the next page. Then the pager bar will be displayed at the bottom of the page as shown in the following screenshot.

 

{border="0"}

Figure 43: Grid---Pager Bar

[]{#related-topics}

