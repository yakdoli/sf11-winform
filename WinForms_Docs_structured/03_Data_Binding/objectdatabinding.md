---
title: objectdatabinding.md
original_path: WinForms_Docs/03_Data_Binding/objectdatabinding.md
created_at: 2025-08-05
---






##### Object Data Binding {#object-data-binding style="tab-stops: 0pt"}

TreeView provides extensive data binding support to populate TreeView items so that the columns of a table can be mapped to the TreeView properties, namely Id, ParentId, Text, ImageUrl, SpriteCss, ImageAttributes, and HtmlAttributes.

 

Use Case Scenarios

The Data Binding feature helps users to plug-in data from a DataTable or DataSet to TreeView.

 

Adding Data Binding[ ]to an Application

Data Binding in TreeView can be customized by using two ways, namely:

[·      ]TreeViewBuilder

[·      ]TreeViewModel

 

Using TreeViewBuilder

To customize Data Binding in TreeView by using TreeViewBuilder:

1.   In the **Controller**, pass the data to the **View** page.

 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                       |
|                                                                                                                                                |
| [public][ [ActionResult] Index()] |
|                                                                                                                                                |
| [        {]                                                                                                |
|                                                                                                                                                |
| [            [Northwind] data = SqlCE;]                                            |
|                                                                                                                                                |
| [            [// Passing the data to the View.]]                                     |
|                                                                                                                                                |
| [            [return] View(data.TreeViewData);]                                       |
|                                                                                                                                                |
| [  }   ]                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

2.   Create a Strongly Typed View.

3.   In the **View**, invoke the **TreeView** helper with the control ID.

4.   Set the **DataSource** and **BindTo** methods.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View][\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%][=][Html.Syncfusion().TreeView([\"myTreeView\"]][,[\"Databind\"]][)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [.**DataSource(Model)**]                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[.BindTo(bind=\>]**                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[bind.Text([\"Title\"])]**                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[    .Id([\"TreeViewId\"])]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[    .ParentId([\"ParentId\"])]**                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[    .SpriteCss([\"SpriteClass\"])]**                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[    .ImageUrl([\"ImagePath\"])]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[    .ImageAttributes([\"Imageattributes\"])]**[)[%\>]][]                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\@{][ Html.Syncfusion().TreeView([\"myTreeView\"]][,[\"Databind\"]][)] |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [.**DataSource(Model)**]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[.BindTo(bind=\>]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[bind.Text([\"Title\"])]**                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[    .Id([\"TreeViewId\"])]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[    .ParentId([\"ParentId\"])]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[    .SpriteCss([\"SpriteClass\"])]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[    .ImageUrl([\"ImagePath\"])]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[    .ImageAttributes([\"Imageattributes\"])]**[).Render();[}]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Build and run the application.

{border="0"}

Figure 326: TreeView - Data Binding Using TreeViewBuilder

 

Using TreeViewModel

To customize Data Binding in TreeView by using TreeViewModel:

1.   In the **Controller**, create an object for the **TreeViewModel** class.

2.   Set the **DataSource** and **BindTo** properties.

3.   Pass the **TreeViewModel** class to the **ViewData**.

 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [      **\[Controller\]**]                                                                                                                    |
|                                                                                                                                                                                   |
| [        [public] [ActionResult] Index()]                                                        |
|                                                                                                                                                                                   |
| [        {]                                                                                                                                   |
|                                                                                                                                                                                   |
| [            [Northwind] context = SqlCE;]                                                                            |
|                                                                                                                                                                                   |
| [            [TreeViewFields] treeViewFields = [new] [TreeViewFields]()] |
|                                                                                                                                                                                   |
| [            {]                                                                                                                               |
|                                                                                                                                                                                   |
| [                Id = [\"Id\"],]                                                                                      |
|                                                                                                                                                                                   |
| [                ParentId = [\"ParentId\"],]                                                                          |
|                                                                                                                                                                                   |
| [                Text = [\"Text\"],]                                                                                  |
|                                                                                                                                                                                   |
| [                ImageUrl = [\"ImageUrl\"],]                                                                          |
|                                                                                                                                                                                   |
| [                SpriteCSS = [\"SpriteCSS\"]]                                                                         |
|                                                                                                                                                                                   |
| [            };]                                                                                                                              |
|                                                                                                                                                                                   |
| [            [TreeViewModel] treeviewModel = [new] [TreeViewModel]()]    |
|                                                                                                                                                                                   |
| [            {]                                                                                                                               |
|                                                                                                                                                                                   |
| [                DataSource = context.TreeDatabinding.ToList(),]                                                                              |
|                                                                                                                                                                                   |
| [                BindTo = treeViewFields,]                                                                                                    |
|                                                                                                                                                                                   |
| [            };]                                                                                                                              |
|                                                                                                                                                                                   |
| [            ViewData\[[\"myTreeViewModel\"]\] = treeviewModel;]                                                      |
|                                                                                                                                                                                   |
| [            [return] View();]                                                                                           |
|                                                                                                                                                                                   |
| [        }]                                                                                                                                   |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

4.   Create a **View**.

5.   In the **View**, invoke the **TreeView** helper with the control ID.

6.   From the **ViewData**, assign the **TreeViewModel** class to the **TreeView** helper.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                           |
| [        [\<%][=]Html.Syncfusion().TreeView([\"MyTreeView\"], [\"Databind\"], ([TreeViewModel])ViewData\[[\"myTreeViewModel\"]\]) [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [     [@(][new] [HtmlString](Html.Syncfusion().TreeView([\"MyTreeView\"], [\"Databind\"], ([TreeViewModel])ViewData\[[\"myTreeViewModel\"]\]).ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Build and run the application.

{border="0"}

Figure 327: TreeView - Data Binding Using TreeViewModel

 

Properties

The properties of the Data Binding feature in TreeView are described in the following tabulation:

 


  ----------------------------------------- ------------------------------------------------------------------------------------------------------------------- ------------------------------------- ---------------------------------------- ----------------------------------------
  Name                                      Description                                                                                                         Type                                  Data Type                                Reference links
  [DataSource]        Gets or sets the data source, which is used to populate TreeView with the TreeView items.[]   [Server-side]   [IEnumerable]      [Not applicable]
  [BindTo]            Maps the TreeView fields to their respective columns from the data source.[]                  [Server-side]   [TreeViewFields]   [Not applicable]
  [Id]                Gets or sets the ID column name.[]                                                            [Server-side]   [string]           [Not applicable]
  [ParentId]          Gets or sets the parent ID column name.                                                                             [Server-side]   [string]           [Not applicable]
  [Text]              Gets or sets the text column name.[]                                                          [Server-side]   [string]           [Not applicable]
  [SpriteCss]         Gets or sets the sprite column name.[]                                                        [Server-side]   [string]           [Not applicable]
  [ImageUrl]          Gets or sets the image path column name.[]                                                    [Server-side]   [string]           [Not applicable]
  [HtmlAttributes]    Gets or sets the HTML attributes column name.[]                                               [Server-side]   [string]           [Not applicable]
  [ImageAttributes]   Gets or sets the image attributes column name.[]                                              [Server-side]   [string]           [Not applicable]
  ----------------------------------------- ------------------------------------------------------------------------------------------------------------------- ------------------------------------- ---------------------------------------- ----------------------------------------


[] 

Sample Link

To view a sample:

1.   Open the Tools Sample Browser from the dashboard. (Refer to the Samples and Location chapter.)

2.   Navigate to **Tools.Mvc** \> **TreeView** \> **Data Binding Demo**.

[] 

[]{#related-topics}

