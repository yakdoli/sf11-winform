---
title: addingjavascripts4.md
original_path: WinForms_Docs/99_Uncategorized/addingjavascripts4.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Adding Java Scripts {#adding-java-scripts style="TEXT-INDENT: -36pt; MARGIN-LEFT: 36pt; tab-stops: 36.0pt"}

To add Java scripts:

1.   On the ***Solution Explorer***, double-click ***Views*** folder, double-click the shared folder, and then double-click ***Site.Master*** file.

{border="0"}

Figure 21: Site.Master file displayed under the Shared Folder

[] 

The **Site.Master** page appears as shown in the following screenshot.

{border="0"}

Figure 22: Site.Master Page

2.   On the ***Solution Explorer****,* click ***Javascripts*** folder. The lists of scripts available are displayed.

{border="0"}

Figure 23: List of scripts displayed under the Javascripts Folder

3.   Import the following javascript files onto the Site.Master page.

[·      ]jquery-1.4.1.min.js

[·    ]MicrosoftAjax.js[]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\] ]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<] [head] [ [runat] [=\"server\"\>] ]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<] [script] [ [src] [=\"] [\<%] [=] Url.Content(\"\~/Javascripts/jquery-1.4.1.min.js\") [%\>][\"][type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<] [script] [ [src] [=\"] [\<%] [=] Url.Content(\"\~/Javascripts/MicrosoftAjax.js\") [%\>][\"][type][=\"text/javascript\"\>\</][script][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [     ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</] [head] [\>]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[\[Razor\] ]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<] [head] [ [runat] [=\"server\"\>] ]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [\<][script][src][=\"][@][Url.Content(][\"\~/Scripts/jquery-1.4.1.min.js\"][)\"][type][=\"text/javascript\"\>\</][script][\>]]                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [\<][script][src][=\"][@][Url.Content(][\"\~/Scripts/MicrosoftAjax.js\"][)\"][type][=\"text/javascript\"\>\</][script][\>]]                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [     ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</] [head] [\>]                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

