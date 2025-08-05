---
title: addingjavascripts.md
original_path: WinForms_Docs/99_Uncategorized/addingjavascripts.md
created_at: 2025-08-05
---








  









### Adding Java Scripts {#adding-java-scripts style="tab-stops: 0pt"}

To add Java scripts:

5.   On the ***Solution Explorer***, double-click ***Views*** folder, double-click the shared folder, and then double-click ***Site.Master*** file.

{border="0"}

Figure 41: Site.Master file displayed under the Shared Folder

[] 

The **Site.Master** page appears as shown in the following screenshot.

{border="0"}

Figure 42: Site.Master Page

6.   On the ***Solution Explorer****,* click ***Javascripts*** folder. The lists of scripts available are displayed.

{border="0"}

Figure 43: List of scripts displayed under the Javascripts Folder

7.   Import the following javascript files onto the Site.Master page.

[·      ]jquery-1.4.1.min.js

[·    ]MicrosoftAjax.js[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Site.Master\] ]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][head][ [runat][=\"server\"\>]]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][script][ [src][=\"][\<%][=] Url.Content(\"\~/Javascripts/jquery-1.4.1.min.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][script][ [src][=\"][\<%][=] Url.Content(\"\~/Javascripts/MicrosoftAjax.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [     ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][head][\>]                                                                                                                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

