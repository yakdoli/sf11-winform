---
title: databinding48.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databinding48.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Data-binding {#data-binding style="tab-stops: 0pt"}

The Mobile Tab control for Tools MVC supports data-binding, to populate Tab items so that the columns of a table can be mapped to the Tab properties, such as Text, image URL, Value, Navigate URL, etc.

Properties

+----------------+-----------------------------------------------------+------------------+------------------+-------------+
| Name           | Description                                         | Type of property | Value it accepts | Dependency  |
+================+=====================================================+==================+==================+=============+
| BindDataSource | Allows you to bind the datasource to the Tab items. | IEnumerable      |                  | NA          |
|                |                                                     |                  |                  |             |
|                |                                                     |                  |                  |             |
|                |                                                     |                  |                  |             |
|                |                                                     |                  |                  |             |
+----------------+-----------------------------------------------------+------------------+------------------+-------------+

**[]**  

 

The following steps explain how you can bind the data to the TabItems:

1.   In the controller, pass the datasource through ViewData.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                    |
|                                                                                                                                               |
| [public] [ [ActionResult] Tab()] |
|                                                                                                                                               |
| [        {]                                                                                               |
|                                                                                                                                               |
| [            ViewData.Model = [NavigationDataBuilder].GetCollection();]           |
|                                                                                                                                               |
| [            [return] View();]                                                       |
|                                                                                                                                               |
| [        }]                                                                                               |
|                                                                                                                                               |
| []                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   In **View**, invoke the TabHelper with the Control ID as the first argument and set DataSource for the TabItems using the BindDataSource().

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                           |
|                                                                                                                                                                      |
| **[\[ASPX\]]**                                                                                                                   |
|                                                                                                                                                                      |
| []                                                                                                           |
|                                                                                                                                                                      |
| [\<%] [Html.MobSyncfusion().Tab([\"tabModel\"])] |
|                                                                                                                                                                      |
| [          .AutoFormat([MobSkins].BlueLight)]                                                            |
|                                                                                                                                                                      |
| [              .BindDataSource(Model, (item, data) =\>]                                                                          |
|                                                                                                                                                                      |
| [              {]                                                                                                                |
|                                                                                                                                                                      |
| [                  item.Text = data.Text;]                                                                                       |
|                                                                                                                                                                      |
| [                  item.NavigateUrl = data.NavigateUrl;]                                                                         |
|                                                                                                                                                                      |
| [              })]                                                                                                               |
|                                                                                                                                                                      |
| [      .Render();]                                                                                                               |
|                                                                                                                                                                      |
| [    [%\>]]                                                                                          |
|                                                                                                                                                                      |
| []                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                            |
|                                                                                                                                                                       |
| **[\[Razor\]]**                                                                                                                   |
|                                                                                                                                                                       |
| []                                                                                                            |
|                                                                                                                                                                       |
| [\@{] [ Html.MobSyncfusion().Tab([\"tabModel\"])] |
|                                                                                                                                                                       |
| [          .TabStyle([TabStyle].Closed)]                                                                  |
|                                                                                                                                                                       |
| [              **.BindDataSource(Model, (item, data) =\>**]                                                                       |
|                                                                                                                                                                       |
| **[              {]**                                                                                                             |
|                                                                                                                                                                       |
| **[                  item.Text = data.Text;]**                                                                                    |
|                                                                                                                                                                       |
| **[                  item.NavigateUrl = data.ImageUrl;]**                                                                         |
|                                                                                                                                                                       |
| **[              })]**                                                                                                            |
|                                                                                                                                                                       |
| [      .Render();]                                                                                                                |
|                                                                                                                                                                       |
| [    [}]]                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application in emulator.

 

[] 

[ {border="0"} ]

Figure 158: Tab -- Dtabinding

[] 

[] 

[]{#related-topics}

