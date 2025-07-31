---
title: addingjavascripts3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingjavascripts3.md
created_at: 2025-07-03
---








  









### [Addi]{.ughyperlink}ng JavaScripts {#adding-javascripts style="tab-stops: 0pt"}

To add JavaScripts:

1.  On the **Solution Explorer**, double-click the **Views** folder, double-click the **Shared** folder, and then double-click the **\_Layout.cshtml** file.

 

{border="0"}

Figure 28: \_Layout.cshtml File Displayed under the Shared Folder

 The **\_Layout.cshtml** page appears as shown in the following screenshot.

{border="0"}

Figure 29: Site.Master Page

2.  On the **Solution Explorer***,* click the **Scripts** folder. The lists of scripts available are displayed.

{border="0"}

Figure 30: List of Scripts Displayed under the Scripts Folder

3.  Import the following javascript files onto the Site.Master page.

[•   ][jquery-1.5.1.min.js]

[•   ][MicrosoftAjax.js]

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\] ]**                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][head][ [runat][=\"server\"\>]]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<][script] [src][=\"][@][Url.Content(][\"\~/Scripts/jquery-1.5.1.min.js\"][)\"] [type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ]                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [     ]                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\</][head][\>][]                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

