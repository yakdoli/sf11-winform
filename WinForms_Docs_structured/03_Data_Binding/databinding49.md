---
title: databinding49.md
original_path: WinForms_Docs/03_Data_Binding/databinding49.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Data Binding {#data-binding style="tab-stops: 0pt"}

The Toolbar provides extensive data binding support to populate Toolbar items so that the columns of a table can be mapped to the Toolbar properties, namely Text, ImageUrl, ImageAttributes, and HtmlAttributes.

The Data Binding feature helps users to plug-in data from a Database to the Toolbar.

 

Properties

The properties of the Data Binding feature in the Toolbar are described in the following tabulation:

 

  ---------------- --------------------------------------------------------------------------------------------- ------------- ---------------- -----------------
  Name             Description                                                                                   Type          Data Type        Reference links
  BindDataSource   Gets or sets the data source, which is used to populate the Toolbar with the Toolbar items.   Server-side   Action Builder   Not applicable
  ---------------- --------------------------------------------------------------------------------------------- ------------- ---------------- -----------------

 

Adding Data Binding to an Application

To customize Data Binding in the Toolbar:

1.   In the **Controller**, pass the data to the **View** page.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [      **\[Controller\]**]                                                                                                              |
|                                                                                                                                                                             |
| [        [public][ActionResult] Databinding()]                                             |
|                                                                                                                                                                             |
| [        {]                                                                                                                             |
|                                                                                                                                                                             |
| [            [DBModel] model = [new][DBModel]();]                  |
|                                                                                                                                                                             |
| [            model.BindDataList = [new][List]\<[BindItemData]\>()] |
|                                                                                                                                                                             |
| [            {]                                                                                                                         |
|                                                                                                                                                                             |
| [                [new][BindItemData](){ Text=[\"Clock\"] },]       |
|                                                                                                                                                                             |
| [                [new][BindItemData](){ Text=[\"Calendar\"] },]    |
|                                                                                                                                                                             |
| [                [new][BindItemData](){ Text=[\"Memo\"] },]        |
|                                                                                                                                                                             |
| [                [new][BindItemData](){ Text=[\"Music\"] },]       |
|                                                                                                                                                                             |
| [                [new][BindItemData](){ Text=[\"Camera\"] },]      |
|                                                                                                                                                                             |
| [                [new][BindItemData](){ Text=[\"Gallery\"] },]     |
|                                                                                                                                                                             |
| [                [new][BindItemData](){ Text=[\"FM radio\"] }]     |
|                                                                                                                                                                             |
| [            };]                                                                                                                        |
|                                                                                                                                                                             |
| [            ViewData\[[\"DataModel\"]\] = model.BindDataList;]                                                 |
|                                                                                                                                                                             |
| [            [return] View();]                                                                                     |
|                                                                                                                                                                             |
| [        }]                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[2.   Create a ] [Strongly Typed View]{.UGHyperlink} [. ]

[3.   In the **View**, invoke the **Toolbar** helper with the control ID.]

[4.   Set the data source and mapping fields in **BindDataSource** method.]

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                         |
| [\<%] [=] [Html.MobSyncfusion().Toolbar([\"DataBindToolbar\"])]                    |
|                                                                                                                                                                                                                                                         |
| [   .Width(430)]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                         |
| [   .AutoFormat([MobSkins].DarkNight)]                                                                                                                                                      |
|                                                                                                                                                                                                                                                         |
| [   .ShowAnimation([MobAnimations].Slide)]                                                                                                                                                  |
|                                                                                                                                                                                                                                                         |
| [.BindDataSource\<[BindItemData]\>(([IEnumerable]\<[BindItemData]\>) ViewData\[[\"DataModel\"]\], (item, data) =\>] |
|                                                                                                                                                                                                                                                         |
| [      {]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                         |
| [        item.Text = data.Text;]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                         |
| [      })[%\>]]                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [ [\@{]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [   Html.MobSyncfusion().Toolbar([\"DataBindToolbar\"])]                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [   .AutoFormat([MobSkins].DarkNight)]                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [   .ShowAnimation([MobAnimations].Slide)]                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [   .BindDataSource\<[BindItemData]\>(([IEnumerable]\<[BindItemData]\>) ViewData\[[\"DataModel\"]\], (item, data) =\>] |
|                                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [      item.Text = data.Text;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [    })]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [   .Render();[}]] []                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   Build and run the application.

 

{border="0"}

 

Figure 174: Toolbar - Data Binding

 

[]{#related-topics}

