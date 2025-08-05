---
title: addingbuttontoanapplication.md
original_path: WinForms_Docs/99_Uncategorized/addingbuttontoanapplication.md
created_at: 2025-08-05
---








  









### Adding Button to an Application {#adding-button-to-an-application style="tab-stops: 0pt"}

In the Getting Started section, we discussed how to create a MVC application and add the Tools package to the application. This section guides you to add the Button control to an application.

1.   In View, invoke the normal Button helper with the button id as the first argument followed by the button's **Text**, **ImageUrl** and **ContentType** methods.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                   |
|                                                                                                                                                                          |
| **[]**                                                                                                                               |
|                                                                                                                                                                          |
| [        [\<%][=]Html.Syncfusion().Button([\"btnNormal\"])] |
|                                                                                                                                                                          |
| [        .Text([\"Save\"])]                                                                                  |
|                                                                                                                                                                          |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                             |
|                                                                                                                                                                          |
| [        .ContentType([ContentTypes].TextAndImage) [%\>]]                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [        ][ [\@{]][ Html.Syncfusion().Button([\"btnNormal\"])] |
|                                                                                                                                                                                                                                |
| [        .Text([\"Save\"])]                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                                                                   |
|                                                                                                                                                                                                                                |
| [        .ContentType([ContentTypes].TextAndImage)][.Render();[}]]                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   Run the application.

 

The output is shown in the following screenshot.

 

 

 

{border="0"}

Figure 83: Normal Button

[] 

[]{#related-topics}

