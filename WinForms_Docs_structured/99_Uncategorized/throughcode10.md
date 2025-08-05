---
title: throughcode10.md
original_path: WinForms_Docs/99_Uncategorized/throughcode10.md
created_at: 2025-08-05
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

This tutorial shows how to create CallbackPanel entirely with code.

[] 

To create CallbackPanel in ASP.NET code, follow the below steps.

[] 

1.   Add new Web Form to your project.

16.  In .cs file, include the following directive.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                     |
|                                                                                                                                                                      |
| []                                                                                                  |
|                                                                                                                                                                      |
| [using][ Syncfusion.Web.UI.WebControls.Shared;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

17.  In code view, the control has to be installed and created as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                            |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)]                                         |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [       BuildCallbackPanel();]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [private][ [void] BuildCallbackPanel()]                                                                                                          |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [       [//Create an instance of the CallbackPanel]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [       [CallbackPanel] CallbackPanel1 = [new] [CallbackPanel]();]                                                                                                      |
|                                                                                                                                                                                                                                                                                            |
| [       CallbackPanel1.ID = [\"CalbackPanel1\"];]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                            |
| [       CallbackPanel1.GroupingText = [\"CallbackPanel\"];]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [       CallbackPanel1.Width = [Unit].Pixel( 200 );]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                            |
| [       CallbackPanel1.CallbackRefresh += [new] [CancellableCallbackEventHandler](CallbackPanel1_CallbackRefresh);]                                                                          |
|                                                                                                                                                                                                                                                                                            |
| [       ]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                            |
| [       [//add any child controls]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                            |
| [       CallbackPanel1.Controls.Add( [new] [LiteralControl]( [\"CallbackPanel content\<br\>\"] ));]                                                                   |
|                                                                                                                                                                                                                                                                                            |
| [       [//Create control to trigger callback]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                            |
| [       [Button] Button1 = [new] [Button]();]                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| [       Button1.OnClientClick = [\"\_sfCalbackPanel1.callback(); return false;\"];]                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [       Button1.Text = [\"callback\"];]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| [       CallbackPanel1.Controls.Add( Button1 );]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [       [//add CallbackPanel to form]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| [       form1.Controls.Add( CallbackPanel1 );]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [protected][ [void] CallbackPanel1_CallbackRefresh([object] sender, [CancellableCallbackEventArgs] e)] |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [       [//Update CallbackPanel and its content]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [       (([CallbackPanel])sender).GroupingText = [\"Callback process complete\"];]                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following code example demonstrates how to create single Splitter control with three SplitPanes programatically.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                 |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)]                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                 |
| [       BuildCallbackPanel();]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [private][ [void] BuildCallbackPanel()]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                 |
| [{      ]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                 |
| [       [CallbackPanel] CallbackPanel1 = [new] [CallbackPanel]();]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                 |
| [       CallbackPanel1.ID = [\"CalbackPanel1\"];]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                 |
| [       CallbackPanel1.GroupingText = [\"CallbackPanel\"];]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [       CallbackPanel1.Width = [Unit].Pixel( 200 );]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                 |
| [       CallbackPanel1.CallbackRefresh += [new] [CancellableCallbackEventHandler]( CallbackPanel1_CallbackRefresh );]                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                 |
| [       ]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                 |
| [       CallbackPanel1.Controls.Add( [new] [LiteralControl]( [\"CallbackPanel content\<br\>\"] ));]                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                 |
| [       [Button] Button1 = [new] [Button]();]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                 |
| [       Button1.OnClientClick = [\"\_sfCalbackPanel1.callback(); return false;\"];]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                 |
| [       Button1.Text = [\"callback\"];]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| [       CallbackPanel1.Controls.Add( Button1 );]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [       form1.Controls.Add( CallbackPanel1 );]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [protected][ [void] CallbackPanel1_CallbackRefresh([object] sender, Syncfusion.Web.UI.WebControls.Shared.[CancellableCallbackEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                 |
| [       (([CallbackPanel])sender).GroupingText = [\"Callback Response\"];]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

