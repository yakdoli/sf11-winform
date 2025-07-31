---
title: databinding47.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databinding47.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Data Binding {#data-binding style="tab-stops: 0pt"}

The Menu provides extensive data binding support to populate Menu items so that the columns of a table can be mapped to the Menu properties, namely Text, ImageUrl, ImageAttributes, and HtmlAttributes.

This feature helps users to plug-in data from a Database to the Menu.

 

Properties

The properties of the Data Binding feature in the Menu are described in the following tabulation:

 

  ---------------- --------------------------------------------------------------------------------------- ------------- ---------------- -----------------
  Name             Description                                                                             Type          Data Type        Reference links
  BindDataSource   Gets or sets the data source, which is used to populate the Menu with the Menu items.   Server-side   Action Builder   Not applicable
  ---------------- --------------------------------------------------------------------------------------- ------------- ---------------- -----------------

 

Adding Data Binding to an Application

To customize Data Binding in the Menu:

1.   In the **Controller**, pass the data to the **View** page.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [      **\[Controller\]**]                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        [public][ActionResult] Databinding()]                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            [DBModel] model = [new][DBModel]();]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            model.BindDataList = [new][List]\<[BindItemData]\>()]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"Wireless and Networks\"], ImageUrl=[\"\~/Content/Menu/Images/Wireless.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] } , Children=[new][List]\<[SubBindData]\>()] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                { ]                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    [new][SubBindData](){ Text=[\"Flight mode\"] } ,]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    [new][SubBindData](){ Text=[\"Wi-Fi settings\"]  }, ]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    [new][SubBindData](){ Text=[\"Bluetooth settings\"] },]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    [new][SubBindData](){ Text=[\"Mobile networks\"]  } ]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                } },]                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"Call Settings\"], ImageUrl=[\"\~/Content/Menu/Images/settings.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] }, Children=[new][List]\<[SubBindData]\>()]          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                { ]                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    [new][SubBindData](){ Text=[\"Voicemail\"] } ,]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    [new][SubBindData](){ Text=[\"Other call settings\"] } ]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                } },]                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"Sound\"], ImageUrl=[\"\~/Content/Menu/Images/Sound.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] } },]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"Application\"], ImageUrl=[\"\~/Content/Menu/Images/Application.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] }, Children=[new][List]\<[SubBindData]\>()]         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                { ]                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    [new][SubBindData](){ Text=[\"Unknown sources\"] },]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    [new][SubBindData](){ Text=[\"Manage applications\"] },]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    [new][SubBindData](){ Text=[\"Running services\"] },]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    [new][SubBindData](){ Text=[\"Development\"] }]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                } },]                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"SD Card and phone storage\"], ImageUrl=[\"\~/Content/Menu/Images/storage.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] } },]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"Search\"], ImageUrl=[\"\~/Content/Menu/Images/search.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] } },]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"Security\"], ImageUrl=[\"\~/Content/Menu/Images/security.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] } },]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"Inbox\"], ImageUrl=[\"\~/Content/Menu/Images/inbox.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] } },]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"Calendar\"], ImageUrl=[\"\~/Content/Menu/Images/calendar.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] } },]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"Battery\"], ImageUrl=[\"\~/Content/Menu/Images/battery.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] } },]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"Phone\"], ImageUrl=[\"\~/Content/Menu/Images/phone.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] } },]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                [new][BindItemData](){ Text=[\"Help\"], ImageUrl=[\"\~/Content/Menu/Images/help.png\"], ImageAttributes=[new] { \@class=[\"menu-img\"] } },]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            [return] View(model.BindDataList);]                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

[2.   Create a ] [Strongly Typed View]{.UGHyperlink} [. ]

[3.   In the **View**, invoke the **Menu** helper with the control ID.]

