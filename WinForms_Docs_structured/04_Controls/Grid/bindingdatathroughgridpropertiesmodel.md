---
title: bindingdatathroughgridpropertiesmodel.md
original_path: WinForms_Docs/04_Controls/Grid/bindingdatathroughgridpropertiesmodel.md
created_at: 2025-08-05
---






#### Binding Data through GridPropertiesModel {#binding-data-through-gridpropertiesmodel style="tab-stops: 0pt"}

 

Data can be bound by using the GridPropertiesModel. To do so, there are five steps involved:

1.   Create an Entity model in the application (see [Creating the ADO.NET Entity Data Model]{.UGHyperlink}).

2.   Create a grid control in the view by adding the following code in the **Index.aspx** file.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                    |
| [   ]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().Grid\<[employee]\>([\"EntityGrid\"],[\"GridModel\"], column =\> {] |
|                                                                                                                                                                                                                                                                                                                    |
| [      column.Add(c =\> c.emp_id).HeaderText([\"Employee ID\"]);]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                    |
| [       column.Add(c =\> c.fname).HeaderText([\"First Name\"]);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                    |
| [       column.Add(c =\> c.lname).HeaderText([\"Last Name\"]);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                    |
| [       column.Add(c =\> c.minit).HeaderText([\"Min\"]);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                    |
| [       column.Add(c =\> c.hire_date).HeaderText([\"Ship City\"]).Format([\"{hire_date:dd/mm/yyyy}\"]);        })]                                                                                                             |
|                                                                                                                                                                                                                                                                                                                    |
| [             [%\>]][]                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[employee]\>([\"EntityGrid\"],[\"GridModel\"], column =\> {] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [      column.Add(c =\> c.emp_id).HeaderText([\"Employee ID\"]);]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [       column.Add(c =\> c.fname).HeaderText([\"First Name\"]);]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [       column.Add(c =\> c.lname).HeaderText([\"Last Name\"]);]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [       column.Add(c =\> c.minit).HeaderText([\"Min\"]);]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [       column.Add(c =\> c.hire_date).HeaderText([\"Ship City\"]).Format([\"{hire_date:dd/mm/yyyy}\"]);      ]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [  })][.ToString())[)]    ][]                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   Create a **GridPropertiesModel** in the **Index** method. Assign grid properties in this model and pass the model from controller to view using the **ViewData** class.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [public][ [ActionResult] Index()]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [            // Create object to GridPropertiesMode.][]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                            |
| [            [// Set the required properties.]][]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [            GridPropertiesModel][\<[employee]\> model = [new] [GridPropertiesModel]\<[employee]\>()] |
|                                                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [                DataSource = [new] [PUBSEntities]().employees,]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                            |
| [                Caption=[\"Employee Details\"],]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                            |
| [AutoFormat=[Skins].Sandune,][]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [                AllowPaging=[true],]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [                AllowSorting=[true]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [            };]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                            |
| [            ViewData\[[\"GridModel\"]\] = model;[ // Pass the model from controller to view using ViewData.]]                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| [            [return] View();]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [        }][]                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

4.   In order to work with paging and sorting actions, create a **Post** method for the **Index** actions and bind the data source to the grid.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                      |
| [  ///][ ][\<summary\>][]                    |
|                                                                                                                                                                                                                                      |
| [        [///][ Paging/sorting requests are mapped to this method. This method invokes the HtmlActionResult]]                                         |
|                                                                                                                                                                                                                                      |
| [        [///][ from the grid. Required response is generated.]]                                                                                      |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</summary\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties. ][\</param\>]] |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<returns\>]]                                                                                                  |
|                                                                                                                                                                                                                                      |
| [        [///][ HtmlActionResult returns the data displayed on the grid.]]                                                                            |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</returns\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                    |
|                                                                                                                                                                                                                                      |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                                |
|                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [            [IEnumerable] data = [new] [PUBSEntities]().employees;]                                                        |
|                                                                                                                                                                                                                                      |
| [            [return] data.GridActions\<[employee]\>();]                                                                                            |
|                                                                                                                                                                                                                                      |
| [        }]***[]***                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Run the application; the grid will then appear as seen in the following image.

 

{border="0"}

Figure 90: Entity Model Grid

[]{#related-topics}

