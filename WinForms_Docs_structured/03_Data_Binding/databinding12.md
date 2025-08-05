---
title: databinding12.md
original_path: WinForms_Docs/03_Data_Binding/databinding12.md
created_at: 2025-08-05
---






#### Data Binding {#data-binding style="tab-stops: 0pt"}

The Menu provides extensive data binding support to populate Menu items so that the columns of a table can be mapped to the Menu properties, namely Id, ParentId, Text, ImageUrl, SpriteCss, ImageAttributes, and HtmlAttributes.

**[]** 

Use Case Scenarios

The Data Binding feature helps users to plug-in data from a DataTable or DataSet to the Menu.

**[]** 

Adding Data Binding to an Application

Data Binding in the Menu can be customized by using two ways, namely:

[·      ]MenuBuilder

[·      ]MenuModel

**[]** 

Using MenuBuilder

To customize Data Binding in the Menu by using MenuBuilder:

1.   In the **Controller**, pass the data to the **View** page.

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| [                ]**[\[Controller\]]**                        |
|                                                                                                                                                |
| [public][ [ActionResult] Index()] |
|                                                                                                                                                |
| [        {]                                                                                                |
|                                                                                                                                                |
| [            [Northwind] data = SqlCE;]                                            |
|                                                                                                                                                |
| [            [// Passing the data to the View.]]                                     |
|                                                                                                                                                |
| [            [return] View(data.MenuData);]                                           |
|                                                                                                                                                |
| [  }   ]                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[2.   Create a ][Strongly Typed View]{.UGHyperlink}[. ]

[3.   In the **View**, invoke the **Menu** helper with the control ID.]

[4.   Set the **DataSource** and **BindTo** methods.]

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [\<%][=][Html.Syncfusion().Menu([\"myMenu\"])] |
|                                                                                                                                                                                                                     |
| [.**DataSource(Model)**]                                                                                                                                                        |
|                                                                                                                                                                                                                     |
| **[.BindTo(bind=\>]**                                                                                                                                                           |
|                                                                                                                                                                                                                     |
| **[bind.Text([\"Title\"])]**                                                                                                                            |
|                                                                                                                                                                                                                     |
| **[    .Id([\"MenuId\"])]**                                                                                                                             |
|                                                                                                                                                                                                                     |
| **[    .ParentId([\"ParentId\"])]**                                                                                                                     |
|                                                                                                                                                                                                                     |
| **[    .SpriteCss([\"SpriteClass\"])]**                                                                                                                 |
|                                                                                                                                                                                                                     |
| **[    .ImageUrl([\"ImagePath\"])]**                                                                                                                    |
|                                                                                                                                                                                                                     |
| **[    .ImageAttributes([\"Imageattributes\"])]**[)[%\>]]                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                       |
|                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [\@{][ ][Html.Syncfusion().Menu([\"myMenu\"])] |
|                                                                                                                                                                                                                     |
| [.**DataSource(Model)**]                                                                                                                                                        |
|                                                                                                                                                                                                                     |
| **[.BindTo(bind=\>]**                                                                                                                                                           |
|                                                                                                                                                                                                                     |
| **[bind.Text([\"Title\"])]**                                                                                                                            |
|                                                                                                                                                                                                                     |
| **[    .Id([\"MenuId\"])]**                                                                                                                             |
|                                                                                                                                                                                                                     |
| **[    .ParentId([\"ParentId\"])]**                                                                                                                     |
|                                                                                                                                                                                                                     |
| **[    .SpriteCss([\"SpriteClass\"])]**                                                                                                                 |
|                                                                                                                                                                                                                     |
| **[    .ImageUrl([\"ImagePath\"])]**                                                                                                                    |
|                                                                                                                                                                                                                     |
| **[    .ImageAttributes([\"Imageattributes\"])]**[)]                                                                |
|                                                                                                                                                                                                                     |
| [    .Render();][]                                                                                                                          |
|                                                                                                                                                                                                                     |
| [}][]                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the application.

 

{border="0"}

Figure 151: Menu - Data Binding Using MenuBuilder

 

 

Using MenuModel

To customize Data Binding in the Menu by using MenuModel:

[·      ]In the **Controller**, create an object for the **MenuModel** class.

[·      ]Set the **DataSource** and **BindTo** properties.

[·      ]Pass the **MenuModel** class to the **ViewData**.

 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [      **\[Controller\]**]                                                                                                        |
|                                                                                                                                                                       |
| [public][ [ActionResult] Index()]                        |
|                                                                                                                                                                       |
| [        {]                                                                                                                       |
|                                                                                                                                                                       |
| [            [Northwind] context = SqlCE;]                                                                |
|                                                                                                                                                                       |
| [            [MenuFields] menuFields = [new] [MenuFields]()] |
|                                                                                                                                                                       |
| [            {]                                                                                                                   |
|                                                                                                                                                                       |
| [                Id = [\"Id\"],]                                                                          |
|                                                                                                                                                                       |
| [                ParentId = [\"ParentId\"],]                                                              |
|                                                                                                                                                                       |
| [                Text = [\"Text\"],]                                                                      |
|                                                                                                                                                                       |
| [                ImageUrl = [\"ImageUrl\"],]                                                              |
|                                                                                                                                                                       |
| [                SpriteCSS = [\"SpriteCSS\"]]                                                             |
|                                                                                                                                                                       |
| [            };]                                                                                                                  |
|                                                                                                                                                                       |
| [            [MenuModel] menuModel = [new] [MenuModel]()]    |
|                                                                                                                                                                       |
| [            {]                                                                                                                   |
|                                                                                                                                                                       |
| [                DataSource = context.MenuData.ToList(),]                                                                         |
|                                                                                                                                                                       |
| [                BindTo = menuFields,]                                                                                            |
|                                                                                                                                                                       |
| [            };]                                                                                                                  |
|                                                                                                                                                                       |
| [            ViewData\[[\"myMenuModel\"]\] = menuModel;]                                                  |
|                                                                                                                                                                       |
| [            [return] View();]                                                                               |
|                                                                                                                                                                       |
| [  }   ]                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

[1.    ]In the **View**, invoke the **Menu** helper with the control ID.

[2.    ]From the **ViewData**, assign the **MenuModel** class to the **Menu** helper.

 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View][\[ASPX\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<%][=]Html][.Syncfusion()][.Menu([\"myMenu\"], ([MenuModel])ViewData\[[\"myMenuModel\"]\])[%\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        [\@{][ ]Html][.Syncfusion()][.Menu([\"myMenu\"], ([MenuModel])ViewData\[[\"myMenuModel\"]\]).Render();[}]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

[3.    ]Build and run the application.

 

{border="0"}

Figure 152: Menu - Data Binding Using MenuModel

 

Properties

The properties of the Data Binding feature in the Menu are described in the following tabulation:

 

  ----------------- --------------------------------------------------------------------------------------- ------------- ------------- -----------------
  Name              Description                                                                             Type          Data Type     Reference links
  DataSource        Gets or sets the data source, which is used to populate the Menu with the Menu items.   Server-side   IEnumerable   Not applicable
  BindTo            Maps the Menu fields to their respective columns from the data source.                  Server-side   MenuFields    Not applicable
  Id                Gets or sets the ID column name.                                                        Server-side   string        Not applicable
  ParentId          Gets or sets the parent ID column name.                                                 Server-side   string        Not applicable
  Text              Gets or sets the text column name.                                                      Server-side   string        Not applicable
  SpriteCss         Gets or sets the sprite column name.                                                    Server-side   string        Not applicable
  ImageUrl          Gets or sets the image path column name.                                                Server-side   string        Not applicable
  HtmlAttributes    Gets or sets the HTML attributes column name.                                           Server-side   string        Not applicable
  ImageAttributes   Gets or sets the image attributes column name.                                          Server-side   string        Not applicable
  ----------------- --------------------------------------------------------------------------------------- ------------- ------------- -----------------

[] 

Sample Link

To view a sample:

1.   Open the **Tools** Sample Browser from the dashboard. (Refer to the Samples and Location chapter.)

2.   Navigate to **Tools.Mvc** -\> **Menu** -\> **Data Binding Demo**.

[] 

[]{#related-topics}

