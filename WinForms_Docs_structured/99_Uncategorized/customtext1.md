---
title: customtext1.md
original_path: WinForms_Docs/99_Uncategorized/customtext1.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### CustomText {#customtext style="tab-stops: 0pt"}

This feature allows the user to customize the display text of the Progress Bar. You can set the custom text that will display when the progress bar shows different levels of progress.

+-----------------+------------------------------------------------------------+------------------+------------------+-------------+
| Name            | Description                                                | Type of property | Value it accepts | Dependency  |
+-----------------+------------------------------------------------------------+------------------+------------------+-------------+
| AllowCustomText | Sets the whether the custom text will be displayed or not. | bool             | True/            | NA          |
|                 |                                                            |                  |                  |             |
|                 |                                                            |                  | False            |             |
+-----------------+------------------------------------------------------------+------------------+------------------+-------------+

 

The following steps guide you to customize the display text of the progress bar.

1.   In View, invoke the ProgressBar helper with the ProgressBar id as the first argument and set the AllowCustomText() method with the desired value as an argument. 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                              |
|                                                                                                                                                                                 |
| [\<%] [Html.MobSyncfusion().ProgressBar([\"progressBar\"])] |
|                                                                                                                                                                                 |
| [       .Value(30)]                                                                                                                         |
|                                                                                                                                                                                 |
| [       **.AllowCustomText(true)**]                                                                                                         |
|                                                                                                                                                                                 |
| **[       .ClientSideOnCustomTextRendering([\"onCustomText\"])]**                                                   |
|                                                                                                                                                                                 |
| [      .Render();]                                                                                                                          |
|                                                                                                                                                                                 |
| [    [%\>]]                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                          |
|                                                                                                                                                                              |
| [ [\@{]]                                                                                       |
|                                                                                                                                                                              |
| [      ] [Html.MobSyncfusion().ProgressBar([\"progressBar\"])] |
|                                                                                                                                                                              |
| [       .Value(30)]                                                                                                                      |
|                                                                                                                                                                              |
| [       **.AllowCustomText(true)**]                                                                                                      |
|                                                                                                                                                                              |
| **[       .ClientSideOnCustomTextRendering([\"onCustomText\"])]**                                                |
|                                                                                                                                                                              |
| [      .Render();]                                                                                                                       |
|                                                                                                                                                                              |
| [ }] []                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.  [Define the custom text handler in view.]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| **[\[Javascript\]]** []                                                                                                                       |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| [        [function] onCustomText(progressBar, currentValue) {]                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            [var] context = currentValue.Context;]                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [            [var] text = currentValue.Text;]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            [var] textwidth = 131;]                                                                                                                                      |
|                                                                                                                                                                                                                                    |
| [            [var] ang = 270;]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            [var] fontsize = 22, progressOrientation = [null] ;]                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [if] (progressOrientation == [null])]                                                                                                   |
|                                                                                                                                                                                                                                    |
| [                progressOrientation = [\"horizontal\"];]                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            context.save();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [            [if] (progressOrientation == [\"horizontal\"]) {]                                                                                     |
|                                                                                                                                                                                                                                    |
| [                [var] textx = currentValue.OffsetX + currentValue.Width / 2 - textwidth / 2;]                                                                            |
|                                                                                                                                                                                                                                    |
| [                context.fillText(text, textx, currentValue.Height / 2 + currentValue.OffsetY + currentValue.Radius / 2);]                                                                     |
|                                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [else] {]                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [                [var] textx = currentValue.Width / 2 - currentValue.Radius / 2 + currentValue.OffsetX;]                                                                  |
|                                                                                                                                                                                                                                    |
| [                context.fillText(text, fontsize, textx, currentValue.OffsetX + currentValue.Height / 2, [\"\"] + ang);]                                                |
|                                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [            context.restore();]                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [    [\</][script][\>]]                                                                                                       |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

 

{border="0"}

Figure 89: Progressbar

 

[]{#related-topics}