[4.   Set the data source and mapping fields in **BindDataSource** method.]

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                      |
|                                                                                                                                                                         |
| [   [\<%][=]Html.MobSyncfusion().Menu([\"DatabindMenu\"])] |
|                                                                                                                                                                         |
| [              .BindDataSource(Model, map =\>]                                                                                      |
|                                                                                                                                                                         |
| [               {]                                                                                                                  |
|                                                                                                                                                                         |
| [                   map.MapTo\<[BindItemData]\>(binding =\>]                                                |
|                                                                                                                                                                         |
| [                   {]                                                                                                              |
|                                                                                                                                                                         |
| [                       binding.ItemDataBound((item, nd) =\>]                                                                       |
|                                                                                                                                                                         |
| [                       {]                                                                                                          |
|                                                                                                                                                                         |
| [                           item.Text = nd.Text;]                                                                                   |
|                                                                                                                                                                         |
| [                           item.ImageUrl = nd.ImageUrl;]                                                                           |
|                                                                                                                                                                         |
| [                           item.ImageAttributes = nd.ImageAttributes;]                                                             |
|                                                                                                                                                                         |
| [                       })]                                                                                                         |
|                                                                                                                                                                         |
| [                      .Children(nd =\> nd.Children);]                                                                              |
|                                                                                                                                                                         |
| [                   });]                                                                                                            |
|                                                                                                                                                                         |
| [                   map.MapTo\<[SubBindData]\>(binding =\>]                                                 |
|                                                                                                                                                                         |
| [                   {]                                                                                                              |
|                                                                                                                                                                         |
| [                       binding.ItemDataBound((item, snd) =\>]                                                                      |
|                                                                                                                                                                         |
| [                       {]                                                                                                          |
|                                                                                                                                                                         |
| [                           item.Text = snd.Text;]                                                                                  |
|                                                                                                                                                                         |
| [                           item.ImageUrl = snd.ImageUrl;]                                                                          |
|                                                                                                                                                                         |
| [                           item.ImageAttributes = snd.ImageAttributes;]                                                            |
|                                                                                                                                                                         |
| [                       });]                                                                                                        |
|                                                                                                                                                                         |
| [                   });]                                                                                                            |
|                                                                                                                                                                         |
| [               })[%\>]]                                                                                |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| []                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                        |
|                                                                                                                                                                            |
| [\@{] [ Html.MobSyncfusion().Menu([\"DatabindMenu\"])] |
|                                                                                                                                                                            |
| [             .BindDataSource(Model, map =\>]                                                                                          |
|                                                                                                                                                                            |
| [             {]                                                                                                                       |
|                                                                                                                                                                            |
| [                 map.MapTo\<[BindItemData]\>(binding =\>]                                                     |
|                                                                                                                                                                            |
| [                 {]                                                                                                                   |
|                                                                                                                                                                            |
| [                     binding.ItemDataBound((item, nd) =\>]                                                                            |
|                                                                                                                                                                            |
| [                     {]                                                                                                               |
|                                                                                                                                                                            |
| [                         item.Text = nd.Text;]                                                                                        |
|                                                                                                                                                                            |
| [                         item.ImageUrl = nd.ImageUrl;]                                                                                |
|                                                                                                                                                                            |
| [                         item.ImageAttributes = nd.ImageAttributes;]                                                                  |
|                                                                                                                                                                            |
| [                     })]                                                                                                              |
|                                                                                                                                                                            |
| [                    .Children(nd =\> nd.Children);]                                                                                   |
|                                                                                                                                                                            |
| [                 });]                                                                                                                 |
|                                                                                                                                                                            |
| [                 map.MapTo\<[SubBindData]\>(binding =\>]                                                      |
|                                                                                                                                                                            |
| [                 {]                                                                                                                   |
|                                                                                                                                                                            |
| [                     binding.ItemDataBound((item, snd) =\>]                                                                           |
|                                                                                                                                                                            |
| [                     {]                                                                                                               |
|                                                                                                                                                                            |
| [                         item.Text = snd.Text;]                                                                                       |
|                                                                                                                                                                            |
| [                         item.ImageUrl = snd.ImageUrl;]                                                                               |
|                                                                                                                                                                            |
| [                         item.ImageAttributes = snd.ImageAttributes;]                                                                 |
|                                                                                                                                                                            |
| [                     });]                                                                                                             |
|                                                                                                                                                                            |
| [                 });]                                                                                                                 |
|                                                                                                                                                                            |
| [             })]                                                                                                                      |
|                                                                                                                                                                            |
| [            .Render(); [}]]                                                                               |
|                                                                                                                                                                            |
| []                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   Build and run the application.

 

{border="0"}

 

Figure 76: Menu - Data Binding Using MenuBuilder

 

[] 

[]{#related-topics}

