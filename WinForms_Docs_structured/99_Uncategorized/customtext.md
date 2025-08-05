---
title: customtext.md
original_path: WinForms_Docs/99_Uncategorized/customtext.md
created_at: 2025-08-05
---






#### Custom Text {#custom-text style="tab-stops: 0pt"}

You can set the custom text that will display when the progress bar shows different levels of progress, using the following code.\
There are two ways in which you can set the orientation of the Progress bar, both of which use properties from the [properties table].

Using Builder

1.   In **View**, invoke the ProgressBar helper with the control ID as an argument, followed by the Custom text method, with the desired text as an argument.

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                           |
|                                                                                                                          |
| []                                                               |
|                                                                                                                          |
| [\<%][{]                     |
|                                                                                                                          |
| [      Html.Syncfusion().ProgressBar([\"Progress\"])]        |
|                                                                                                                          |
| [      .AllowCustomText([true])]                                |
|                                                                                                                          |
| [      .ClientSideOnCustomTextRendering([\"onCustomText\"])] |
|                                                                                                                          |
| [      .Render();]                                                                   |
|                                                                                                                          |
| [  } [%\>]]                                              |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                                                                                                                |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                      |
| [\@{][]                                                                                      |
|                                                                                                                                                                                                                      |
| [    Html.Syncfusion().ProgressBar(][\"Progress\"][)]        |
|                                                                                                                                                                                                                      |
| [    .Height(22)]                                                                                                                                                  |
|                                                                                                                                                                                                                      |
| [    .Width(700)]                                                                                                                                                  |
|                                                                                                                                                                                                                      |
| [    .Value(50)]                                                                                                                                                   |
|                                                                                                                                                                                                                      |
| [    .AllowCustomText(][true][)]                                |
|                                                                                                                                                                                                                      |
| [    .Orientation(][ProgressBarOrientation][.Horizontal)]    |
|                                                                                                                                                                                                                      |
| [    .Minimum(10)]                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [    .Maximum(100)    ]                                                                                                                                            |
|                                                                                                                                                                                                                      |
| [    .ClientSideOnCustomTextRendering(][\"onCustomText\"][)] |
|                                                                                                                                                                                                                      |
| [    .Render();]                                                                                                                                                   |
|                                                                                                                                                                                                                      |
| [}][]                                                                                        |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In Javascript, define the handler as shown below:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                            |
|                                                                                                                                                                                            |
| \[Javascript\]                                                                                                                                                                             |
|                                                                                                                                                                                            |
| \<[script] [type]=\"text/javascript\"\>[]                                                                                  |
|                                                                                                                                                                                            |
| [function][ onCustomText(progressBar, currentValue) {]                                                                                          |
|                                                                                                                                                                                            |
| [     ][var][ context = currentValue.\_Context;]                                                                          |
|                                                                                                                                                                                            |
| [    ][var][ text;]                                                                                                       |
|                                                                                                                                                                                            |
| [    ][if][ (progressBar == ][null][)]                                         |
|                                                                                                                                                                                            |
| [        progressBar = \$find(controlId);]                                                                                                                           |
|                                                                                                                                                                                            |
| [    ][/// adding the custom text with the progressbar value  ][]                                                    |
|                                                                                                                                                                                            |
| [    text = currentValue.\_Value + ][\"% of 100GB Completed\"][;]                                                       |
|                                                                                                                                                                                            |
| [    ][var][ text_width = context.measureText(text).width;]                                                               |
|                                                                                                                                                                                            |
| [    ][/// we must set this angle then only the text is aligned properly when we set the Orientation as Vertical][]  |
|                                                                                                                                                                                            |
| [    ][///The user must define the font size]                                                                                              |
|                                                                                                                                                                                            |
| [   /// This is the simple example for how to calculate the width, text_x value.][ ]                                                       |
|                                                                                                                                                                                            |
| [    ][var][ ang = 270;]                                                                                                  |
|                                                                                                                                                                                            |
| [    ][var][ fontsize = 22;]                                                                                              |
|                                                                                                                                                                                            |
| [    ][if][ (progressOrientation == ][null][)]                                 |
|                                                                                                                                                                                            |
| [        progressOrientation = ][\"horizontal\"][;]                                                                     |
|                                                                                                                                                                                            |
| [    context.save();]                                                                                                                                                |
|                                                                                                                                                                                            |
| [    ][if][ (progressOrientation == ][\"horizontal\"][) {]                   |
|                                                                                                                                                                                            |
| [        ][var][ text_x = currentValue.\_OffsetX + currentValue.\_Width / 2 - text_width / 2;]                            |
|                                                                                                                                                                                            |
| [        context.fillText(text, text_x, currentValue.\_Height / 2 + currentValue.\_OffsetY + currentValue.\_Radius / 2);]                                            |
|                                                                                                                                                                                            |
| [    }]                                                                                                                                                              |
|                                                                                                                                                                                            |
| [    ][else][ {]                                                                                                          |
|                                                                                                                                                                                            |
| [        ][var][ text_x = currentValue.\_Width / 2 - currentValue.\_Radius / 2 + currentValue.\_OffsetX;]                 |
|                                                                                                                                                                                            |
| [        context.fillText(text, fontsize, text_x, currentValue.\_OffsetX + currentValue.\_Height / 2, ][\"\"][ + ang);] |
|                                                                                                                                                                                            |
| [    }]                                                                                                                                                              |
|                                                                                                                                                                                            |
| [    context.restore();]                                                                                                                                             |
|                                                                                                                                                                                            |
| [ }  ]                                                                                                                                                               |
|                                                                                                                                                                                            |
| [\</[script\>][                  ]]                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   Build and run the application.

 

Using PropertiesModel

1.   In the controller, create an instance of the ProgressBarPropertiesModel.

2.   Define the Custom text property and pass the instance through the view-specific data to the view.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[controller\]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                       |
| [public][ ActionResult Index()]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                       |
| [{  ]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                       |
| [                        ][ProgressBarPropertiesModel[ model = ][new][ ]ProgressBarPropertiesModel[();]] |
|                                                                                                                                                                                                                                                                                       |
| [model.AllowCustomText = [true];]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                       |
| [model.ClientSideOnCustomTextRendering = [\" onCustomText \"];]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                       |
| [            ViewData\[[\"Progress\"]\] = [model];]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                       |
| [            [return] View();]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                       |
| [ }]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In View, invoke the ProgressBar helper with the view data key as the control ID.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[View\]]**                                                                                                                                                         |
|                                                                                                                                                                                                            |
| [    [\<%]{ Html.Syncfusion().ProgressBar(][\"Progress\"][).Render(); } [%\>]] |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                                                                                                  |
|                                                                                                                                                                                                        |
| []                                                                                                                                                           |
|                                                                                                                                                                                                        |
| [\@{][]                                                                        |
|                                                                                                                                                                                                        |
| [      ][Html.Syncfusion().ProgressBar(][\"Progress\"][)] |
|                                                                                                                                                                                                        |
| [     .Render();]                                                                                                                                               |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [}][]                                                                          |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   In Javascript, define the handler as shown below:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| \[Javascript\]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| \<[script] [type]=\"text/javascript\"\>[]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [function][ onCustomText(progressBar, currentValue) {]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [     ][var][ context = currentValue.\_Context;]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [    ][var][ text;]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [    ][if][ (progressBar == ][null][)]                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [        progressBar = \$find(controlId);]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| [    ][/// adding the custom text with the progressbar value  ][]                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [    text = currentValue.\_Value + ][\"% of 100GB Completed\"][;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [    ][var][ text_width = context.measureText(text).width;]                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [    ][/// we must set this angle then only the text is aligned properly when we set the Orientation as Vertical][]                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [    ][///The user must define the font size]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [   /// This is the simple example for how to calculate the width, text_x value.][ ]                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [    ][var][ ang = 270;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [    ][var][ fontsize = 22;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [    ][if][ (progressOrientation == ][null][)]                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [        progressOrientation = ][\"horizontal\"][;]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [    context.save();]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [       if][ (progressOrientation == ][\"horizontal\"][) {]                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [         var][ text_x = currentValue.\_OffsetX + currentValue.\_Width / 2 -          text_width / 2;          context.fillText(text, text_x, currentValue.\_Height / 2 + currentValue.\_OffsetY + currentValue.\_Radius / 2);] |
|                                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [    ][else][ {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [        ][var][ text_x = currentValue.\_Width / 2 -        currentValue.\_Radius / 2 + currentValue.\_OffsetX;]                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [        context.fillText(text, fontsize, text_x, currentValue.\_OffsetX + currentValue.\_Height / 2, ][\"\"][ + ang);]                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [    context.restore();]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [ }  ]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [\</[script\>][                  ]]                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   Build and run the application, the output will be as follows:

 

{border="0"}

Figure 174: Custom Text in Progress Bar**[]**

 

[]{#related-topics}

