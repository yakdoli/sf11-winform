---
title: textmaskformat1.md
original_path: WinForms_Docs/99_Uncategorized/textmaskformat1.md
created_at: 2025-08-05
---






##### TextMaskFormat {#textmaskformat style="tab-stops: 0pt"}

  Details

Old:

[                        ]The text inside the **MaskedTextBox** was the output.

                        Example: When the Mask string is **(00)-(000).(0)**

                        And the user inputs 1, the output will be **(1\_)-(\_\_\_).(\_)**

[            ]New:

[                        ]The text inside the **MaskedTextBox** is formatted and given as the output.

                        There are four formatting properties and it is an enum. they are,

1)         ExcludePromptAndLiterals

2)         IncludeLiterals

           3)      IncludePrompt

           4)      IncludePromptAndLiterals

[] 

Example: When the Mask string is (00)-(000). (0)

And the user inputs 1, the output Text will be

1\) ExcludePromptAndLiterals                    -           1

2\) IncludeLiterals                           -           (1)-(). ()

3\) IncludePrompt                          -           1\_\_\_\_\_

4\) IncludePromptAndLiterals                      -           (1\_)-(\_\_\_). (\_)

**[]** 

IncludePromptAndLiterals is enabled by default.

Usage

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][MaskedTextBox][ Name][=\"maskedtextBox1\"][ TextMaskFormat][=\"ExcludePromptAndLiterals\" /\>] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                                 |
| [MaskedTextBox][ maskedTextBox = [new] [MaskedTextBox]();] |
|                                                                                                                                                                                                 |
| [maskedTextBox.TextMaskFormat = [MaskFormat].ExcludePromptAndLiterals;]                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

