---
title: clientsidemethods20.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsidemethods20.md
created_at: 2025-07-03
---






##### Client-side methods {#client-side-methods style="tab-stops: 0pt"}

+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| [Name] | Parameters                                                  | Return type | Description                                                                                                | Reference Link |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setValue                                   | **Value --** the value to be displayed in the progress bar. | NA          | Sets the value for the progress bar with the specified value.                                              | NA             |
|                                            |                                                             |             |                                                                                                            |                |
|                                            |                                                             |             |                                                                                                            |                |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setMinimum                                 | **Value --** the minimum value of progress bar.             | NA          | Sets the minimum value for the progress bar                                                                | NA             |
|                                            |                                                             |             |                                                                                                            |                |
|                                            |                                                             |             |                                                                                                            |                |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setMaximum                                 | **Value --** the maximum value of progress bar.             | NA          | Sets the maximum value for the progress bar                                                                | NA             |
|                                            |                                                             |             |                                                                                                            |                |
|                                            |                                                             |             |                                                                                                            |                |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setHeight                                  | **Value -** the height of the progress bar                  | NA          | Sets the height for the progress bar                                                                       | NA             |
|                                            |                                                             |             |                                                                                                            |                |
|                                            |                                                             |             |                                                                                                            |                |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setWidth                                   | **Value -** the width of the progress bar                   | NA          | Sets the width for the progress bar                                                                        | NA             |
|                                            |                                                             |             |                                                                                                            |                |
|                                            |                                                             |             |                                                                                                            |                |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| Disable                                    | NA                                                          | NA          | Disables the progress bar                                                                                  | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| Enable                                     | NA                                                          | NA          | Enable the progress bar                                                                                    | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| Reset                                      | NA                                                          | NA          | [Resets the progress bar value to zero.][] | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setBackgroundColor                         | **Color --** the background color of the substrate          | NA          | Change the background color of the substrate                                                               | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setBorderColor                             | **Color --** the border color of the substrate              | NA          | Change the border color of the substrate                                                                   | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setProgressBarColor                        | **Color --** the background color of the Progress bar.      | NA          | Change the color of the progress bar                                                                       | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setProgressBarBorderColor                  | **Color --** the border color of the Progress bar.          | NA          | Change the border color of the progress bar                                                                | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setProgressBarTextColor                    | **Color --** the text color of the Progress bar.            | NA          | Change the text color of the progress bar                                                                  | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setProgressBarTextFontSize                 | **FontSize --** the text size of the Progress bar.          | NA          | Change the text size of the progress bar                                                                   | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setProgressBarFontFamily                   | **FontFamily --** the font style of the Progress bar.       | NA          | Change the font family of the progress bar                                                                 | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setOrientation                             | **Orientation --** the orientation of the progressbar       | NA          | Change the orientation of the progress bar.                                                                | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+
| setStepValue                               | **Value --** the step increment value of the progress bar.  | NA          | Change the step increment value of the progress bar.                                                       | NA             |
+--------------------------------------------+-------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------+----------------+

 

**Using Builder**

The following steps guide in handling client side events through Builder:

1.  [In **View**, [invoke the ProgressBar helper with the **ProgressBar** **id** as the first argument.]][ ]

 

