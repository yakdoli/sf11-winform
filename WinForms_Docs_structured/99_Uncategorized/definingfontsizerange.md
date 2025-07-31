---
title: definingfontsizerange.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\definingfontsizerange.md
created_at: 2025-07-03
---






#### Defining Font-Size Range {#defining-font-size-range style="tab-stops: 0pt"}

The tag cloud control allows you to customize the range of font sizes used to vary the appearance of the tags.

Properties

 

  ----------------- --------------------------------------------------------- ------------------ ------------------ ------------
  Name              Description                                               Type of property   Value it accepts   Dependency
  MinimumFontSize   Sets the text to be displayed on the header               int                int.MaxValue       NA
  MaximumFontSize   Sets the url of the image to be displayed on the header   int                int.MaxValue       NA
  ----------------- --------------------------------------------------------- ------------------ ------------------ ------------

[] 

Using Builder

 

The following steps explain how to define the font-size range of the tag cloud control through the builder.

1.   In the controller, pass the model to the view.

[] 

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
| []                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

2.   Create a [strongly typed view]{.UGHyperlink}. In the view, create a list of tag items and invoke the tag cloud helper with the control ID as the first argument followed by the **TagItems**, **MinimumFontSize**, and **MaximumFontSize** methods with the desired options as arguments.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                   |
| [\<%][List][\<[TagItems]\> tagItems = [new] [List]\<[TagItems]\>();] |
|                                                                                                                                                                                                                                                                                                                   |
| [            [foreach] ([var] item [in] Model.OrderBy(p =\> p.Title))]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                   |
| [            {]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
| [          tagItems.Add([new] [TagItems] { ]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                   |
| [TagName = item.Title, ]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                   |
| [Frequency = ([int])item.Rank, ]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                   |
| [NavigatetUrl = item.Website });]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                   |
| [            } [%\>]]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                   |
| [      [\<%][=]Html.Syncfusion().TagCloud([\"myTagCloud\"])]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                   |
| [.TagItems(tagItems)]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                   |
| [.Title([\"Top Blog Sites\"])]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
| [.TitleImageUrl(Url.Content([\"\~/Content/Blog.png\"]))]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                   |
| [.**MinimumFontSize(14)**]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                   |
| **[.MaximumFontSize(28)]**[%\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                          |
| [\@{][List][\<[TagItems]\> tagItems = [new] [List]\<[TagItems]\>();] |
|                                                                                                                                                                                                                                                                                                                                                          |
| [   foreach][ ([var] item [in] Model.OrderBy(p =\> p.Title))]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                          |
| [      {]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                          |
| [          tagItems.Add([new] [TagItems] { ]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                          |
| [TagName = item.Title, ]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                          |
| [Frequency = ([int])item.Rank, ]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                          |
| [NavigatetUrl = item.Website });]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                          |
| [      }][ [}]]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                          |
| [      []]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                          |
| [      [\@{] Html.Syncfusion().TagCloud([\"myTagCloud\"])]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                          |
| [.TagItems(tagItems)]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                          |
| [.Title([\"Top Blog Sites\"])]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                          |
| [.TitleImageUrl(Url.Content([\"\~/Content/Blog.png\"]))]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                          |
| [.**MinimumFontSize(14)**]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                          |
| **[.MaximumFontSize(28)]**[.Render();][}]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   Build and run the application.

 

Using Properties Model

The following steps explain how to define the font-size range of the tag cloud control through the properties model.

1.   In the controller, create an instance of TagCloudModel and define the TagItems, MinimumFontSize, and MaximumFontSize properties.**

2.   Pass the instance through the view-specific data to the view.**

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                       |
|                                                                                                                                                                                |
| [public][ [ActionResult] Index()]                                 |
|                                                                                                                                                                                |
| [        {]                                                                                                                                |
|                                                                                                                                                                                |
| [            [Northwind] data = SqlCE;]                                                                            |
|                                                                                                                                                                                |
| [            [//Create an instance of TagCloudModel.]]                                                               |
|                                                                                                                                                                                |
| [            [TagCloudModel] myModel = [new] [TagCloudModel]();]      |
|                                                                                                                                                                                |
| [            myModel.Title = [\"Top Tech Sites\"];]                                                                |
|                                                                                                                                                                                |
| [            myModel.TitleImageUrl = Url.Content([\"\~/Content/Blog.png\"]);]                                      |
|                                                                                                                                                                                |
| [            **myModel.MinimumFontSize = 14;**]                                                                                            |
|                                                                                                                                                                                |
| **[            myModel.MaximumFontSize = 28;        ]**                                                                                    |
|                                                                                                                                                                                |
| [                        ]                                                                                                                 |
|                                                                                                                                                                                |
| [//Create a list of tag items.]                                                                                              |
|                                                                                                                                                                                |
| [            [foreach] ([var] item [in] data.Blogs.OrderBy(p =\> p.Title))] |
|                                                                                                                                                                                |
| [            {]                                                                                                                            |
|                                                                                                                                                                                |
| [                myModel.TagItems.Add([new] [TagItems] { ]                                    |
|                                                                                                                                                                                |
| [TagName = item.Title, ]                                                                                                                   |
|                                                                                                                                                                                |
| [Frequency = ([int])item.Rank, ]                                                                                      |
|                                                                                                                                                                                |
| [NavigatetUrl = item.Website });]                                                                                                          |
|                                                                                                                                                                                |
| [            }]                                                                                                                            |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [            [//Pass the instance to the view through the view data.]]                                               |
|                                                                                                                                                                                |
| [            ViewData\[[\"myTagCloud\"]\] = myModel;]                                                              |
|                                                                                                                                                                                |
| [            [return] View();]                                                                                        |
|                                                                                                                                                                                |
| [   }  ]                                                                                                                                   |
|                                                                                                                                                                                |
| []                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

3.   In **View**, invoke the tag cloud helper with the view data key as the control ID.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [\<%][=][Html.Syncfusion().TagCloud([\"myTagCloud\"])[%\>]] |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| [\@{][ Html.Syncfusion().TagCloud([\"myTagCloud\"]).Render();[}]] |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

The following figure shows the output of the tag cloud control.

[] 

{border="0"}

Figure 275: Tag Cloud with Set Font-Sizes

*[]* 

[]{#related-topics}

