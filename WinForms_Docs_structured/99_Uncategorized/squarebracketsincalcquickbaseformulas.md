---
title: squarebracketsincalcquickbaseformulas.md
original_path: WinForms_Docs/99_Uncategorized/squarebracketsincalcquickbaseformulas.md
created_at: 2025-08-05
---








  









### Square Brackets in CalcQuickBase Formulas {#square-brackets-in-calcquickbase-formulas style="tab-stops: 0pt"}

 

If you are using a **CalcQuickBase** object to add calculation support to your business object, then you must use strings as indexers on the CalcQuickBase instance to get and set values. These strings are referred to as the value\'s Name. If you need to use a Name in a formula, then you should enclose the string within brackets, \[ \]. In step three of the code below, four names A, B, C, and D are registered. Notice that the formula entered in step two uses the values from A and B by enclosing these names in brackets.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [// 1) Instantiates a CalcQuickBase object.]                                                                                               |
|                                                                                                                                                                                              |
| [calculator = ][New][ CalcQuickBase();] |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [// 2) Populate your controls.]                                                                                                            |
|                                                                                                                                                                                              |
| [this][.textBoxA.Text = [\"12\"];]                                               |
|                                                                                                                                                                                              |
| [this][.textBoxB.Text = [\"3\"];]                                                |
|                                                                                                                                                                                              |
| [this][.textBoxC.Text = [\"= \[A\] + 2 \* \[B\]\"];]                             |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [// Must enter formula names before turning on calculations.]                                                                              |
|                                                                                                                                                                                              |
| [// 3) Assigns formula object names.]                                                                                                      |
|                                                                                                                                                                                              |
| [calculator([\"A\"]) = [this].textBoxA.Text;]                                                                |
|                                                                                                                                                                                              |
| [calculator([\"B\"]) = [this].textBoxB.Text;]                                                                |
|                                                                                                                                                                                              |
| [calculator([\"C\"]) = [this].textBoxC.Text;]                                                                |
|                                                                                                                                                                                              |
| [calculator([\"D\"]) = [this].textBoxD.Text;]                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [\' 1) Instantiates a CalcQuickBase object.]                                                                                              |
|                                                                                                                                                                                             |
| [calculator = ][New][ CalcQuickBase()] |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [\' 2) Populate your controls.]                                                                                                           |
|                                                                                                                                                                                             |
| [Me][.textBoxA.Text = [\"12\"]]                                                 |
|                                                                                                                                                                                             |
| [Me][.textBoxB.Text = [\"3\"]]                                                  |
|                                                                                                                                                                                             |
| [Me][.textBoxC.Text = [\"= \[A\] + 2 \* \[B\]\"][   ] ]   |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [\' Must enter formula names before turning on calculations.]                                                                             |
|                                                                                                                                                                                             |
| [\' 3) Assigns formula object names.]                                                                                                     |
|                                                                                                                                                                                             |
| [calculator([\"A\"]) = [Me].textBoxA.Text]                                                                  |
|                                                                                                                                                                                             |
| [calculator([\"B\"]) = [Me].textBoxB.Text]                                                                  |
|                                                                                                                                                                                             |
| [calculator([\"C\"]) = [Me].textBoxC.Text]                                                                  |
|                                                                                                                                                                                             |
| [calculator([\"D\"]) = [Me].textBoxD.Text]                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p50} 

 

[]{#related-topics}

