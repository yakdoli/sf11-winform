---
title: throughdiagrampropertiesmodel3.md
original_path: WinForms_Docs/04_Controls/Diagram/throughdiagrampropertiesmodel3.md
created_at: 2025-08-05
---






#### Through Diagram Properties Model {#through-diagram-properties-model style="tab-stops: 0pt"}

1.  [Create a model in the application (Refer to ][[Getting Started \> Examining the MVC Project \> Adding a Model to the Application]](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2Faddingamodeltotheapplication.htm)[).]

2.  [Create a **DiagramPropertiesModel** in the **Index** method. Bind the data source using the **DataSource** property and pass the model from the **controller** to the **view** using the **ViewData** class as shown in the following code.]


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                            |
|                                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                                       |
| [        [public] [ActionResult] Index()]                                                               |
|                                                                                                                                                                                                       |
| [        {]                                                                                                                                          |
|                                                                                                                                                                                                       |
| [            [DiagramPropertiesModel] model = [new] [DiagramPropertiesModel]()] |
|                                                                                                                                                                                                       |
| [            {]                                                                                                                                      |
|                                                                                                                                                                                                       |
| [                DataSource = [new] [CompanyDataContext]().Company,]                                    |
|                                                                                                                                                                                                       |
| [                BindTo = [new] [DiagramFields]()]                                                      |
|                                                                                                                                                                                                       |
| [                {]                                                                                                                                  |
|                                                                                                                                                                                                       |
| [                    NodeId = [\"DeptId\"],]                                                                                 |
|                                                                                                                                                                                                       |
| [                    ParentNodeId = [\"HeadDept\"],]                                                                         |
|                                                                                                                                                                                                       |
| [                    NodeText = [\"DeptName\"],]                                                                             |
|                                                                                                                                                                                                       |
| [                    NodeShape = [\"Shape\"]]                                                                                |
|                                                                                                                                                                                                       |
| [                },]                                                                                                                                 |
|                                                                                                                                                                                                       |
| [                DiagramMode = [DiagramMode].SVG,]                                                                           |
|                                                                                                                                                                                                       |
| [                LayoutType = [LayoutType].HierarchicalTreeLayout,]                                                          |
|                                                                                                                                                                                                       |
| [                Orientation = [TreeOrientation].TopBottom,]                                                                 |
|                                                                                                                                                                                                       |
| [                Width = 800,]                                                                                                                       |
|                                                                                                                                                                                                       |
| [                Height = 450]                                                                                                                       |
|                                                                                                                                                                                                       |
| [            };]                                                                                                                                     |
|                                                                                                                                                                                                       |
| [            ViewData\[[\"GenericList\"]\] = model;]                                                                         |
|                                                                                                                                                                                                       |
| [            [return] View();]                                                                                                  |
|                                                                                                                                                                                                       |
| [        }]                                                                                                                                          |
|                                                                                                                                                                                                       |
| []                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

[3.   ]In the **view**, invoke the **Diagram** helper with the control ID the same as the view data key.[ ]

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                             |
|                                                                                                                                |
| [\<%][{] |
|                                                                                                                                |
| [      Html.Syncfusion().Diagram([\"GenericList\"])]  |
|                                                                                                                                |
| [        .Render();]                                                          |
|                                                                                                                                |
| [  }[%\>]]                                        |
|                                                                                                                                |
| []                                                        |
|                                                                                                                                |
| []                                                        |
|                                                                                                                                |
| **[\[Razor\]]**                                                                            |
|                                                                                                                                |
| [\@{][]  |
|                                                                                                                                |
| [    Html.Syncfusion().Diagram([\"GenericList\"])]    |
|                                                                                                                                |
| [        .Render();]                                                          |
|                                                                                                                                |
| [}][]    |
|                                                                                                                                |
| []                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------+

 

4.  [Build and run the application. The diagram will appear as shown below.]

{border="0"}

Figure 128: Generic Collection Diagram

 

[]{#related-topics}

