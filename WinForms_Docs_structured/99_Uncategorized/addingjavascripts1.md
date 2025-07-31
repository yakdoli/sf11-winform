---
title: addingjavascripts1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingjavascripts1.md
created_at: 2025-07-03
---








  









### Adding Java Scripts {#adding-java-scripts style="tab-stops: 0pt"}

To add Java scripts:

1.   In the ***Solution Explorer***, double-click ***Views*** \> ***Shared folder*** \> ***Layout.cshtml*** file.

 

 

 

 

{border="0"}

*[Figure ][48][: \_Layout.cshtml][ file displayed under the Shared Folder]*

[] 

2.   The **Layout.cshtml** page opens.

{border="0"}

*[Figure ][49][:\_Layout.cshtml Page]*

[[]]{.underline} 

3.  On the ***Solution Explorer****,* click ***Javascripts*** folder. The lists of scripts available are displayed.

{border="0"}

*[Figure ][50][: ][List of scripts displayed under the Javascripts Folder]*

*[]* 

4.  Import the following javascript files onto the Site.Master page.

[·      ]jquery-1.4.1.min.js

[·      ]MicrosoftAjax.js

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[\_Layout.cshtml\] ]**[]                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][head][ [runat][=\"server\"\>]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [     [\<][script] [src][=\"]][@][Url.Content(\"\~/Scripts/jquery-1.4.1.min.js\")[\"] [type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [     [\<][script] [src][=\"]][@][Url.Content(\"\~/Scripts/MicrosoftAjax.js\")[\"] [type][=\"text/javascript\"\>\</][script][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [     ]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][head][\>]                                                                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

