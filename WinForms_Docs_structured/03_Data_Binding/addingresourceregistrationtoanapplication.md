---
title: addingresourceregistrationtoanapplication.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\addingresourceregistrationtoanapplication.md
created_at: 2025-07-03
---








  









### Adding Resource Registration to an Application {#adding-resource-registration-to-an-application style="tab-stops: 0pt"}

Methods

 


+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| Method                           | Description                                                              | Parameters                                     | Type            | Return Type         | Reference links |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| StyleManager()                   | Used to initialize the StyleManager instance                             | NA                                             | **Server-side** | StyleManager        | NA              |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| [Register] | Used to register the components style                                    | (Action\<Com\[ponentFactoryBuilder components) | **Server-side** | StyleManager        | StyleManager    |
|                                  |                                                                          |                                                |                 |                     |                 |
|                                  |                                                                          |                                                |                 |                     |                 |
|                                  |                                                                          |                                                |                 |                     |                 |
|                                  |                                                                          | (string components)                            |                 |                     |                 |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| [Theme]    | Used to apply themes to all the components                               | (Skins skin)                                   | **Server-side** | StyleManager        | StyleManager    |
|                                  |                                                                          |                                                |                 |                     |                 |
|                                  |                                                                          | Default:Office2007Blue                         |                 |                     |                 |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| [Minify]   | Used to enable or disable the minify feature for styleManager            | (bool enable)                                  | **Server-side** | StyleManager        | StyleManager    |
|                                  |                                                                          |                                                |                 |                     |                 |
|                                  |                                                                          | Default:True                                   |                 |                     |                 |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| [Combine]  | Used to enable/disable the combined files feature                        | (bool enable)                                  | **Server-side** | StyleManager        | StyleManager    |
|                                  |                                                                          |                                                |                 |                     |                 |
|                                  |                                                                          | Default: True                                  |                 |                     |                 |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| [Add]      | Used to add the components/CSS files to stylemanager                     | (Component Type)                               | **Server-side** | IComponentBuilder   | Register        |
|                                  |                                                                          |                                                |                 |                     |                 |
|                                  |                                                                          |                                                |                 |                     |                 |
|                                  |                                                                          |                                                |                 |                     |                 |
|                                  |                                                                          | (string path)                                  |                 |                     |                 |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| [Theme]    | Used to apply theme to specify component                                 | (Skins skin)                                   | **Server-side** | IComponentBuilder   | Register        |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| JqueryTheme                      | Used to apply JqueryTheme to JqueryControls                              | (JquerySkins skins)                            | **Server-side** | IComponentBuilder   | Register        |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| DontOverrride                    | Used to disable the Theme override to specific control by external theme | NA                                             | **Server-side** | IComponentBuilder   | Register        |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| DisableChildRegister             | Used to disable the sub-component registration                           | NA                                             | **Server-side** | IComponentBuilder   | Register        |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| AllowChildRegister               | Used to enable or disable the sub-component registration                 | (bool enable)                                  | **Server-side** | IComponentBuilder   | Register        |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| ScriptManager                    | Used to register the Javascript files in Syncfusion Mvc assemblies       | NA                                             | **Server-side** | MvcResourceRenderer | NA              |
+----------------------------------+--------------------------------------------------------------------------+------------------------------------------------+-----------------+---------------------+-----------------+
| Minify                           | Used to enable or disable the minify feature to ScriptManager            | (bool enable)                                  | **Server-side** | MvcResourceRenderer | ScriptManager   |
|                                  |                                                                          |                                                |                 |                     |                 |
|                                  |                                                                          | Default:True                                   |                 |                     |                 |
+==================================+==========================================================================+================================================+=================+=====================+=================+


[] 

Sample Link

To view the samples:

1.   Open the any MVC sample browser from the dashboard. (Refer to Samples and Location chapter).

2.   Navigate to **SiteMaster.Master file**.

[] 

More:







