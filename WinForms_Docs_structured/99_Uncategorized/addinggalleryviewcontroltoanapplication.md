---
title: addinggalleryviewcontroltoanapplication.md
original_path: WinForms_Docs/99_Uncategorized/addinggalleryviewcontroltoanapplication.md
created_at: 2025-08-05
---








  









### Adding Gallery View Control to an Application {#adding-gallery-view-control-to-an-application style="tab-stops: 0pt"}

The GalleryView vontrol can be created in the following two ways:

 

Using Builder

5.   In the **View**, invoke the **GalleryView** helper with the control ID as an argument.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                               |
| [            [\<%][=]Html.Syncfusion().GalleryView(\"galleryview1\").AutoFormat((Skins)ViewData\[\"CurrentTheme\"\]).Items(item =\>]     |
|                                                                                                                                                                                                                               |
| [                                    {]                                                                                                                                                   |
|                                                                                                                                                                                                                               |
| [                                        item.Add().ImageUrl(Url.Content(\"\~/Content/images/GalleryView/Heading1.png\"));]                                                               |
|                                                                                                                                                                                                                               |
| [                                        item.Add().ImageUrl(Url.Content(\"\~/Content/images/GalleryView/Heading2.png\"));]                                                               |
|                                                                                                                                                                                                                               |
| [                                        item.Add().ImageUrl(Url.Content(\"\~/Content/images/GalleryView/Heading3.png\"));]                                                               |
|                                                                                                                                                                                                                               |
| [                                        item.Add().ImageUrl(Url.Content(\"\~/Content/images/GalleryView/Intense.png\"));]                                                                |
|                                                                                                                                                                                                                               |
| [                                        item.Add().ImageUrl(Url.Content(\"\~/Content/images/GalleryView/Heading1.png\"));]                                                               |
|                                                                                                                                                                                                                               |
| [                                        item.Add().ImageUrl(Url.Content(\"\~/Content/images/GalleryView/Heading2.png\"));]                                                               |
|                                                                                                                                                                                                                               |
| [                                        item.Add().ImageUrl(Url.Content(\"\~/Content/images/GalleryView/Heading3.png\"));]                                                               |
|                                                                                                                                                                                                                               |
| [                                        item.Add().ImageUrl(Url.Content(\"\~/Content/images/GalleryView/Intense.png\"));]                                                                |
|                                                                                                                                                                                                                               |
| [        ]                                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| [                                    }).ExtraItem(extraItem =\>]                                                                                                                          |
|                                                                                                                                                                                                                               |
| [                                        {]                                                                                                                                               |
|                                                                                                                                                                                                                               |
| [                                            extraItem.Add().Text(\"ExtraItem1\").ImageUrl(Url.Content(\"\~/Content/images/GalleryView/FontColor16.png\"));;]                             |
|                                                                                                                                                                                                                               |
| [                                            extraItem.Add().Text(\"ExtraItem2\").ImageUrl(Url.Content(\"\~/Content/images/GalleryView/Sort16.png\")); [%\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [      ][\@{][Html.Syncfusion().GalleryView([\"galleryview1\"]).AutoFormat(([Skins])ViewData\[[\"CurrentTheme\"]\]).Items(item =\>] |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                    {]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        item.Add().ImageUrl(Url.Content([\"\~/Content/images/GalleryView/Heading1.png\"]));]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        item.Add().ImageUrl(Url.Content([\"\~/Content/images/GalleryView/Heading2.png\"]));]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        item.Add().ImageUrl(Url.Content([\"\~/Content/images/GalleryView/Heading3.png\"]));]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        item.Add().ImageUrl(Url.Content([\"\~/Content/images/GalleryView/Intense.png\"]));]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        item.Add().ImageUrl(Url.Content([\"\~/Content/images/GalleryView/Heading1.png\"]));]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        item.Add().ImageUrl(Url.Content([\"\~/Content/images/GalleryView/Heading2.png\"]));]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        item.Add().ImageUrl(Url.Content([\"\~/Content/images/GalleryView/Heading3.png\"]));]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        item.Add().ImageUrl(Url.Content([\"\~/Content/images/GalleryView/Intense.png\"]));]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [        ]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                    }).ExtraItem(extraItem =\>]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        {]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                           extraItem.Add().Text([\"ExtraItem1\"]).ImageUrl(Url.Content([\"\~/Content/images/GalleryView/FontColor16.png\"]));]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                            extraItem.Add().Text([\"ExtraItem2\"]).ImageUrl(Url.Content([\"\~/Content/images/GalleryView/Sort16.png\"]));]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        })]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        ]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [                                        .ItemToShow(5)]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [}][   ]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Using Model

1.  In the **view**, invoke the **GalleryView** helper with the control ID as an argument.**[]**

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                        |
| [  ]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                        |
| [\<%][=][Html.Syncfusion().GalleryView([\"gallery1\"],([GalleryViewModel])Model)[%\>]] |
|                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                  |
| [  ]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                  |
| [@][Html.Syncfusion().GalleryView([\"gallery1\"],([GalleryViewModel])Model[)]] |
|                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

2.   In the controller, create an instance of **GalleryViewModel**.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [public][ ActionResult ThroughModel(][GalleryViewModel]          |
|                                                                                                                                                                                                                                                  |
| [model)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                  |
| [        {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                  |
| [             model.AutoFormat = [Skins].Almond;]                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [            [GalleryViewItem] item = [new] [GalleryViewItem]();]                                                          |
|                                                                                                                                                                                                                                                  |
| [            item.ImageUrl = Url.Content([\"\~/Content/images/GalleryView/Heading1.png\"]);]                                                                            |
|                                                                                                                                                                                                                                                  |
| [            [GalleryViewItem] item2 = [new] [GalleryViewItem]();]                                                         |
|                                                                                                                                                                                                                                                  |
| [            item2.ImageUrl = Url.Content([\"\~/Content/images/GalleryView/Heading2.png\"]);]                                                                           |
|                                                                                                                                                                                                                                                  |
| [            [GalleryViewItem] item3 = [new] [GalleryViewItem]();]                                                         |
|                                                                                                                                                                                                                                                  |
| [            item3.ImageUrl = Url.Content([\"\~/Content/images/GalleryView/Heading3.png\"]);]                                                                           |
|                                                                                                                                                                                                                                                  |
| [            [GalleryViewItem] item4 = [new] [GalleryViewItem]();]                                                         |
|                                                                                                                                                                                                                                                  |
| [            item4.ImageUrl = Url.Content([\"\~/Content/images/GalleryView/Intense.png\"]);]                                                                            |
|                                                                                                                                                                                                                                                  |
| [            [GalleryViewItem] item5 = [new] [GalleryViewItem]();]                                                         |
|                                                                                                                                                                                                                                                  |
| [            item5.ImageUrl = Url.Content([\"\~/Content/images/GalleryView/Heading1.png\"]);]                                                                           |
|                                                                                                                                                                                                                                                  |
| [            [GalleryViewItem] item6 = [new] [GalleryViewItem]();]                                                         |
|                                                                                                                                                                                                                                                  |
| [            item6.ImageUrl = Url.Content([\"\~/Content/images/GalleryView/Heading2.png\"]);]                                                                           |
|                                                                                                                                                                                                                                                  |
| [            [GalleryViewItem] item7 = [new] [GalleryViewItem]();]                                                         |
|                                                                                                                                                                                                                                                  |
| [            item7.ImageUrl = Url.Content([\"\~/Content/images/GalleryView/Heading3.png\"]);]                                                                           |
|                                                                                                                                                                                                                                                  |
| [            [GalleryViewItem] item8 = [new] [GalleryViewItem]();]                                                         |
|                                                                                                                                                                                                                                                  |
| [            item8.ImageUrl = Url.Content([\"\~/Content/images/GalleryView/Intense.png\"]);]                                                                            |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                  |
| [            [GalleryViewExtraItem] extraitem = [new] [GalleryViewExtraItem]();]                                           |
|                                                                                                                                                                                                                                                  |
| [            extraitem.Text = [\"extraitem\"];]                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [            extraitem.ImageUrl = Url.Content([\"\~/Content/images/GalleryView/FontColor16.png\"]);]                                                                    |
|                                                                                                                                                                                                                                                  |
| [            [GalleryViewExtraItem] extraitem2 = [new] [GalleryViewExtraItem]();]                                          |
|                                                                                                                                                                                                                                                  |
| [            extraitem2.Text = [\"extratiem\"];]                                                                                                                        |
|                                                                                                                                                                                                                                                  |
| [            extraitem2.ImageUrl = Url.Content([\"\~/Content/images/GalleryView/Sort16.png\"]);]                                                                        |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                  |
| [            model.Items = [new] [List]\<[GalleryViewItem]\>() { item, item2, item3, item4, item5, item6, item7, item8 };] |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                  |
| [            model.ExtraItem = [new] [List]\<[GalleryViewExtraItem]\>() { extraitem, extraitem2 };]                        |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                  |
| [            [return] View(model);]                                                                                                                                        |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.  Build and run the application

The output will be displayed as shown below.

 

{border="0"}

Figure 122: Gallery View

[]{#related-topics}

