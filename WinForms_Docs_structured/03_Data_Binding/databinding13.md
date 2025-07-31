---
title: databinding13.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databinding13.md
created_at: 2025-07-03
---






#### Data Binding {#data-binding style="tab-stops: 0pt"}

 

The tag cloud control provides extensive data binding support so that the columns of a table can be mapped to the properties of a tag item (TagName, Frequency, and NavigateUrl) to generate the tags.

The following steps describe defining the data source and mapping the column names.

 

1.   In the controller, pass the model to the view.

 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                       |
|                                                                                                                                                |
| [public][ [ActionResult] Index()] |
|                                                                                                                                                |
| [        {]                                                                                                |
|                                                                                                                                                |
| [            [Northwind] data = SqlCE;]                                            |
|                                                                                                                                                |
| [            [//passing the Model to the view]]                                      |
|                                                                                                                                                |
| [            [return] View(data.Blogs);]                                              |
|                                                                                                                                                |
| [  }   ]                                                                                                   |
|                                                                                                                                                |
| **[]**                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   [[Create a strongly typed view]]{.underline}[. ]

3.   In **View**, create the list of tag items and invoke the tag cloud helper with the control ID as the first argument followed by the **DataSource** and **BindTo** methods with the data source and column names for the respective tag item properties as arguments.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                             |
| [\<%][=][Html.Syncfusion().TagCloud([\"myTagCloud\"])] |
|                                                                                                                                                                                                                             |
| [.Title([\"Favourite Sites\"])]                                                                                                                                 |
|                                                                                                                                                                                                                             |
| [.TitleImageUrl(Url.Content([\"\~/Content/Blog.png\"]))        .**DataSource(Model)**]                                                                          |
|                                                                                                                                                                                                                             |
| **[.BindTo(bind=\>]**                                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| **[bind.TagName([\"Title\"])]**                                                                                                                                 |
|                                                                                                                                                                                                                             |
| **[    .Frequency([\"Rank\"])]**                                                                                                                                |
|                                                                                                                                                                                                                             |
| **[    .NavigateUrl([\"Website\"])]**[)[%\>]]                                                   |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                |
|                                                                                                                                                                                   |
| [\@{][ Html.Syncfusion().TagCloud([\"myTagCloud\"])]          |
|                                                                                                                                                                                   |
| [.Title([\"Favourite Sites\"])]                                                                                       |
|                                                                                                                                                                                   |
| [.TitleImageUrl(Url.Content([\"\~/Content/Blog.png\"]))        .**DataSource(Model)**]                                |
|                                                                                                                                                                                   |
| **[.BindTo(bind=\>]**                                                                                                                         |
|                                                                                                                                                                                   |
| **[bind.TagName([\"Title\"])]**                                                                                       |
|                                                                                                                                                                                   |
| **[    .Frequency([\"Rank\"])]**                                                                                      |
|                                                                                                                                                                                   |
| **[    .NavigateUrl([\"Website\"])]**[).Render();[}]] |
|                                                                                                                                                                                   |
| []                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application.

After performing the above steps, the tag cloud will be rendered with tag name, frequency, and URL populated from the corresponding column.

 

[]{#related-topics}

