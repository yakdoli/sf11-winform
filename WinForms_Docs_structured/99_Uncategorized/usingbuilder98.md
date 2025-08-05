---
title: usingbuilder98.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder98.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how you can bind the data source through the webservice.

1.   In **View**, invoke the Listbox Helper with the control ID as the first argument and set the WebService URL for the webservice binding.


Note: Column mapping can be  done as in the JSON mode.


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [    ] [\<%] [ Html.MobSyncfusion().ListBox([\"lbDatabinding\"])] |
|                                                                                                                                                                                                                                                                  |
| **[              .ActionMode([ActionMode].WebService)]**                                                                                                                                |
|                                                                                                                                                                                                                                                                  |
| **[              .WebServiceUrl([\"/Models/Orders.svc/RenderData\"])]**                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| [              .Items(item =\>]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| [              {]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                  |
| [                  **item.Add()**]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                  |
| **[                      .Text([\"\${Text}\"]).ImageUrl([\"\${ImageUrl}\"])]**                                                                                  |
|                                                                                                                                                                                                                                                                  |
| **[                      .Children([\"Children\"], ch =\>]**                                                                                                                            |
|                                                                                                                                                                                                                                                                  |
| **[                      {]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                  |
| **[                          ch.Add().Text([\"\${Text}\"])]**                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| **[                              .Children([\"Street\"], ch1 =\>]**                                                                                                                     |
|                                                                                                                                                                                                                                                                  |
| **[                                {]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                  |
| **[                                    ch1.Add().Text([\"\${Text}\"]);]**                                                                                                               |
|                                                                                                                                                                                                                                                                  |
| **[                                 });]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                  |
| **[                       });]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                  |
| [               })]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                  |
| [               .Render();]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                  |
| [    [%\>]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[                       ]**

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [    ] [\@{] [ Html.MobSyncfusion().ListBox([\"lbDatabinding\"])] |
|                                                                                                                                                                                                                           |
| **[              .ActionMode([ActionMode].WebService)]**                                                                                                      |
|                                                                                                                                                                                                                           |
| **[              .WebServiceUrl([\"/Models/Orders.svc/RenderData\"])]**                                                                                       |
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

 

2.   Create a web method **(RenderData)** for binding the listbox to the webservice using the object datasource. The webservice method should return the ListBoxWebService object.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [    ] []                                                                                                                 |
|                                                                                                                                                                                                   |
| **[\[Orders.svc\]]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                                        |
|                                                                                                                                                                                                   |
| [\[[OperationContract]\]]                                                                                                             |
|                                                                                                                                                                                                   |
| [        [public][ListBoxWebService] RenderData([ListBoxParams] webParams)]              |
|                                                                                                                                                                                                   |
| [        {]                                                                                                                                                   |
|                                                                                                                                                                                                   |
| [            [ListBoxWebService] sdf = [new][ListBoxWebService]();]                      |
|                                                                                                                                                                                                   |
| [            [List]\<[Countries]\> \_Datasrc = [this].RenderDataSource().ToList();]      |
|                                                                                                                                                                                                   |
| [            [IEnumerable]\<[DTO]\> data = [from] o [in] \_Datasrc] |
|                                                                                                                                                                                                   |
| [                                    [select][new][DTO]]                                    |
|                                                                                                                                                                                                   |
| [                                    {]                                                                                                                       |
|                                                                                                                                                                                                   |
| [                                        Text = o.Text,]                                                                                                      |
|                                                                                                                                                                                                   |
| [                                        Children = o.Children]                                                                                               |
|                                                                                                                                                                                                   |
| [                                    };]                                                                                                                      |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [            [return] data.ListBoxWebServiceAction\<[DTO]\>();]                                                  |
|                                                                                                                                                                                                   |
| [        }]                                                                                                                                                   |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

3.   Build and run the application.

 

 

[ {border="0"} ]

Figure 67: Listbox - Jsonbinding[]

[] 

 

[]{#related-topics}

