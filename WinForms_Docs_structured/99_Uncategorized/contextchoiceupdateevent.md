---
title: contextchoiceupdateevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\contextchoiceupdateevent.md
created_at: 2025-07-03
---






#### ContextChoiceUpdate Event {#contextchoiceupdate-event style="tab-stops: 0pt"}

 

This event occurs when the context choice list is updated.

 

The event handler receives an argument of type **IContextChoiceController**. The following IContextChoiceController members provide information specific to this event.

 


  ---------------------------- ----------------------------------------------------------------------------------------
  Member                       Description
  Dropper                      Gets / sets dropping lexem.
  ExtendItemsFilteringString   Specifies whether autocomplete string should be extended.
  FormSize                     Gets / sets size of the context choice form.
  Images                       Gets collection of the INamedImage items.
  IsVisible                    Specifies whether context choice window associated with current controller is visible.
  Items                        Gets collection of the context choice items.
  LexemBeforeDropper           Gets / sets lexem situated before dropper.
  SelectedItem                 Gets / sets currently selected item.
  UseAutocomplete              Specifies whether autocomplete technique should be used with current context choice.
  ---------------------------- ----------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [// Create a new instance of the context choice item collection.]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [private][ [ContextChoiceItemCollection] c = [new] [ContextChoiceItemCollection]();]                                                               |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [// Handle the ContextChoiceUpdate event.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                        |
| [this][.editControl1.ContextChoiceUpdate+=[new] Syncfusion.Windows.Forms.Edit.[ContextChoiceEventHandler](editControl1_ContextChoiceUpdate);]                           |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [// IContextChoiceController.LexemBeforeDropper property returns the lexem before the dropper which displays the context choice. It is possible to control the lexem being searched in the context choice list using the ContextChoiceUpdate event.] |
|                                                                                                                                                                                                                                                                                                        |
| [private][ [void] editControl1_ContextChoiceUpdate(Syncfusion.Windows.Forms.Edit.Interfaces.[IContextChoiceController] controller)]                                     |
|                                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [Console][.WriteLine([\"LexemBeforeDropper:\"] + controller.LexemBeforeDropper.Text);]                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| [controller.Items.Clear();]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                        |
| [foreach][ ([IContextChoiceItem] item [in] c)]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [  if][ (item.Text.Equals(controller.LexemBeforeDropper.Text))]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [  {]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                        |
| [  controller.Items.Add(item.Text);]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                        |
| [  }]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                        |
| [}  ]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [\' Create a new instance of the context choice item collection.]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [Private][ c [As] ContextChoiceItemCollection = [New] ContextChoiceItemCollection()]                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [\' Handle the ContextChoiceUpdate event.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                        |
| [Me][.editControl1.ContextChoiceUpdate+=[New] Syncfusion.Windows.Forms.Edit.ContextChoiceEventHandler(editControl1_ContextChoiceUpdate)]                                                     |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [\' IContextChoiceController.LexemBeforeDropper property returns the lexem before the dropper which displays the context choice. It is possible to control the lexem being searched in the context choice list using the ContextChoiceUpdate event.] |
|                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] editControl1_ContextChoiceUpdate([ByVal] controller [As] Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController)]      |
|                                                                                                                                                                                                                                                                                                        |
| [Console.WriteLine([\"LexemBeforeDropper:\"] + controller.LexemBeforeDropper.Text)]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| [controller.Items.Clear()]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| [Dim][ item [As] IContextChoiceItem]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| [For][ [Each] item [In] c]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                        |
| [  If][ item.Text.Equals(controller.LexemBeforeDropper.Text) [Then]]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| [  controller.Items.Add(item.Text)]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [  End][ [If]]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                        |
| [Next]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p127} 

[]{#related-topics}

