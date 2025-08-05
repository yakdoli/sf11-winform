---
title: addingtoolbarcontroltowindowsphoneanapplication.md
original_path: WinForms_Docs/99_Uncategorized/addingtoolbarcontroltowindowsphoneanapplication.md
created_at: 2025-08-05
---






#### Adding Toolbar Control to Windows Phone an Application {#adding-toolbar-control-to-windows-phone-an-application style="tab-stops: 0pt"}

To , refer to section . This section covers how to add Toolbar control to this application.

 

The *Toolbar* control can be added to the application using either Xaml or procedural code. The following code illustrartes this:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**[]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][ToolBar][\>]  |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                               |
| [\</][syncfusion][:][ToolBar][\>] |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][]**                                                                             |
|                                                                                                                                                                                                          |
| []                                                                                                                                      |
|                                                                                                                                                                                                          |
| [ToolBar][ toolbar1 = [new] [ToolBar]();] |
|                                                                                                                                                                                                          |
| [ [this].LayoutRoot.Children.Add(toolbar1);]                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 59: Adding Toolbar control

 


{border="0"}Note: Toolbar has to be added into the Root Layout element of the page, and only one Toolbar can be added in a page.

 


***[]*** 

[]{#related-topics}

