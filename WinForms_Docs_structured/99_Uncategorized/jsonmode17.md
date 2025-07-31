---
title: jsonmode17.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\jsonmode17.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### JSON Mode {#json-mode style="tab-stops: 0pt"}

The following steps explain how you can bind the data source to the listbox control in the JSON mode:

1.   In **View**, invoke the Listbox Helper with the control ID as the first argument and use the Items() for column mapping.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]    ]                                                                                                                             |
|                                                                                                                                                                                |
| [\<%] [ Html.MobSyncfusion().ListBox([\"lbDatabinding\"])] |
|                                                                                                                                                                                |
| **[              .ActionMode([ActionMode].Json)]**                                                                 |
|                                                                                                                                                                                |
| [              .Items(item =\>]                                                                                                            |
|                                                                                                                                                                                |
| [              {]                                                                                                                          |
|                                                                                                                                                                                |
| [                  **item.Add()**]                                                                                                         |
|                                                                                                                                                                                |
| **[                      .Text([\"\${Text}\"]).ImageUrl([\"\${ImageUrl}\"])]**             |
|                                                                                                                                                                                |
| **[                      .Children([\"Children\"], ch =\>]**                                                       |
|                                                                                                                                                                                |
| **[                      {]**                                                                                                              |
|                                                                                                                                                                                |
| **[                          ch.Add().Text([\"\${Text}\"])]**                                                      |
|                                                                                                                                                                                |
| **[                              .Children([\"Street\"], ch1 =\>]**                                                |
|                                                                                                                                                                                |
| **[                                {]**                                                                                                    |
|                                                                                                                                                                                |
| **[                                    ch1.Add().Text([\"\${Text}\"]);]**                                          |
|                                                                                                                                                                                |
| **[                                 });]**                                                                                                 |
|                                                                                                                                                                                |
| **[                       });]**                                                                                                           |
|                                                                                                                                                                                |
| [               })]                                                                                                                        |
|                                                                                                                                                                                |
| [               .Render();]                                                                                                                |
|                                                                                                                                                                                |
| [    [%\>]]                                                                                                    |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| []                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [    ] [\@{] [ Html.MobSyncfusion().ListBox([\"lbDatabinding\"])] |
|                                                                                                                                                                                                                           |
| **[              .ActionMode([ActionMode].Json)]**                                                                                                            |
|                                                                                                                                                                                                                           |
| [              .Items(item =\>]                                                                                                                                                       |
|                                                                                                                                                                                                                           |
| [              {]                                                                                                                                                                     |
|                                                                                                                                                                                                                           |
| [                  **item.Add()**]                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| **[                      .Text([\"\${Text}\"]).ImageUrl([\"\${ImageUrl}\"])]**                                                        |
|                                                                                                                                                                                                                           |
| **[                      .Children([\"Children\"], ch =\>]**                                                                                                  |
|                                                                                                                                                                                                                           |
| **[                      {]**                                                                                                                                                         |
|                                                                                                                                                                                                                           |
| **[                          ch.Add().Text([\"\${Text}\"])]**                                                                                                 |
|                                                                                                                                                                                                                           |
| **[                              .Children([\"Street\"], ch1 =\>]**                                                                                           |
|                                                                                                                                                                                                                           |
| **[                                {]**                                                                                                                                               |
|                                                                                                                                                                                                                           |
| **[                                    ch1.Add().Text([\"\${Text}\"]);]**                                                                                     |
|                                                                                                                                                                                                                           |
| **[                                 });]**                                                                                                                                            |
|                                                                                                                                                                                                                           |
| **[                       });]**                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [               })]                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [               .Render();]                                                                                                                                                           |
|                                                                                                                                                                                                                           |
| [}]                                                                                                                                                               |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   [In the post action, pass the data source to the listbox control.]

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [    ] []                                                                                              |
|                                                                                                                                                                                |
| **[\[Controller\]]**                                                                                                                       |
|                                                                                                                                                                                |
| **[]**                                                                                                                                     |
|                                                                                                                                                                                |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                      |
|                                                                                                                                                                                |
| [        [public][ActionResult] LBDatabinding([ListBoxParams] param)] |
|                                                                                                                                                                                |
| [        {]                                                                                                                                |
|                                                                                                                                                                                |
| [            [IEnumerable] data = [this].RenderDataSource().ToList();]                        |
|                                                                                                                                                                                |
| [            param.CollectionSize = 20;]                                                                                                   |
|                                                                                                                                                                                |
| [            [return] data.ListBoxJsonAction\<[Countries]\>(param);]                          |
|                                                                                                                                                                                |
| [        }]                                                                                                                                |
|                                                                                                                                                                                |
| []                                                                                                                     |
|                                                                                                                                                                                |
| []                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

3.   Build and run the application.

 

 

[ {border="0"} ]

Figure 66: Listbox - Jsonbinding[]

[] 

 

[]{#related-topics}

