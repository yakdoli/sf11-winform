---
title: throughthejsonmode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughthejsonmode.md
created_at: 2025-07-03
---






##### Through the JSON Mode {#through-the-json-mode style="tab-stops: 0pt"}

The filtering technique can be incorporated into the MultiColumnDropDown control in MVC using the **Builder** in the JSON mode:

Using Builder

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().MultiColumnDropDown\<Sample.Models.[Student]\>([\"MultiColumnDD\"]).ActionMode([ActionMode].JSON)] |
|                                                                                                                                                                                                                                                                                                                                                    |
| [        .DataSource(Model)]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [        .Columns(column=\>{column.Add(p =\> p.Title).HeaderText([\"Course Title\"]);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                    |
| [              column.Add(P =\> P.Duration).Format([\"{Duration} hrs\"]);]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [              column.Add(p =\> p.CourseFees).Format([\"{CourseFees:c}\"]).HeaderText([\"Course Fees\"]);]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| [              column.Add(p =\> p.CGPA);]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            }).AllowSorting([true]).DisplayExpression([new] [int]\[3\]{1,3,4})]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            .PopupPanelWidth(700).Width(700).AllowFiltering([true])]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| [        ]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| [        [%\>]]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                |
| [\@{][Html.Syncfusion().MultiColumnDropDown\<Sample.Models.[Student]\>([\"MultiColumnDD\"]).ActionMode([ActionMode].JSON)] |
|                                                                                                                                                                                                                                                                                                |
| [        .DataSource(Model)]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                |
| [        .Columns(column=\>{column.Add(p =\> p.Title).HeaderText([\"Course Title\"]);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                |
| [              column.Add(P =\> P.Duration).Format([\"{Duration} hrs\"]);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                |
| [              column.Add(p =\> p.CourseFees).Format([\"{CourseFees:c}\"]).HeaderText([\"Course Fees\"]);]                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| [              column.Add(p =\> p.CGPA);]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| [            }).AllowSorting([true]).DisplayExpression([new] [int]\[3\]{1,3,4})]                                                                                                            |
|                                                                                                                                                                                                                                                                                                |
| [            .PopupPanelWidth(700).Width(700).AllowFiltering([true]).Render();]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                |
| [        ]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| [        [}]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                 |
|                                                                                                                                                                                                      |
| **[]**                                                                                                                                                           |
|                                                                                                                                                                                                      |
| [public][ [ActionResult] index()]                                                       |
|                                                                                                                                                                                                      |
| [        {]                                                                                                                                                      |
|                                                                                                                                                                                                      |
| [            [var] data = [new] [StudentDataContext]().Student.Take(200).ToList();           ] |
|                                                                                                                                                                                                      |
| [            [return] View(data);]                                                                                                          |
|                                                                                                                                                                                                      |
| [        }]                                                                                                                                                      |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                    |
|                                                                                                                                                                                                      |
| [        [public] [ActionResult] index([PagingParams] args)]                                |
|                                                                                                                                                                                                      |
| [        {]                                                                                                                                                      |
|                                                                                                                                                                                                      |
| [            [IEnumerable] data = [new] [StudentDataContext]().Student.Take(200).ToList();] |
|                                                                                                                                                                                                      |
| [            [ActionResult] result = data.GridJSONActions\<[Student]\>();]                                       |
|                                                                                                                                                                                                      |
| [            [return] result;]                                                                                                              |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [        }]                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 334: MultiColumnDropDown Control with Filtering Enabled

**[]** 

{border="0"}

Figure 335: Filtered with "Duration" Value as 45 hrs**[]**

 

 

[]{#related-topics}

