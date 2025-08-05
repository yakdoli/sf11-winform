---
title: addingjavascripts2.md
original_path: WinForms_Docs/99_Uncategorized/addingjavascripts2.md
created_at: 2025-08-05
---








  









### Adding Java Scripts {#adding-java-scripts style="tab-stops: 0pt"}

To add JavaScripts:

1.  On the ***Solution Explorer***, double-click ***Views*** folder, double-click the shared folder, and then double-click ***Site.Master*** file.

{border="0"}

Figure 19: Site.Master File Displayed under the Shared Folder

 

The **Site.Master** page appears as shown in the following screenshot.

{border="0"}

Figure 20: Site.Master Page

2.  On the **Solution Explorer***,* click the **Javascripts** folder. The lists of available scripts is displayed.

{border="0"}

Figure 21: List of Scripts Displayed under the Scripts Folder

3.  Import the following JavaScript files onto the Site.Master page:

[•   ]jquery-1.5.1.min.js

[•   ]MicrosoftAjax.js

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\] ]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][head][ [runat][=\"server\"\>]]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][script][ [src][=\"][\<%][=] Url.Content(\"\~/Javascripts/jquery-1.5.1.min.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [     ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][head][\>][]                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

