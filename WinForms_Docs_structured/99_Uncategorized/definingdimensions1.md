---
title: definingdimensions1.md
original_path: WinForms_Docs/99_Uncategorized/definingdimensions1.md
created_at: 2025-08-05
---






#### Defining Dimensions {#defining-dimensions style="tab-stops: 0pt"}

The tag cloud control's height and width dimensions can be customized. 

**[]** 

**[Properties]**

**[]** 

 

  -------- --------------------------------------------- ------------------ ------------------ ------------
  Name     Description                                   Type of property   Value it accepts   Dependency
  Height   Sets the height of the tag cloud in pixels.   struct             Members of Unit    NA
  Width    Sets the width of the tag cloud in pixels.    struct             Members of Unit    NA
  -------- --------------------------------------------- ------------------ ------------------ ------------

 

*[[]]{.underline}* 

Using Builder

The following steps explain how to set the dimensions of tag cloud through the builder.

 

1.   In the controller, pass the model to the view.

[] 

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

3.   In **View**, create a list of tag items and invoke the tag cloud helper with the control ID as the first argument followed by the **TagItems**, **Width**, and **Height** methods with the desired options as arguments.[]

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
| [.**Width(500)**]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                   |
| **[.Height(201)]**[%\>]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                          |
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
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                          |
| [      [\@{] Html.Syncfusion().TagCloud([\"myTagCloud\"])]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                          |
| [.TagItems(tagItems)]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                          |
| [.Title([\"Top Blog Sites\"])]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                          |
| [.**Width(500)**]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                          |
| **[.Height(201)]**[.Render();][}]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application.**

*[[]]{.underline}* 

Using Properties Model

The following steps explain how to set the dimensions of the tag cloud control through the properties model.

1.   In the controller, create an instance of **TagCloudModel** and define the **TagItems**, **Width**, and **Height** properties.**

2.   Pass the instance through the view-specific data to the view.**

*[[]]{.underline}* 

*[[[]]]{.underline}* 

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
| [            **myModel.Width = 500;**]                                                                                                     |
|                                                                                                                                                                                |
| **[            myModel.Height = 201;]**                                                                                                    |
|                                                                                                                                                                                |
| [            ]                                                                                                                             |
|                                                                                                                                                                                |
| [            [//Create a list of tag items.]]                                                                        |
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
| **[]**                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

3.   In View, invoke the tag cloud helper with the view data key as the control ID.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [\<%][=][Html.Syncfusion().TagCloud([\"myTagCloud\"])[%\>]] |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| [\@{][ Html.Syncfusion().TagCloud([\"myTagCloud\"]).Render();[}]] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

4.   Build and run the application.

The following figure shows the output of the tag cloud with customized dimensions.

 

{border="0"}

Figure 273: Tag Cloud with Customized Dimensions

*[]* 

[]{#related-topics}

