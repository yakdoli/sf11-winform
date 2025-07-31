---
title: databinding14.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databinding14.md
created_at: 2025-07-03
---






#### Data Binding {#data-binding style="tab-stops: 0pt"}

 

Toolbar provides extensive data binding support to populate Toolbar items so that the columns of a table can be mapped to the Toolbar properties, namely Id, Text, ImageUrl, SpriteCss, ImageAttributes, and HtmlAttributes.

 

Use Case Scenarios

The Data Binding feature helps users to plug-in data from a DataTable or DataSet to Toolbar.

 

Adding Data Binding[ ]to an Application

Data Binding in Toolbar can be customized by using two ways, namely:

[·      ]ToolbarBuilder

[·      ]ToolbarModel

 

Using ToolbarBuilder

To customize Data Binding in Toolbar by using ToolbarBuilder:

1.   In the **Controller**, pass the data to the **View** page.

**[]** 

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
| [            [return] View(data.ToolbarData);]                                        |
|                                                                                                                                                |
| [  }   ]                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

2.   Create a [Strongly Typed View]{.UGHyperlink}.

3.   In the **View**, invoke the **Toolbar** helper with the control ID.

4.   Set the **DataSource** and **BindTo** methods.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Toolbar([\"myToolbar\"])] |
|                                                                                                                                                                                                                           |
| [.**DataSource(Model)**]                                                                                                                                                              |
|                                                                                                                                                                                                                           |
| **[.BindTo(bind=\>]**                                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| **[bind.Text([\"Title\"])]**                                                                                                                                  |
|                                                                                                                                                                                                                           |
| **[    .Id([\"ToolbarId\"])]**                                                                                                                                |
|                                                                                                                                                                                                                           |
| **[    .SpriteCss([\"SpriteClass\"])]**                                                                                                                       |
|                                                                                                                                                                                                                           |
| **[    .ImageUrl([\"ImagePath\"])]**                                                                                                                          |
|                                                                                                                                                                                                                           |
| **[    .ImageAttributes([\"Imageattributes\"])]**[)[%\>]]                                     |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                  |
| [\@{][ Html.Syncfusion().Toolbar([\"myToolbar\"])]                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [.**DataSource(Model)**]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                  |
| **[.BindTo(bind=\>]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                  |
| **[bind.Text([\"Title\"])]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                  |
| **[    .Id([\"ToolbarId\"])]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                  |
| **[    .SpriteCss([\"SpriteClass\"])]**                                                                                                                                                              |
|                                                                                                                                                                                                                                                                  |
| **[    .ImageUrl([\"ImagePath\"])]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| **[    .ImageAttributes([\"Imageattributes\"])]**[).Render();[}]][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the application.

 

{border="0"}

Figure 308: Toolbar - Data Binding Using ToolbarBuilder

 

 

Using ToolbarModel

 

To customize Data Binding in Toolbar by using ToolbarModel:

1.   In the **Controller**, create an object for the **ToolbarModel** class.

2.   Set the **DataSource** and **BindTo** properties.

3.   Pass the **ToolbarModel** class to the **ViewData**.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [      **\[Controller\]**]                                                                                                                 |
|                                                                                                                                                                                |
| [        [public] [ActionResult] Index()]                                                     |
|                                                                                                                                                                                |
| [        {]                                                                                                                                |
|                                                                                                                                                                                |
| [            [Northwind] context = SqlCE;]                                                                         |
|                                                                                                                                                                                |
| [            [ToolbarFields] toolbarFields = [new] [ToolbarFields]()] |
|                                                                                                                                                                                |
| [            {]                                                                                                                            |
|                                                                                                                                                                                |
| [                Id = [\"Id\"],]                                                                                   |
|                                                                                                                                                                                |
| [                ParentId = [\"ParentId\"],]                                                                       |
|                                                                                                                                                                                |
| [                Text = [\"Text\"],]                                                                               |
|                                                                                                                                                                                |
| [                ImageUrl = [\"ImageUrl\"],]                                                                       |
|                                                                                                                                                                                |
| [                SpriteCSS = [\"SpriteCSS\"]]                                                                      |
|                                                                                                                                                                                |
| [            };]                                                                                                                           |
|                                                                                                                                                                                |
| [            [ToolbarModel] toolbarModel = [new] [ToolbarModel]()]    |
|                                                                                                                                                                                |
| [            {]                                                                                                                            |
|                                                                                                                                                                                |
| [                DataSource = context.ToolbarData.ToList(),]                                                                               |
|                                                                                                                                                                                |
| [                BindTo = toolbarFields,]                                                                                                  |
|                                                                                                                                                                                |
| [            };]                                                                                                                           |
|                                                                                                                                                                                |
| [            ViewData\[[\"myToolbarModel\"]\] = toolbarModel;]                                                     |
|                                                                                                                                                                                |
| [            [return] View();]                                                                                        |
|                                                                                                                                                                                |
| [        }]                                                                                                                                |
|                                                                                                                                                                                |
| []                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

4.   Create a **View**.

5.   In the **View**, invoke the **Toolbar** helper with the control ID.

6.   From the **ViewData**, assign the **ToolbarModel** class to the **Toolbar** helper.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                               |
| [        [\<%][=]Html.Syncfusion().Toolbar([\"MyToolbar\"], ([ToolbarModel])ViewData\[[\"myToolbarModel\"]\]) [%\>]] |
|                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                |
| [        [\@{] Html.Syncfusion().Toolbar([\"MyToolbar\"], ([ToolbarModel])ViewData\[[\"myToolbarModel\"]\]).Render(); [}]] |
|                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Build and run the application.

 

{border="0"}

Figure 309: Toolbar - Data Binding Using ToolbarModel

 

**Properties**

The properties of the Data Binding feature in Toolbar are described in the following tabulation:

 

  ---------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------- --------------------------------------------------------------- ---------------------------------------------------------------------
  **[Name]**[]   **[Description]**[]                                                   **[Type]**[]   **[Data Type]**[]   **[Reference links]**[]
  [DataSource]                         [Gets or sets the data source, which is used to populate Toolbar with the Toolbar items.]   [Server-side]                        [IEnumerable]                             [Not applicable]
  [BindTo]                             [Maps the Toolbar fields to their respective columns from the data source.]                 [Server-side]                        [ToolbarFields]                           [ Not applicable]
  [Id]                                 [Gets or sets the ID column name.]                                                          [Server-side]                        [string]                                  [ Not applicable]
  [Text]                               [Gets or sets the text column name.]                                                        [Server-side]                        [string]                                  [ Not applicable]
  [SpriteCss]                          [Gets or sets the sprite column name.]                                                      [Server-side]                        [string]                                  [ Not applicable]
  [ImageUrl]                           [Gets or sets the image path column name.]                                                  [Server-side]                        [string]                                  [ Not applicable]
  [HtmlAttributes]                     [Gets or sets the HTML attributes column name.]                                             [Server-side]                        [string]                                  [ Not applicable]
  [ImageAttributes]                    [Gets or sets the image attributes column name.]                                            [Server-side]                        [string]                                  [ Not applicable]
  ---------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------- --------------------------------------------------------------- ---------------------------------------------------------------------

[] 

Sample Link

To view a sample:

1.   Open the Tools Sample Browser from the dashboard. (Refer to the Samples and Location chapter.)

2.   Navigate to **Tools.Mvc** -\> **Toolbar** -\> **Data Binding Demo**.

 

[]{#related-topics}

