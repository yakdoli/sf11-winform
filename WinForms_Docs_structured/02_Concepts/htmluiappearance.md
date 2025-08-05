---
title: htmluiappearance.md
original_path: WinForms_Docs/02_Concepts/htmluiappearance.md
created_at: 2025-08-05
---








  









## HTMLUI Appearance {#htmlui-appearance style="tab-stops: 0pt"}

[[[]]]{.underline} 

With HTMLUI, the application developer can decide the appearance of his application even at run time by setting the style according to his needs. A common application is changing the background color for a particular page based on the user signing in. These interactive applications help in developing user-friendly applications.

The HTMLUI control allows the following modes of changing the background color to your application.

[] 

[·      ]Inside the HTML document as Attribute

[·      ]Using the Style Sheets

[] 

The following HTML coding shows the different methods of changing the background color that HTMLUI control supports, leaving it to the user to choose the best among the various options as per the requirements.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[HTML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][html][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][head][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][link][ ][type][=\"text/css\" ][rel][=\"stylesheet\" ][href][=\"backgroundColor.CSS\"\>\<][/link][\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][style][\>.div{\"background-color: #ffffcc;\"}\<][/style][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][/head][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][body][ ][bgcolor][=\"#dae5f5\"\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][p][ ][style][=\"background-color: #ffffff;\"][\>Background color changed through the style attribute[\<][/p][\>]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][/body][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][/html][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following figure shows the backcolor of the HTML document customized by using HTMLUI.

 

{border="0"}

 

[]{#p161}Figure 42: Background Color of the HTML document customized by using the HTMLUI Control

 

More:





