---
title: keystrokeactioncombinationsbinding.md
original_path: WinForms_Docs/03_Data_Binding/keystrokeactioncombinationsbinding.md
created_at: 2025-08-05
---








  









### Keystroke - Action Combinations Binding {#keystroke---action-combinations-binding style="tab-stops: 0pt"}

 

Edit Control offers support for the action-keystroke binding functionality, providing you the ability to perform advanced customization of action-keystroke bindings to suit your preferences. You can bind any desired keystroke combination to a standard (or custom) command like Copy, Cut, Paste or Find in the designer using the **Keys Binding** dialog as illustrated in the following procedure:

 

1.   In the Editor Keys Binding dialog box, select the desired standard command. The default shortcuts assigned for a particular command are listed in the combobox under the Shortcut(s) for selected command: label.

2.   Set the focus to the Edit Box Press TAB to navigate to the shortcuts drop-down list.

3.   Press the desired key or key combination.

4.   Now, click the Assign button, to assign this keystroke combination as the shortcut for that particular standard command. Click OK.

 

The **KeyBinder** property is used to get the key binder, and the **KeyBindingProcessor** property is used to get / set the key binding processor.

 

The Editor Keys Binding dialog is invoked using the **ShowKeysBindingEditor** method of the Edit Control.

 

The following illustration shows the Keys Binding dialog box.

 

{border="0"}

Figure 10: Preview of Keys Binding Dialog Box

 

You can also make use the **RegisteringKeyCommands** and **RegisteringDefaultKeyBindings** events to specify user-defined commands and bind the desired custom keystroke combinations to them.

 

This following code snippet registers the \"File.Open\" command and binds a Ctrl+O keystroke combination to it.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [// Invoke the Editor Keys Binding dialog.]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [this][.editControl1.ShowKeysBindingEditor();]                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [// Bind the action name to the action using the RegisteringKeyCommands and ProcessCommandEventHandler events.]                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [private][ [void] [this].editControl1_RegisteringKeyCommands([object] sender, [EventArgs] e)]        |
|                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [this][.editControl1.Commands.Add( [\"File.Open\"] ).ProcessCommand += [new] ProcessCommandEventHandler( Command_Open );]                    |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [// Bind key combinations to the action name using the RegisteringDefaultKeyBindings event.]                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| [private][ [void] [this].editControl1_RegisteringDefaultKeyBindings([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [this][.editControl1.KeyBinder.BindToCommand( [Keys].Control \| [Keys].O, [\"File.Open\"] );]                           |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [// Define the action that needs to be performed.]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [private][ [void] Command_Open()]                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [/\* Do the desired task. \*/]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Invoke the Editor Keys Binding dialog.]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.editControl1.ShowKeysBindingEditor()]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Bind the action name to the action using the RegisteringKeyCommands and ProcessCommandEventHandler events.]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][  [Sub] [Me].editControl1_RegisteringKeyCommands([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]        |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.editControl1.Commands.Add([\"File.Open\"]).ProcessCommand += [New] ProcessCommandEventHandler(Command_Open)]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Bind key combinations to the action name using the RegisteringDefaultKeyBindings event. ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][  [Sub] [Me].editControl1_RegisteringDefaultKeyBindings([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.editControl1.KeyBinder.BindToCommand(Keys.Control \| Keys.O, [\"File.Open\"])]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Define the action that needs to be performed.]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] Command_Open()]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Do the desired task.]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample which demonstrates Keys Binding is available in the following sample installation path.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Advanced Keyboard Interaction\\KeysBindingDemo***

[]{#p24}[] 

[]{#related-topics}

