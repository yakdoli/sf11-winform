---
title: addingresourceregistrationtoanapplication4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\addingresourceregistrationtoanapplication4.md
created_at: 2025-07-03
---








  









### Adding Resource Registration to an Application {#adding-resource-registration-to-an-application style="tab-stops: 0pt"}

 

Methods

Table 4: Resource Management Method Table


+----------------------------------+---------------------------------------------------------------+------------------------------------------------+-------------+-------------------+-----------------+
| Method                           | Description                                                   | Parameters                                     | Type        | Return Type       | Reference links |
+----------------------------------+---------------------------------------------------------------+------------------------------------------------+-------------+-------------------+-----------------+
| StyleManager()                   | Used to initialize the StyleManager instance                  | NA                                             | Server-side | StyleManager      | NA              |
+----------------------------------+---------------------------------------------------------------+------------------------------------------------+-------------+-------------------+-----------------+
| [Register] | Used to register the components style                         | (Action\<ComponentFactoryBuilder\> components) | Server-side | StyleManager      | NA              |
|                                  |                                                               |                                                |             |                   |                 |
|                                  |                                                               |                                                |             |                   |                 |
|                                  |                                                               |                                                |             |                   |                 |
|                                  |                                                               | (string components)                            |             |                   |                 |
+----------------------------------+---------------------------------------------------------------+------------------------------------------------+-------------+-------------------+-----------------+
| [Minify]   | Used to enable or disable the minify feature for styleManager | (bool enable)                                  | Server-side | StyleManager      | NA              |
|                                  |                                                               |                                                |             |                   |                 |
|                                  |                                                               | Default:True                                   |             |                   |                 |
+----------------------------------+---------------------------------------------------------------+------------------------------------------------+-------------+-------------------+-----------------+
| [Combine]  | Used to enable/disable the combined files feature             | (bool enable)                                  | Server-side | StyleManager      | NA              |
|                                  |                                                               |                                                |             |                   |                 |
|                                  |                                                               | Default: True                                  |             |                   |                 |
+----------------------------------+---------------------------------------------------------------+------------------------------------------------+-------------+-------------------+-----------------+
| [Add]      | Used to add the components/CSS files to the stylemanager      | (Component Type)                               | Server-side | IComponentBuilder | NA              |
|                                  |                                                               |                                                |             |                   |                 |
|                                  |                                                               |                                                |             |                   |                 |
|                                  |                                                               |                                                |             |                   |                 |
|                                  |                                                               | (string path)                                  |             |                   |                 |
+==================================+===============================================================+================================================+=============+===================+=================+


***[]*** 


+----------------------+--------------------------------------------------------------------------+---------------------+-------------+---------------------+-----------------+
| Method               | Description                                                              | Parameters          | Type        | Return Type         | Reference links |
+----------------------+--------------------------------------------------------------------------+---------------------+-------------+---------------------+-----------------+
| JqueryTheme          | Used to apply JqueryTheme to JqueryControls                              | (JquerySkins skins) | Server-side | IComponentBuilder   | NA              |
+----------------------+--------------------------------------------------------------------------+---------------------+-------------+---------------------+-----------------+
| DontOverrride        | Used to disable the Theme override to specific control by external theme | NA                  | Server-side | IComponentBuilder   | NA              |
+----------------------+--------------------------------------------------------------------------+---------------------+-------------+---------------------+-----------------+
| DisableChildRegister | Used to disable the sub component registration                           | NA                  | Server-side | IComponentBuilder   | NA              |
+----------------------+--------------------------------------------------------------------------+---------------------+-------------+---------------------+-----------------+
| AllowChildRegister   | Used to enable or disable the Sub component registration                 | (bool enable)       | Server-side | IComponentBuilder   | NA              |
+----------------------+--------------------------------------------------------------------------+---------------------+-------------+---------------------+-----------------+
| ScriptManager        | Used to register the Javascript files in Syncfusion Mvc assemblies       | NA                  | Server-side | MvcResourceRenderer | NA              |
+----------------------+--------------------------------------------------------------------------+---------------------+-------------+---------------------+-----------------+
| Minify               | Used to enable or disable the minify feature to ScriptManager            | (bool enable)       | Server-side | MvcResourceRenderer | NA              |
|                      |                                                                          |                     |             |                     |                 |
|                      |                                                                          | Default:True        |             |                     |                 |
+======================+==========================================================================+=====================+=============+=====================+=================+


[] 

Sample Link[]

To view the samples:

1.   Open the  **ASP.NET MVC** sample browser from the dashboard. (Refer to  chapter).

2.   Navigate to **SiteMaster.Master** file.

[] 

More:









