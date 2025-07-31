---
title: usingpropertiesmodel16.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel16.md
created_at: 2025-07-03
---






#### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps guide in handling multiple selection through the properties model.

1.   In the **controller**, create an object for the **DiagramPropertiesModel** class. Assign this model class to the **view data**. 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                       |
|                                                                                                                                                                                                             |
| []                                                                                                                                                     |
|                                                                                                                                                                                                             |
| ```                                                                                                                             |
| DiagramPropertiesModel model = new DiagramPropertiesModel()                                                                                                                                                 |
| ```                                                                                                                                                                                                         |
|                                                                                                                                                                                                             |
| ```                                                                                                                             |
|             {                                                                                                                                                                                               |
| ```                                                                                                                                                                                                         |
|                                                                                                                                                                                                             |
| ```                                                                                                                             |
|                 Width = 900,                                                                                                                                                                                |
| ```                                                                                                                                                                                                         |
|                                                                                                                                                                                                             |
| ```                                                                                                                                                                            |
|                 Height = 500,                                                                                                                                                                               |
| ```                                                                                                                                                                                                         |
|                                                                                                                                                                                                             |
| ```                                                                                                                                                       |
|                 DiagramMode = DiagramMode.SVG,                                                                                                                                                              |
| ```                                                                                                                                                                                                         |
|                                                                                                                                                                                                             |
| ```                                                                                                                                                                            |
|                 AllowMultipleSelect = true                                                                                                                                                                  |
| ```                                                                                                                                                                                                         |
|                                                                                                                                                                                                             |
| ```                                                                                                                                                                            |
|             };                                                                                                                                                                                              |
| ```                                                                                                                                                                                                         |
|                                                                                                                                                                                                             |
| ```                                                                                                                                                                            |
|             ViewData["FlatDiagram"] = model;                                                                                                                                                                |
| ```                                                                                                                                                                                                         |
|                                                                                                                                                                                                             |
| [            ][return][ View();][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

2.   In the **view**, invoke the **Diagram** helper with the **view data key** as the control ID.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**[]                              |
|                                                                                                                                                     |
| ```                                                                                                                    |
| <%{                                                                                                                                                 |
| ```                                                                                                                                                 |
|                                                                                                                                                     |
| ```                                                                                                                    |
|       Html.Syncfusion().Diagram("FlatDiagram")                                                                                                      |
| ```                                                                                                                                                 |
|                                                                                                                                                     |
| [          .Render();]                                                                         |
|                                                                                                                                                     |
| ```                                                                                                                    |
|   }                                                                                                                                                 |
| ```                                                                                                                                                 |
|                                                                                                                                                     |
| [%\>][] |
|                                                                                                                                                     |
| []                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application.

 

[]{#related-topics}

