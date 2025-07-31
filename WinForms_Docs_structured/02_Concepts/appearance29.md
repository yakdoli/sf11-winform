---
title: appearance29.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\appearance29.md
created_at: 2025-07-03
---






#### Appearance {#appearance style="tab-stops: 0pt"}

[] 

The tag cloud control provides support for fourteen predefined themes to enhance the look and feel.

**[]** 

Properties

 

+-------------+---------------------------------------+----------------------------------+--------------------------------------------------------------+-------------+
| Name        | Description                           | Type of property                 | Value it accepts                                             | Dependency  |
+-------------+---------------------------------------+----------------------------------+--------------------------------------------------------------+-------------+
| AutoFormat  | Used to define the Syncfusion themes. | [enum] | [·      ]Skins.Office2007Blue   | NA          |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Office2007Silver |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Office2007Black  |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Vista            |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Almond           |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Blueberry        |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Blend            |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Olive            |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Turquoise        |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Monochrome       |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Sandune          |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.VS2010           |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Marble           |             |
|             |                                       |                                  |                                                              |             |
|             |                                       |                                  | [·      ]Skins.Midnight         |             |
+-------------+---------------------------------------+----------------------------------+--------------------------------------------------------------+-------------+

*[[]]{.underline}* 

Using Builder

The following steps explain how to set themes of the tag cloud control through the builder.

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
| [            [//Passing the model to the view]]                                      |
|                                                                                                                                                |
| [            [return] View(data.Blogs);]                                              |
|                                                                                                                                                |
| [  } ]                                                                                                     |
|                                                                                                                                                |
| []                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   [Create a strongly typed view]{.UGHyperlink}[. ]

3.   In **View**, create a list of tag items and invoke the tag cloud helper with the control ID as the first argument followed by the **TagItems** and **AutoFormat** methods with the desired options as arguments.[]

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
| [.**AutoFormat([Skins].Vista)**][%\>]                                                                                                                                                         |
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
| [.**AutoFormat([Skins].Vista)**.Render();][}]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application.

**[]** 

**[Using Properties Model]**

The following steps explain how to set themes of the tag cloud control through the properties model.

1.   In the controller, create an instance of **TagCloudModel** and define the **TagItems** and **AutoFormat** properties.**

2.   Pass the instance through the view-specific data to the view.**

[            [return] View(data.Blogs);]

[  }   ]

3.   Create a [[strongly typed view]]{.underline}. In the view, invoke the tag cloud helper with the view data key as the control ID.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [\<%][=][Html.Syncfusion().TagCloud([\"myTagCloud\"])[%\>]] |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| [\@{][ Html.Syncfusion().TagCloud([\"myTagCloud\"]).Render();[}]] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[1.     Build and run the application.]

The figure shows the output of the tag cloud with a set theme.

{border="0"}

Figure 277: Tag Cloud with Theme

[]{#related-topics}