+-----------------------------------------------------------------------------------------------------------------------------+
| [\[View\]]                                                                        |
|                                                                                                                             |
| []                                                                                |
|                                                                                                                             |
| [\<%][{]                                                    |
|                                                                                                                             |
| [      Html.Syncfusion().ProgressBar(][\"Progress\"][)] |
|                                                                                                                             |
| [      .Value(50)]                                                                                    |
|                                                                                                                             |
| [      .Render();]                                                                                    |
|                                                                                                                             |
| [  } [%\>]]                                                               |
|                                                                                                                             |
| []                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                           |
|                                                                                                                                 |
| []                                                                                    |
|                                                                                                                                 |
| [\@{][] |
|                                                                                                                                 |
| [      Html.Syncfusion().ProgressBar(][\"Progress\"][)]     |
|                                                                                                                                 |
| [      .Value(50)]                                                                                        |
|                                                                                                                                 |
| [      .Render();]                                                                                        |
|                                                                                                                                 |
| [}][]   |
|                                                                                                                                 |
| []                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------+

2.  In JavaScript, use the methods as seen in the following code: 

  --------------------------------------------------------------------------
  [] 
  --------------------------------------------------------------------------

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javscript\]][ ]**[]                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [\<[script] [type]=\"text/javascript\"\>]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ ChangeBgColor(sender, args) {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newColor = args.get_text();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setBackgroundColor(newColor != ][\"\"][ && newColor != ][null][ ? newColor : ][\"\"][);]        |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ ChangeBorderColor(sender, args) {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newColor = args.get_text();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setBorderColor(newColor != ][\"\"][ && newColor != ][null][ ? newColor : ][\"\"][);]            |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ ChangeProgressBorderColor(sender, args) {]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newColor = args.get_text();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setProgressBarBorderColor(newColor != ][\"\"][ && newColor != ][null][ ? newColor : ][\"\"][);] |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ ChangeProgressBgColor(sender, args) {]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newColor = args.get_text();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setProgressBarColor(newColor != ][\"\"][ && newColor != ][null][ ? newColor : ][\"\"][);]       |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ ChangeFontColor(sender, args) {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newColor = args.get_text();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setProgressBarTextColor(newColor != ][\"\"][ && newColor != ][null][ ? newColor : ][\"\"][);]   |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ onValueChange(sender, args) {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newValue = args.get_value();]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setValue(newValue != ][\"\"][ && newValue != ][null][ ? newValue : ][\"\"][);]                  |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [function][ onWidthValueChange(sender, args) {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newWidth = args.get_value();]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setWidth(newWidth != ][\"\"][ && newWidth != ][null][ ? newWidth : ][\"\"][);]                  |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ onHeightValueChange(sender, args) {]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newHeight = args.get_value();]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setHeight(newHeight != ][\"\"][ && newHeight != ][null][ ? newHeight : ][\"\"][);]              |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ onStepValueChange(sender, args) {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newStep = args.get_value();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setStepValue(newStep != ][\"\"][ && newStep != ][null][ ? newStep : ][\"\"][);]                 |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [function][ onMaximumValueChange(sender, args) {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newMaximum = args.get_value();]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setMaximum(newMaximum != ][\"\"][ && newMaximum != ][null][ ? newMaximum : ][\"\"][);]          |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [function][ onMinimumValueChange(sender, args) {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newMinimum = args.get_value();]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setMinimum(newMinimum != ][\"\"][ && newMinimum != ][null][ ? newMinimum : ][\"\"][);]          |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [function][ onFontSizeChange(sender, args) {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newSize = args.get_value();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setProgressBarTextFontSize(newSize != ][\"\"][ && newSize != ][null][ ? newSize : ][\"\"][);]   |
|                                                                                                                                                                                                                                                                             |
| [} ]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [\$(][\"#EnableDisable\"][).bind(][\'click\'][, ][function][ () {]                                               |
|                                                                                                                                                                                                                                                                             |
| [        progressBar = \$find(][Progress][);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [        ][if][ (\$(][\"#EnableDisable\"][).is(][\":checked\"][))      ]                                         |
|                                                                                                                                                                                                                                                                             |
| [            progressBar.Enable();]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [        ][else][       ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [            progressBar.Disable();]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    });]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [    \$(][\'#Orientation\'][).bind(][\'change\'][, ][function][ () {]                                            |
|                                                                                                                                                                                                                                                                             |
| [        ][var][ orientation = ][this][.value;]                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| [       progressBar = \$find(][Progress][);]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                             |
| [        progressOrientation = orientation;]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| [        progressBar.setOrientation(orientation);]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [    });]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [    \$(][\'#FontFamily\'][).bind(][\'change\'][, ][function][ () {]                                             |
|                                                                                                                                                                                                                                                                             |
| [        ][var][ fontFamily = ][this][.value;]                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [        progressBar = \$find(][Progress][);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [        progressBar.setProgressBarFontFamily(fontFamily);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [    });]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| [      [\</]script[\>]]                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Using Properties model**

1.   [In Controller, create an object for the **ProgressBarModel** class. Assign this model class to view data.][ ]

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                               |
| [public][ [ActionResult] Index()]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                               |
| [{[                       ][ProgressBarPropertiesModel][ model = ][new][ ][ProgressBarPropertiesModel][();]] |
|                                                                                                                                                                                                                                                                                                               |
| [        model.Value=50;]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                               |
|   ViewData\[[\"Progress\"]\] = [model];                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                               |
|   [return] View();                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                               |
|  }                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In View, invoke the ProgressBar helper with the view data key as the control ID

 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[View\]]**                                                                          |
|                                                                                                                             |
| [\<%][{]                                                    |
|                                                                                                                             |
| [      Html.Syncfusion().ProgressBar(][\"Progress\"][)] |
|                                                                                                                             |
| [      .Render();]                                                                                    |
|                                                                                                                             |
| [  } [%\>]]                                                               |
|                                                                                                                             |
| []                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                            |
|                                                                                                                                  |
| []                                                                                     |
|                                                                                                                                  |
| [\@{][   ] |
|                                                                                                                                  |
| [      Html.Syncfusion().ProgressBar(][\"Progress\"][)]      |
|                                                                                                                                  |
| [      .Render();]                                                                                         |
|                                                                                                                                  |
| [}][]    |
|                                                                                                                                  |
| []                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------+

 

3.   In JavaScript, use the methods as seen in the following code: 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javscript\]][ ]**[]                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [\<[script] [type]=\"text/javascript\"\>]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ ChangeBgColor(sender, args) {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newColor = args.get_text();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setBackgroundColor(newColor != ][\"\"][ && newColor != ][null][ ? newColor : ][\"\"][);]        |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ ChangeBorderColor(sender, args) {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newColor = args.get_text();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setBorderColor(newColor != ][\"\"][ && newColor != ][null][ ? newColor : ][\"\"][);]            |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ ChangeProgressBorderColor(sender, args) {]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newColor = args.get_text();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setProgressBarBorderColor(newColor != ][\"\"][ && newColor != ][null][ ? newColor : ][\"\"][);] |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ ChangeProgressBgColor(sender, args) {]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newColor = args.get_text();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setProgressBarColor(newColor != ][\"\"][ && newColor != ][null][ ? newColor : ][\"\"][);]       |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ ChangeFontColor(sender, args) {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newColor = args.get_text();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setProgressBarTextColor(newColor != ][\"\"][ && newColor != ][null][ ? newColor : ][\"\"][);]   |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ onValueChange(sender, args) {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newValue = args.get_value();]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setValue(newValue != ][\"\"][ && newValue != ][null][ ? newValue : ][\"\"][);]                  |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [function][ onWidthValueChange(sender, args) {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newWidth = args.get_value();]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setWidth(newWidth != ][\"\"][ && newWidth != ][null][ ? newWidth : ][\"\"][);]                  |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ onHeightValueChange(sender, args) {]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newHeight = args.get_value();]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setHeight(newHeight != ][\"\"][ && newHeight != ][null][ ? newHeight : ][\"\"][);]              |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [function][ onStepValueChange(sender, args) {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newStep = args.get_value();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setStepValue(newStep != ][\"\"][ && newStep != ][null][ ? newStep : ][\"\"][);]                 |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [function][ onMaximumValueChange(sender, args) {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newMaximum = args.get_value();]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setMaximum(newMaximum != ][\"\"][ && newMaximum != ][null][ ? newMaximum : ][\"\"][);]          |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [function][ onMinimumValueChange(sender, args) {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newMinimum = args.get_value();]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setMinimum(newMinimum != ][\"\"][ && newMinimum != ][null][ ? newMinimum : ][\"\"][);]          |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [function][ onFontSizeChange(sender, args) {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [    progressBar = \$find(][Progress][);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    ][var][ newSize = args.get_value();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    progressBar.setProgressBarTextFontSize(newSize != ][\"\"][ && newSize != ][null][ ? newSize : ][\"\"][);]   |
|                                                                                                                                                                                                                                                                             |
| [} ]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [\$(][\"#EnableDisable\"][).bind(][\'click\'][, ][function][ () {]                                               |
|                                                                                                                                                                                                                                                                             |
| [        progressBar = \$find(][Progress][);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [        ][if][ (\$(][\"#EnableDisable\"][).is(][\":checked\"][))      ]                                         |
|                                                                                                                                                                                                                                                                             |
| [            progressBar.Enable();]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [        ][else][       ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [            progressBar.Disable();]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [    });]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [    \$(][\'#Orientation\'][).bind(][\'change\'][, ][function][ () {]                                            |
|                                                                                                                                                                                                                                                                             |
| [        ][var][ orientation = ][this][.value;]                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| [       progressBar = \$find(][Progress][);]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                             |
| [        progressOrientation = orientation;]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| [        progressBar.setOrientation(orientation);]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [    });]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [    \$(][\'#FontFamily\'][).bind(][\'change\'][, ][function][ () {]                                             |
|                                                                                                                                                                                                                                                                             |
| [        ][var][ fontFamily = ][this][.value;]                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [        progressBar = \$find(][Progress][);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [        progressBar.setProgressBarFontFamily(fontFamily);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [    });]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| [      [\</]script[\>]]                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

