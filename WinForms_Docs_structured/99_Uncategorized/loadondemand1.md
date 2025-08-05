---
title: loadondemand1.md
original_path: WinForms_Docs/99_Uncategorized/loadondemand1.md
created_at: 2025-08-05
---






#### LoadOnDemand {#loadondemand style="tab-stops: 0pt"}

LoadOnDemand can load TreeView nodes on demand by using Ajax requests. The TreeView control populates its child nodes on demand by using Ajax. All root items and child nodes are loaded by clicking the Expand icon. You can enable LoadOnDemand in TreeView by using the LoadOnDemand property.

 

Use Case Scenarios

The LoadOnDemand feature is designed to improve the performance of TreeView.

 

Adding LoadOnDemand[ ]to an Application

LoadOnDemand in TreeView can be customized by using two ways, namely:

[·      ]TreeViewBuilder

[·      ]TreeViewModel

 

Using TreeViewBuilder

To customize LoadOnDemand in TreeView by using TreeViewBuilder:

1.   In the **Controller**, pass the data to the **View** page.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [public][ [ActionResult] ][Databinding][()] |
|                                                                                                                                                                                                                                  |
| [        {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [            [Northwind] data = SqlCE;]                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [            [// Passing the data to the View.]]                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [            [return] View(data.][ ][TreeDatabinding);]                                         |
|                                                                                                                                                                                                                                  |
| [  }   ]                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In the **Controller**, define the post action.

3.   Get the child nodes from the data source by using the expanded parent node ID.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                |
|                                                                                                                                                                                                                                  |
| [        [public] [ActionResult] LoadOnDemand([TreeViewModel] treeViewModel, [TreeViewItem] b)] |
|                                                                                                                                                                                                                                  |
| [        {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [            [Northwind] context = SqlCE;]                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [            [var] subNodes = SqlCE.TreeDatabinding.Where(c =\> c.ParentId == [Convert].ToInt32(b.Value));]                                     |
|                                                                                                                                                                                                                                  |
| [            [return] [new] [JsonResult] { Data = subNodes };]                                                             |
|                                                                                                                                                                                                                                  |
| [        }]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

4.   Create a [Strongly Typed View]{.UGHyperlink}.

5.   In the **View**, invoke the **TreeView** helper with the control ID.

6.   Set the **DataSource**, **BindTo, RequestMapper**, and **LoadOnDemand** methods.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [\<%][=][Html.Syncfusion().Treeview([\"myTreeview\"])] |
|                                                                                                                                                                                                                             |
| [.**DataSource(Model)**]                                                                                                                                                                |
|                                                                                                                                                                                                                             |
| [.**LoadOnDemand(**]**[true][)]**                                                                  |
|                                                                                                                                                                                                                             |
| [            **.RequestMapper([\"LoadOnDemand\"])**]                                                                                                            |
|                                                                                                                                                                                                                             |
| **[.BindTo(bind=\>]**                                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| **[bind.Text([\"Title\"])]**                                                                                                                                    |
|                                                                                                                                                                                                                             |
| **[    .Id([\"TreeviewId\"])]**                                                                                                                                 |
|                                                                                                                                                                                                                             |
| **[    .ParentId([\"ParentId\"])]**                                                                                                                             |
|                                                                                                                                                                                                                             |
| **[    .SpriteCss([\"SpriteClass\"])]**                                                                                                                         |
|                                                                                                                                                                                                                             |
| **[    .ImageUrl([\"ImagePath\"])]**                                                                                                                            |
|                                                                                                                                                                                                                             |
| **[    .ImageAttributes([\"Imageattributes\"])]**[)[%\>]]                                       |
|                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                            |
|                                                                                                                                                                                               |
|                                                                                                                                                                                               |
|                                                                                                                                                                                               |
| [\@{][ Html.Syncfusion().Treeview([\"myTreeview\"])]                      |
|                                                                                                                                                                                               |
| [.**DataSource(Model)**]                                                                                                                                  |
|                                                                                                                                                                                               |
| [.**LoadOnDemand(**]**[true][)]**                                    |
|                                                                                                                                                                                               |
| [            **.RequestMapper([\"LoadOnDemand\"])**]                                                                              |
|                                                                                                                                                                                               |
| **[.BindTo(bind=\>]**                                                                                                                                     |
|                                                                                                                                                                                               |
| **[bind.Text([\"Title\"])]**                                                                                                      |
|                                                                                                                                                                                               |
| **[    .Id([\"TreeviewId\"])]**                                                                                                   |
|                                                                                                                                                                                               |
| **[    .ParentId([\"ParentId\"])]**                                                                                               |
|                                                                                                                                                                                               |
| **[    .SpriteCss([\"SpriteClass\"])]**                                                                                           |
|                                                                                                                                                                                               |
| **[    .ImageUrl([\"ImagePath\"])]**                                                                                              |
|                                                                                                                                                                                               |
| **[    .ImageAttributes([\"Imageattributes\"])]**[).Render();[}]] |
|                                                                                                                                                                                               |
| **[]**                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Build and run the application.

 

{border="0"}

Figure 317: TreeView - LoadOnDemand Using TreeViewBuilder

 

Using TreeViewModel

To customize Data Binding in TreeView by using TreeViewModel:

1.   In the **Controller**, create an object for the **TreeViewModel** class.

2.   Set the **DataSource**, **BindTo**, and **LoadOnDemand** properties.

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
| [                LoadOnDemand = [true],]                                                                                 |
|                                                                                                                                                                                   |
| [                RequestMapper = [\"LoadOnDemand\"]]                                                                  |
|                                                                                                                                                                                   |
| [            };]                                                                                                                              |
|                                                                                                                                                                                   |
| [            ViewData\[[\"myTreeViewModel\"]\] = treeviewModel;]                                                      |
|                                                                                                                                                                                   |
| [            [return] View();]                                                                                           |
|                                                                                                                                                                                   |
| [        }]                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

4.   In the **Controller**, define the post action.

5.   Get the child nodes from the data source by using the expanded parent node ID.

 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                |
|                                                                                                                                                                                                                                  |
| [        [public] [ActionResult] LoadOnDemand([TreeViewModel] treeViewModel, [TreeViewItem] b)] |
|                                                                                                                                                                                                                                  |
| [        {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [            [Northwind] context = SqlCE;]                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [            [var] subNodes = SqlCE.TreeDatabinding.Where(c =\> c.ParentId == [Convert].ToInt32(b.Value));]                                     |
|                                                                                                                                                                                                                                  |
| [            [return] [new] [JsonResult] { Data = subNodes };]                                                             |
|                                                                                                                                                                                                                                  |
| [        }]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

6.   Create a **View**.

7.   In the **View**, invoke the **TreeView** helper with the control ID.

8.   From the **ViewData**, assign the **TreeViewModel** class to the **TreeView** helper.

 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                           |
| [        [\<%][=]Html.Syncfusion().TreeView([\"MyTreeView\"], [\"Databind\"], ([TreeViewModel])ViewData\[[\"myTreeViewModel\"]\]) [%\>]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [      [@(][new] [HtmlString](Html.Syncfusion().TreeView([\"MyTreeView\"], [\"Databind\"], ([TreeViewModel])ViewData\[[\"myTreeViewModel\"]\]).ToString())[)]     ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

9.   Build and run the application.

 

 

{border="0"}

Figure 318: TreeView - LoadOnDemand Using TreeViewModel[]

 

Properties

The properties of the LoadOnDemand feature in TreeView are described in the following tabulation:

 

  --------------- ----------------------------------------------------- ------------- ----------- -----------------
  Name            Description                                           Type          Data Type   Reference links
  LoadOnDemand    Enables or disables LoadOnDemand in TreeView.         Server-side   Bool        Not applicable
  RequestMapper   Gets or sets the name for the post action function.   Server-side   String      Not applicable
  --------------- ----------------------------------------------------- ------------- ----------- -----------------

[] 

[] 

Events

The events of the LoadOnDemand feature in TreeView are described in the following tabulation:

 

 

+---------------------------+--------------------------------------------------------------------------------+--------------------+-------------+-----------------+
| Event                     | Description                                                                    | Arguments          | Type        | Reference links |
+---------------------------+--------------------------------------------------------------------------------+--------------------+-------------+-----------------+
| ClientSideOnBeforeRequest | Sets the function name to raise the event before the Ajax request.             | Instance and args. | Client-side | Not applicable  |
+---------------------------+--------------------------------------------------------------------------------+--------------------+-------------+-----------------+
| ClientSideOnSuccess       | Sets the function name to raise the event when the Ajax request is successful. | Instance and args. | Client-side | Not applicable  |
+---------------------------+--------------------------------------------------------------------------------+--------------------+-------------+-----------------+
| ClientSideOnFailure       | Sets the function name to raise the event when the Ajax request has failed.    | Instance and args. | Client-side | Not applicable  |
|                           |                                                                                |                    |             |                 |
|                           |                                                                                |                    |             |                 |
+---------------------------+--------------------------------------------------------------------------------+--------------------+-------------+-----------------+

[][] 

Sample Link

To view a sample:

1.   Open the Tools Sample Browser from the dashboard. (Refer to the Samples and Location chapter.)

2.   Navigate to **Tools.Mvc** -\> **TreeView** -\> **LoadOnDemand Demo**.

[] 

[]{#related-topics}

