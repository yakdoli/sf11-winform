---
title: howtobinddatatotherotatorcontrol.md
original_path: WinForms_Docs/03_Data_Binding/howtobinddatatotherotatorcontrol.md
created_at: 2025-08-05
---








  









### How to bind data to the Rotator control? {#how-to-bind-data-to-the-rotator-control style="tab-stops: 0pt"}

The Rotator provides extensive data binding support to populate Rotator items so that the columns of a table can be mapped to the Rotator properties, namely Text and ImageUrl.

 The Data Binding feature helps users to plug-in data from a DataTable or DataSet to the Rotator.

[] 

Enabling Data Binding in Rotator control

[Data Binding in the Rotator can be customized by using two ways, namely:]

[·      ]RotatorBuilder

[·      ]RotatorModel

[] 

Using RotatorBuilder

[To customize Data Binding in the Rotator by using RotatorBuilder:]

1.   In the[ ]**Controller**, pass the data to the[ ]**View**[ ]page.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Controller\]]**                                                                                      |
|                                                                                                                                                |
| [public][ [ActionResult] Index()] |
|                                                                                                                                                |
| [        {]                                                                                                |
|                                                                                                                                                |
| [            [Northwind] data = SqlCE;]                                            |
|                                                                                                                                                |
| [            [// Passing the data to the View.]]                                     |
|                                                                                                                                                |
| [            [return] View(data.RotatorData);]                                        |
|                                                                                                                                                |
| [  }  ][]                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[][] 

[2.   ]Create a Strongly Typed View.[]

[3.   In the][ ]**[View]**[, invoke the][ ]**[Rotator]**[ ][helper with the control ID.]

[4.   Set the][ ]**[DataSource][ ]**[and]**[ ][BindTo][ ]**[methods.]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Rotator([\"myRotator\"])] |
|                                                                                                                                                                                                                           |
| [.**DataSource(Model)**]                                                                                                                                                              |
|                                                                                                                                                                                                                           |
| **[.BindTo(bind=\>]**                                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| **[bind.Text([\"Text\"])    ]**                                                                                                                               |
|                                                                                                                                                                                                                           |
| **[                  .ImageUrl([\"ImagePath\"])]**[)[%\>]]                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the application.

[] 

[] 

Using RotatorModel

[To customize Data Binding in the Rotator by using RotatorModel:]

1.   In the[ ]**Controller**, create an object for the[ ]**RotatorModel**[ ]class.

2.   Set the[ ]**DataSource**[ ]and[ ]**BindTo**[ ]properties.

3.   Pass the[ ]**RotatorModel**[ ]class to the[ ]**ViewData**.

[] 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [      **\[Controller\]**]                                                                                                                 |
|                                                                                                                                                                                |
| [public][ [ActionResult] Index()]                                 |
|                                                                                                                                                                                |
| [        {]                                                                                                                                |
|                                                                                                                                                                                |
| [            [Northwind] context = SqlCE;]                                                                         |
|                                                                                                                                                                                |
| [            [RotatorFields] rotatorFields = [new] [RotatorFields]()] |
|                                                                                                                                                                                |
| [            {                ]                                                                                                            |
|                                                                                                                                                                                |
| [                Text = [\"Text\"],]                                                                               |
|                                                                                                                                                                                |
| [                ImageUrl = [\"ImageUrl\"]             ]                                                           |
|                                                                                                                                                                                |
| [            };]                                                                                                                           |
|                                                                                                                                                                                |
| [            [RotatorModel] rotatorModel = [new] [RotatorModel]()]    |
|                                                                                                                                                                                |
| [            {]                                                                                                                            |
|                                                                                                                                                                                |
| [                DataSource = context.RotatorData.ToList(),]                                                                               |
|                                                                                                                                                                                |
| [                BindTo = rotatorFields,]                                                                                                  |
|                                                                                                                                                                                |
| [            };]                                                                                                                           |
|                                                                                                                                                                                |
| [            ViewData\[[\"myRotatorModel\"]\] = rotatorModel;]                                                     |
|                                                                                                                                                                                |
| [            [return] View();]                                                                                        |
|                                                                                                                                                                                |
| [  }  ]                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[][] 

4.   In the[ ]**View**, invoke the[ ]**Rotator**[ ]helper with the control ID.

5.   From the[ ]**ViewData**, assign the[ ]**RotatorModel[ ]**class to the[ ]**Rotator**[ ]helper.

[] 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                              |
| [        [\<%][=]Html.Syncfusion().Rotator([\"myRotator\"], ([RotatorModel])ViewData\[[\"myRotatorModel\"]\])[%\>]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

6.   Build and run the application.

[] 

[] 

Properties

[The properties used for data binding in the Rotator are described in the following tabulation:* *]

[][] 


  ------------ --------------------------------------------------------------------------------------------- ------------- --------------- -----------------
  Name         Description                                                                                   Type          Data Type       Reference links
  DataSource   Gets or sets the data source, which is used to populate the Rotator with the Rotator items.   Server-side   IEnumerable     Not applicable
  BindTo       Maps the Rotator fields to their respective columns from the data source.                     Server-side   RotatorFields   Not applicable
  Text         Gets or sets the text column name.                                                            Server-side   string          Not applicable
  ImageUrl     Gets or sets the image path column name.                                                      Server-side   string          Not applicable
  ------------ --------------------------------------------------------------------------------------------- ------------- --------------- -----------------


 

[]{#related-topics}

