---
title: howtodynamicallyvalidatetextusingthetextchangedevent.md
original_path: WinForms_Docs/99_Uncategorized/howtodynamicallyvalidatetextusingthetextchangedevent.md
created_at: 2025-08-05
---








  









## How To Dynamically Validate Text Using the TextChanged Event {#how-to-dynamically-validate-text-using-the-textchanged-event style="tab-stops: 0pt"}

[] 

Text can be validated dynamically by using the **TextChanged** event and a Timer. The validation routine is invoked in response to a brief pause by the user while typing. The following code snippet illustrates this.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [private][ [void] editControl1_TextChanged([object] sender, System.[EventArgs] e) ] |
|                                                                                                                                                                                                                                         |
| [{ ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [    [// Do not start the timer as long as characters are being typed. ]]                                                                                                     |
|                                                                                                                                                                                                                                         |
| [    [if] ([this].timer1.Enabled == [true]) { ]                                                                                      |
|                                                                                                                                                                                                                                         |
| [        [this].timer1.Stop(); ]                                                                                                                                               |
|                                                                                                                                                                                                                                         |
| [    } ]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| [    [this].timer1.Start(); ]                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [} ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [private][ [void] timer1_Tick([object] sender, System.[EventArgs] e) ]              |
|                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [    [this].ValidateText();]                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [    ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [    [this].timer1.Stop(); ]                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [} ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [private][ [void] ValidateText() ]                                                                                            |
|                                                                                                                                                                                                                                         |
| [{ ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [    [// Perform your validation logic here. ]]                                                                                                                               |
|                                                                                                                                                                                                                                         |
| [    [MessageBox].Show([\" Text Validated \"]);]                                                                                                        |
|                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] editControl1_TextChanged([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] EditControl1.TextChanged] |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Do not start the timer as long as characters are being typed.]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [If][ [Me].timer1.Enabled = [True] [Then]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.timer1.Stop()]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [If]]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.timer1.Start()]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] timer1_Tick([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] timer1.Tick]                           |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.ValidateText()]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.timer1.Stop()]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] ValidateText()]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Perform your validation logic here.]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [MessageBox.Show([\" Text validated \"])]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p190} 

[]{#related-topics}

