---
title: usingpropertiesmodel78.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel78.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using PropertiesModel {#using-propertiesmodel style="tab-stops: 0pt"}

1.   In the controller, create an instance of the **MobProgressBarPropertiesModel**.

2.   Define the **AutoFormat** property and pass the instance through the view-specific data to the view.

 

+----------------------------------------------------------------------------------------------------------------------------------------+
| [\[controller\]]                                                                                   |
|                                                                                                                                        |
| []                                                                                                 |
|                                                                                                                                        |
| [public ActionResult Index()]                                                                      |
|                                                                                                                                        |
| [{  ]                                                                                              |
|                                                                                                                                        |
| [MobProgressBarPropertiesModel pBar = [new] MobProgressBarPropertiesModel();] |
|                                                                                                                                        |
| [pBar.Value = 30;]                                                                                 |
|                                                                                                                                        |
| [pBar.AutoFormat = [MobSkins].Spinach;]                                    |
|                                                                                                                                        |
| [ViewData\[[\"progressBar\"]\] = pBar;]                                    |
|                                                                                                                                        |
| []                                                                                                 |
|                                                                                                                                        |
| [         [return] View();]                                                   |
|                                                                                                                                        |
| [ }]                                                                                               |
|                                                                                                                                        |
| []                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In View, invoke the ProgressBar helper with the control id and view data key as arguments.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    ] [\<%] [=] [ Html.MobSyncfusion().ProgressBar([\"pBar\"], [\"progressBar\"])[%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| ```                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| ```                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [\@{] []                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [               ] [Html.MobSyncfusion().ProgressBar([\"pBar\"], [\"progressBar\"])[.Render(); ]] |
|                                                                                                                                                                                                                                                              |
| [}] []                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application, the output will be as follows:

 

 

{border="0"}

Figure 91: Progressbar with Spinach Theme

 

{border="0"}

Figure 92: Progressbar with BlueLight Theme

 

{border="0"}

Figure 93: Progressbar with MetroBlue Theme

 

{border="0"}

Figure 94: Progressbar with DarkNight Theme

[]{#related-topics}

