---
title: customizingheaders.md
original_path: WinForms_Docs/99_Uncategorized/customizingheaders.md
created_at: 2025-08-05
---






#### Customizing Headers {#customizing-headers style="tab-stops: 0pt"}

The tag cloud allows you to customize headers for the control.

 

Properties

 

  ------------------ ---------------------------------------------------------- ----------- ----------------
  Name               Description                                                Arguments   Reference Link
  ClientSideOnShow   Sets the text to be displayed in the header.               string      \-
  ClientSideOnLoad   Sets the URL of the image to be displayed in the header.   string      \-
  ------------------ ---------------------------------------------------------- ----------- ----------------

*[[]]{.underline}* 

Using Builder

The following steps explain how to customize the header of a tag cloud through the builder.

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
| [            [//Passing the model to the view.]]                                     |
|                                                                                                                                                |
| [            [return] View(data.Blogs);]                                              |
|                                                                                                                                                |
| [  }   ]                                                                                                   |
|                                                                                                                                                |
| []                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   [Create a strongly typed view]{.UGHyperlink}[. ]

3.   In **View**, create a list of tag items and invoke the tag cloud helper with the control ID as the first argument followed by the **TagItems**, **Title**, and **TitleUrl** methods with the desired options as arguments.

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
| [            } [%\>]][]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().TagCloud([\"myTagCloud\"])]                                                                                       |
|                                                                                                                                                                                                                                                                                                                   |
| [.TagItems(tagItems)]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                   |
| [.Title([\"Top Blog Sites\"])]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
| [.TitleImageUrl(Url.Content([\"\~/Content/Blog.png\"]))][%\>]                                                                                                                                 |
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
| []                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                          |
| [      [\@{] Html.Syncfusion().TagCloud([\"myTagCloud\"])]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                          |
| [.TagItems(tagItems)]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                          |
| [.Title([\"Top Blog Sites\"])]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                          |
| [.TitleImageUrl(Url.Content([\"\~/Content/Blog.png\"])).Render();][}]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain how to customize the header of a tag cloud through the properties model.

1.   In the controller, create an instance of **TagCloudModel** and define the **TagItems**, **Title**, and **TitleUrl** properties.**

2.   Pass the instance through the view-specific data to the view.**

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                        |
|                                                                                                                                                                                                 |
| [public][ [ActionResult] Index()]                                                  |
|                                                                                                                                                                                                 |
| [        {]                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [            [Northwind] data = SqlCE;]                                                                                             |
|                                                                                                                                                                                                 |
| [            [//Create an instance of TagCloudModel.]]                                                                                |
|                                                                                                                                                                                                 |
| [            [TagCloudModel] myModel = [new] [TagCloudModel]();]                       |
|                                                                                                                                                                                                 |
| [            **myModel.Title = [\"Top Tech Sites\"];**]                                                                             |
|                                                                                                                                                                                                 |
| **[            myModel.TitleImageUrl = Url.Content([\"\~/Content/Blog.png\"]);]**[            ] |
|                                                                                                                                                                                                 |
| [            ]                                                                                                                                              |
|                                                                                                                                                                                                 |
| [//Create a list of tag items.]                                                                                                               |
|                                                                                                                                                                                                 |
| [            [foreach] ([var] item [in] data.Blogs.OrderBy(p =\> p.Title))]                  |
|                                                                                                                                                                                                 |
| [            {]                                                                                                                                             |
|                                                                                                                                                                                                 |
| [                myModel.TagItems.Add([new] [TagItems] { ]                                                     |
|                                                                                                                                                                                                 |
| [TagName = item.Title, ]                                                                                                                                    |
|                                                                                                                                                                                                 |
| [Frequency = ([int])item.Rank, ]                                                                                                       |
|                                                                                                                                                                                                 |
| [NavigatetUrl = item.Website });]                                                                                                                           |
|                                                                                                                                                                                                 |
| [            }]                                                                                                                                             |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [            [//Pass the instance to the view through the view data.]]                                                                |
|                                                                                                                                                                                                 |
| [            ViewData\[[\"myTagCloud\"]\] = myModel;]                                                                               |
|                                                                                                                                                                                                 |
| [            [return] View();]                                                                                                         |
|                                                                                                                                                                                                 |
| [   } ]                                                                                                                                                     |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| [\@{][ Html.Syncfusion().TagCloud([\"myTagCloud\"]).Render();[}]] |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

4.   Build and run the application.

 

The following figure shows the output of the tag cloud control with a customized header.

 

{border="0"}

[Figure]{#_Ref268773356} 274: Tag Cloud with Customized Header

 

[]{#related-topics}

