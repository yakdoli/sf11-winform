---
title: servermode16.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\servermode16.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Server Mode {#server-mode style="tab-stops: 0pt"}

 

The following steps explain how you can bind the data source to the listbox control in the Server mode:

1.   In Controller, pass the data source through view data.

 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                     |
|                                                                                                                                                                              |
| **[]**                                                                                                                                   |
|                                                                                                                                                                              |
| [  ]                                                                                                                                     |
|                                                                                                                                                                              |
| [        [public][ActionResult] LBDatabinding()]                                            |
|                                                                                                                                                                              |
| [        {]                                                                                                                              |
|                                                                                                                                                                              |
| [            IEnumerable] [ model = [this].RenderDataSource();] |
|                                                                                                                                                                              |
| [            [return] View(model);]                                                                                 |
|                                                                                                                                                                              |
| [        }]                                                                                                                              |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| []                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In **View**, and invoke the Listbox Helper with the control ID as the first argument and configure the **BindDataSource()** . For column mapping, use the MapTo() method.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [    ] [\<%] [ Html.MobSyncfusion().ListBox([\"lbDatabinding\"])] |
|                                                                                                                                                                                                                           |
| [       **.ActionMode([ActionMode].Server)**]                                                                                                                 |
|                                                                                                                                                                                                                           |
| [       .**BindDataSource**(Model, map =\>]                                                                                                                                           |
|                                                                                                                                                                                                                           |
| [       {]                                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| [           map.MapTo\<[Countries]\>(binding =\>]                                                                                                             |
|                                                                                                                                                                                                                           |
| [           {]                                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [               binding.ItemDataBound((item, nd) =\>]                                                                                                                                 |
|                                                                                                                                                                                                                           |
| [               {]                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [                   item.Text = nd.Text;]                                                                                                                                             |
|                                                                                                                                                                                                                           |
| [                   item.ImageUrl = nd.ImageUrl;]                                                                                                                                     |
|                                                                                                                                                                                                                           |
| [               })]                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [              .Children(nd =\> nd.Children);]                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [           });]                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [           map.MapTo\<[Cities]\>(binding =\>]                                                                                                                |
|                                                                                                                                                                                                                           |
| [           {]                                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [               binding.ItemDataBound((item, snd) =\>]                                                                                                                                |
|                                                                                                                                                                                                                           |
| [               {]                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [                   item.Text = snd.Text;]                                                                                                                                            |
|                                                                                                                                                                                                                           |
| [               });]                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [           });]                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [       })]                                                                                                                                                                           |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [       .Render();]                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [    [%\>]]                                                                                                                                               |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                               |
|                                                                                                                                                                                                                          |
| [    ] [\@{] [Html.MobSyncfusion().ListBox([\"lbDatabinding\"])] |
|                                                                                                                                                                                                                          |
| [       **.ActionMode([ActionMode].Server)**]                                                                                                                |
|                                                                                                                                                                                                                          |
| [       .**BindDataSource**(Model, map=\>]                                                                                                                                           |
|                                                                                                                                                                                                                          |
| [           {]                                                                                                                                                                       |
|                                                                                                                                                                                                                          |
| [               map.MapTo\<[Countries]\>(binding =\>]                                                                                                        |
|                                                                                                                                                                                                                          |
| [                   {]                                                                                                                                                               |
|                                                                                                                                                                                                                          |
| [                       binding.ItemDataBound((item, nd) =\>]                                                                                                                        |
|                                                                                                                                                                                                                          |
| [                      {]                                                                                                                                                            |
|                                                                                                                                                                                                                          |
| [                          item.Text = nd.Text;]                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [                          item.ImageUrl = nd.ImageUrl;]                                                                                                                             |
|                                                                                                                                                                                                                          |
| [                      })]                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| [                      .Children(nd=\>nd.Children);]                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [                   });]                                                                                                                                                             |
|                                                                                                                                                                                                                          |
| [               map.MapTo\<[Cities]\>(binding =\>]                                                                                                           |
|                                                                                                                                                                                                                          |
| [               {]                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [                   binding.ItemDataBound((item, snd) =\>]                                                                                                                           |
|                                                                                                                                                                                                                          |
| [                          {]                                                                                                                                                        |
|                                                                                                                                                                                                                          |
| [                              item.Text = snd.Text;]                                                                                                                                |
|                                                                                                                                                                                                                          |
| [                          });]                                                                                                                                                      |
|                                                                                                                                                                                                                          |
| [               });]                                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [           })]                                                                                                                                                                      |
|                                                                                                                                                                                                                          |
| [      ]                                                                                                                                                                             |
|                                                                                                                                                                                                                          |
| [       .Render();]                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [}]                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application.

 

[ {border="0"} ]

Figure 65: Listbox - Databinding[]

 

[]{#related-topics}

