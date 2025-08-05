---
title: addingscripts6.md
original_path: WinForms_Docs/99_Uncategorized/addingscripts6.md
created_at: 2025-08-05
---








  









### Adding Scripts {#adding-scripts style="tab-stops: 0pt"}

The steps to add scripts are as follows:

1.   On the **Solution Explorer**, double-click the **Views** folder, double-click the **Shared** folder, and then double-click the **\_Layout.cshtml** file.[ ]The \_layout.cshtml page appears.

                      {border="0"}

Figure 52_Layout.cshtml file displayed under the Shared folder

{border="0"}

 

Figure 533: \_Layout.cshtml page

9.   On the Solution Explorer, click the **Scripts** folder. The lists of scripts available are displayed.

{border="0"}

Figure 54: List of scripts displayed under the Scripts folder 

10.  Import the following javascript files onto the \_Layout.cshtml page:

 

[·      ]jquery-1.4.1.min.js

[·      ]MicrosoftAjax.js

[·      ]MicrosoftMvcAjax.debug.js

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[\_Layout.cshtml\] ]**[]                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][head][ [runat][=\"server\"\>]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [     [\<][script] [src][=\"][@]Url.Content(\"\~/Scripts/jquery-1.4.1.min.js\")[\"] [type][=\"text/javascript\"\>\</][script][\>]]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [     [\<][script] [src][=\"][@]Url.Content(\"\~/Scripts/MicrosoftAjax.js\")[\"] [type][=\"text/javascript\"\>\</][script][\>]]                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [     [\<][script] [src][=\"][@]Url.Content(\"\~/Scripts/][ MicrosoftMvcAjax.debug.js][ \")[\"] [type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][head][\>]                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

[]{#related-topics}

