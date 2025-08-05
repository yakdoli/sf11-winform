---
title: bindingdatathroughgridbuilder.md
original_path: WinForms_Docs/04_Controls/Grid/bindingdatathroughgridbuilder.md
created_at: 2025-08-05
---






#### Binding Data through GridBuilder {#binding-data-through-gridbuilder style="tab-stops: 0pt"}

 

Data can be bound by customizing the view. To do so, there are the six steps involved:

1.   Create an Entity model in an application (see [Creating the ADO.NET Entity Data Model]{.UGHyperlink}).

2.   Create a strongly typed view (see [Creating a Strongly Typed View]{.UGHyperlink}).

3.   In the view, use the **Model** property in **Datasource** to bind the data source.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][ASPX][\]]**                                                                                         |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [\<%][=][Html.Syncfusion().Grid\<[employee]\>([\"EntityGrid\"])] |
|                                                                                                                                                                                                                                                               |
| [              .Datasource(Model)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [              .Caption([\"Employee Details\"])]                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [                 .AutoFormat([Skins].Sandune)][]                                                                                                             |
|                                                                                                                                                                                                                                                               |
| [.EnablePaging()]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [              .EnableSorting()]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [              .Column(cols =\>]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [                {]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [                    cols.Add(c =\> c.emp_id).HeaderText([\"Employee ID\"]);]                                                                                                                     |
|                                                                                                                                                                                                                                                               |
| [                    cols.Add(c =\> c.fname).HeaderText([\"First Name\"]);]                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [                    cols.Add(c =\> c.lname).HeaderText([\"Last Name\"]);]                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [                    cols.Add(c =\> c.minit).HeaderText([\"Min\"]);]                                                                                                                              |
|                                                                                                                                                                                                                                                               |
| [                    cols.Add(c =\> c.hire_date).HeaderText([\"Ship City\"]).Format([\"{hire_date:dd/mm/yyyy}\"]);]                                                       |
|                                                                                                                                                                                                                                                               |
| [                })       ]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [       [%\>]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                    |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [\@{][ Html.Syncfusion().Grid\<[employee]\>([\"EntityGrid\"])] |
|                                                                                                                                                                                                            |
| [              .Datasource(Model)]                                                                                                                                     |
|                                                                                                                                                                                                            |
| [              .Caption([\"Employee Details\"])]                                                                                               |
|                                                                                                                                                                                                            |
| [                 .AutoFormat([Skins].Sandune)][]                                                          |
|                                                                                                                                                                                                            |
| [.EnablePaging()]                                                                                                                                                      |
|                                                                                                                                                                                                            |
| [              .EnableSorting()]                                                                                                                                       |
|                                                                                                                                                                                                            |
| [              .Column(cols =\>]                                                                                                                                       |
|                                                                                                                                                                                                            |
| [                {]                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [                    cols.Add(c =\> c.emp_id).HeaderText([\"Employee ID\"]);]                                                                  |
|                                                                                                                                                                                                            |
| [                    cols.Add(c =\> c.fname).HeaderText([\"First Name\"]);]                                                                    |
|                                                                                                                                                                                                            |
| [                    cols.Add(c =\> c.lname).HeaderText([\"Last Name\"]);]                                                                     |
|                                                                                                                                                                                                            |
| [                    cols.Add(c =\> c.minit).HeaderText([\"Min\"]);]                                                                           |
|                                                                                                                                                                                                            |
| [                    cols.Add(c =\> c.hire_date).HeaderText([\"Ship City\"]).Format([\"{hire_date:dd/mm/yyyy}\"]);]    |
|                                                                                                                                                                                                            |
| [                }).Render();     ]                                                                                                                                    |
|                                                                                                                                                                                                            |
| [       [}]]                                                                                                                               |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Set the data source and render the view.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [///][ ][\<summary\>][]                |
|                                                                                                                                                                                                                                |
| [        [///][ Used for rendering the grid initially.]]                                                                                        |
|                                                                                                                                                                                                                                |
| [///][ ][\</summary\>][]               |
|                                                                                                                                                                                                                                |
| [        [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]] |
|                                                                                                                                                                                                                                |
| [        [public] [ActionResult] Index()]                                                                                                     |
|                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [            [var] data = [new] [PUBSEntities]().employees; ]                                                            |
|                                                                                                                                                                                                                                |
| [            [return] View(data);]                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [        }****]                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In order to work with paging and sorting actions, create a **Post** method for the **Index** actions and bind the data source to the grid, as seen in the code below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [///][ ][\<summary\>][]                                        |
|                                                                                                                                                                                                                                                        |
| [        [///][ Sorting/paging requests are mapped to this method.]]                                                                                                    |
|                                                                                                                                                                                                                                                        |
| [        [///][ This method invokes the HtmlActionResult from the grid.]]                                                                                               |
|                                                                                                                                                                                                                                                        |
| [        [///][ The required response is generated.]]                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [        [///][ ][\</summary\>]]                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [        [///][ ][\<returns\>][HtmlActionResult returns the data displayed on the grid.][\</returns\>]] |
|                                                                                                                                                                                                                                                        |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                                                  |
|                                                                                                                                                                                                                                                        |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [            [IEnumerable] data = [new] [PUBSEntities]().employees;]                                                                          |
|                                                                                                                                                                                                                                                        |
| [            [return] data.GridActions\<[employee]\>();]                                                                                                              |
|                                                                                                                                                                                                                                                        |
| [        }][]                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Run the application; the grid will then appear as seen in the following image.

 

{border="0"}

Figure 89: Entity Model Grid

[]{#related-topics}

