---
title: assigncurrentuiculturetotheapplication3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\assigncurrentuiculturetotheapplication3.md
created_at: 2025-07-03
---






#### Assign Current UI Culture to the Application {#assign-current-ui-culture-to-the-application style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; tab-stops: 0pt"}

By default, the current culture will be **en-US**. You have to set the current culture before **IntializeComponent** in the StartUp page, or you can do it in **App.xaml.cs** in the **Application_Startup** event.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                |
| [public][ MainPage()]                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [  [Thread].CurrentThread.CurrentCulture = [new] System.Globalization.[CultureInfo]([\"es-ES\"]);]               |
|                                                                                                                                                                                                                                                                |
| [  [Thread].CurrentThread.CurrentUICulture = [new] System.Globalization.[CultureInfo]([\"es-ES\"]);            ] |
|                                                                                                                                                                                                                                                                |
| [  InitializeComponent();           ]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

