---
title: howtochangethetextforalreadyassignedbannertextofacontrol.md
original_path: WinForms_Docs/99_Uncategorized/howtochangethetextforalreadyassignedbannertextofacontrol.md
created_at: 2025-08-05
---








  









### How to change the text for already assigned banner text of a control? {#how-to-change-the-text-for-already-assigned-banner-text-of-a-control style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This is done using the below code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                 |
| [BannerTextInfo ][info = ][bannerTextProvider1.GetBannerText(comboBoxAutoComplete1);[ // textbox is the control used for example]] |
|                                                                                                                                                                                                                                                                                                 |
| [info.Text = \"New Banner Text\";][]                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1205}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [Dim][ info [As] BannerTextInfo = bannerTextProvider1.GetBannerText(comboBoxAutoComplete1) [\' textbox is the control used for example]] |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [info.Text = [\"New Banner Text\"]][]                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note: Make sure you clear the default value of the Text property of the controls before setting the banner text.


 

[]{#related-topics}

