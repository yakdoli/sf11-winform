---
title: addingresourceregistrationtoanapplication8.md
original_path: WinForms_Docs/03_Data_Binding/addingresourceregistrationtoanapplication8.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Adding Resource Registration to an Application {#adding-resource-registration-to-an-application style="TEXT-INDENT: -36pt; MARGIN-LEFT: 36pt; tab-stops: 36.0pt"}

Methods

 

+----------------------------------+---------------------------------------------------------------+----------------------------------------------+-----------------+-------------------+-----------------+
| Method                           | Description                                                   | Parameters                                   | Type            | Return Type       | Reference links |
+----------------------------------+---------------------------------------------------------------+----------------------------------------------+-----------------+-------------------+-----------------+
| StyleManager()                   | Used to initialize the StyleManager instance                  | NA                                           | **Server-side** | StyleManager      | NA              |
+----------------------------------+---------------------------------------------------------------+----------------------------------------------+-----------------+-------------------+-----------------+
| [Register] | Used to register the components style                         | (Action\<ComponentFactoryBuilder components) | **Server-side** | StyleManager      | StyleManager    |
|                                  |                                                               |                                              |                 |                   |                 |
|                                  |                                                               |                                              |                 |                   |                 |
|                                  |                                                               |                                              |                 |                   |                 |
|                                  |                                                               | (string components)                          |                 |                   |                 |
+----------------------------------+---------------------------------------------------------------+----------------------------------------------+-----------------+-------------------+-----------------+
| [Theme]    | Used to apply themes to all the Components                    | (Skins skin)                                 | **Server-side** | StyleManager      | StyleManager    |
|                                  |                                                               |                                              |                 |                   |                 |
|                                  |                                                               | Default:Office2007Blue                       |                 |                   |                 |
+----------------------------------+---------------------------------------------------------------+----------------------------------------------+-----------------+-------------------+-----------------+
| [Minify]   | Used to enable or disable the minify feature for styleManager | (bool enable)                                | **Server-side** | StyleManager      | StyleManager    |
|                                  |                                                               |                                              |                 |                   |                 |
|                                  |                                                               | Default:True                                 |                 |                   |                 |
+----------------------------------+---------------------------------------------------------------+----------------------------------------------+-----------------+-------------------+-----------------+
| [Combine]  | Used to enable/disable the combined files feature             | (bool enable)                                | **Server-side** | StyleManager      | StyleManager    |
|                                  |                                                               |                                              |                 |                   |                 |
|                                  |                                                               | Default: True                                |                 |                   |                 |
+----------------------------------+---------------------------------------------------------------+----------------------------------------------+-----------------+-------------------+-----------------+
| [Add]      | Used to add the components/CSS files to stylemanager          | (Component Type)                             | **Server-side** | IComponentBuilder | Register        |
|                                  |                                                               |                                              |                 |                   |                 |
|                                  |                                                               |                                              |                 |                   |                 |
|                                  |                                                               |                                              |                 |                   |                 |
|                                  |                                                               | (string path)                                |                 |                   |                 |
+----------------------------------+---------------------------------------------------------------+----------------------------------------------+-----------------+-------------------+-----------------+
| [Theme]    | Used to apply theme to specify component                      | (Skins skin)                                 | **Server-side** | IComponentBuilder | Register        |
+==================================+===============================================================+==============================================+=================+===================+=================+

***[]***  

+---------------+--------------------------------------------------------------------------+---------------+-----------------+---------------------+-----------------+
| Method        | Description                                                              | Parameters    | Type            | Return Type         | Reference links |
+---------------+--------------------------------------------------------------------------+---------------+-----------------+---------------------+-----------------+
| DontOverrride | Used to disable the Theme override to specific control by external theme | NA            | **Server-side** | IComponentBuilder   | Register        |
+---------------+--------------------------------------------------------------------------+---------------+-----------------+---------------------+-----------------+
| ScriptManager | Used to register the Javascript files in Syncfusion Mvc assemblies       | NA            | **Server-side** | MvcResourceRenderer | NA              |
+---------------+--------------------------------------------------------------------------+---------------+-----------------+---------------------+-----------------+
| Minify        | Used to enable or disable the minify feature to ScriptManager            | (bool enable) | **Server-side** | MvcResourceRenderer | ScriptManager   |
|               |                                                                          |               |                 |                     |                 |
|               |                                                                          | Default:True  |                 |                     |                 |
+===============+==========================================================================+===============+=================+=====================+=================+

***[]***  

[] 

Sample Link

 

To view the samples, follow the below steps:

1.   Open the Mobile MVC sample browser from the dashboard. (Refer Samples and Location chapter)

2.   Navigate to Site.Master file

[] 

 

[] 

More:





