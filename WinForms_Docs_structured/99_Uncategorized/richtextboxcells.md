---
title: richtextboxcells.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\richtextboxcells.md
created_at: 2025-07-03
---






##### Rich Text Box Cells {#rich-text-box-cells style="tab-stops: 0pt"}

The Rich Text control will allow you to display and edit rich text in grid cells. The control will allow you to modify the rich text through in-place editing.

 

Example

 

It can be built by hosting the Rich Text Box control in grid cells. To host this control, the cellrenderer must be derived from GridVirtualizingCellRenderer, whose OnIntializeContent should be overridden to provide the content (as Flow Document) for the rich text box.

 

CellModel class

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                             |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [public][ [class] [RichTextBoxCellModel] : GridCellModel\<RichTextBoxCellRenderer\>] |
|                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                |
|                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

CellRenderer class

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                        |
| [public][ [class] [RichTextBoxCellRenderer] : GridVirtualizingCellRenderer\<[RichTextBox]\>] |
|                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [    [public] RichTextBoxCellRenderer()]                                                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [        IsControlTextShown = [false];]                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [        IsFocusable = [true];]                                                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [    [public] [override] [void] OnInitializeContent([RichTextBox] textBox, GridRenderStyleInfo style)]                      |
|                                                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [        textBox.Padding = [new] [Thickness](0);]                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [        [FlowDocument] document = GetControlValue(style) [as] [FlowDocument];]                                                               |
|                                                                                                                                                                                                                                                        |
| [        [if] (document == [null])]                                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [            textBox.Document = [new] [FlowDocument]();]                                                                                                              |
|                                                                                                                                                                                                                                                        |
| [        [if] (document.Parent != [null])]                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [            [var] parentTextBox = document.Parent [as] [RichTextBox];]                                                                          |
|                                                                                                                                                                                                                                                        |
| [            parentTextBox.Document = [new] [FlowDocument]();]                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [        }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [        textBox.Document = document;]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                        |
| [        VirtualizingCellsControl.SetWantsMouseInput(textBox, [true]);]                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [    [protected] [override] [void] OnUnwireUIElement([RichTextBox] uiElement)]                                              |
|                                                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [        uiElement.Document = [new] [FlowDocument]();]                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [        [base].OnUnwireUIElement(uiElement);]                                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [    [protected] [override] [object] GetControlValueFromEditorCore([RichTextBox] uiElement)]                                |
|                                                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [        [return] uiElement.Document;]                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [    [protected] [override] [void] OnGridPreviewTextInput([TextCompositionEventArgs] e)]                                    |
|                                                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [        CurrentCell.ScrollInView();]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                        |
| [        CurrentCell.BeginEdit([true]);]                                                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [    [protected] [override] [bool] ShouldGridTryToHandlePreviewKeyDown([KeyEventArgs] e)]                                   |
|                                                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [        [if] (CurrentCellUIElement.IsFocused && e.Key != [Key].Escape)]                                                                                              |
|                                                                                                                                                                                                                                                        |
| [            [return] [false];]                                                                                                                                          |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [        [return] [true];]                                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Setting up Rich Text Box Cell

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                      |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [grid.Model.CellModels.Add([\"RichText\"], [new] RichTextBoxCellModel());]                                     |
|                                                                                                                                                                                                 |
| [grid.Model.CellModels.Add([\"FlowDocumentReader\"], [new] FlowDocumentReaderCellModel());]                    |
|                                                                                                                                                                                                 |
| [{]                                                                                                                                                         |
|                                                                                                                                                                                                 |
| [// Create a FlowDocument to contain content for the RichTextBox.]                                                                            |
|                                                                                                                                                                                                 |
| [FlowDocument myFlowDoc = [new] FlowDocument();]                                                                                       |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [// Add paragraphs to the FlowDocument.]                                                                                                      |
|                                                                                                                                                                                                 |
| [myFlowDoc.Blocks.Add([new] Paragraph([new] Run([\"Paragraph 1\"])));]                    |
|                                                                                                                                                                                                 |
| [myFlowDoc.Blocks.Add([new] Paragraph([new] Run([\"Paragraph 2\"])));]                    |
|                                                                                                                                                                                                 |
| [myFlowDoc.Blocks.Add([new] Paragraph([new] Run([\"Paragraph 3\"])));]                    |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [grid.Model\[2, 2\].CellType = [\"RichText\"];]                                                                                     |
|                                                                                                                                                                                                 |
| [grid.Model\[2, 2\].CellValue = myFlowDoc;]                                                                                                                 |
|                                                                                                                                                                                                 |
| [grid.Model.CoveredCells.Add([new] CoveredCellInfo(2, 2, 8, 8));]                                                                      |
|                                                                                                                                                                                                 |
| [}]                                                                                                                                                         |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [{]                                                                                                                                                         |
|                                                                                                                                                                                                 |
| [Paragraph myParagraph = [new] Paragraph();]                                                                                           |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [// Add some Bold text to the paragraph]                                                                                                      |
|                                                                                                                                                                                                 |
| [myParagraph.Inlines.Add([new] Bold([new] Run([\"Some bold text in the paragraph.\"])));] |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [// Add some plain text to the paragraph]                                                                                                     |
|                                                                                                                                                                                                 |
| [myParagraph.Inlines.Add([new] Run([\" Some text that is not bold.\"]));]                                      |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [// Create a List and populate with three list items.]                                                                                        |
|                                                                                                                                                                                                 |
| [List myList = [new] List();]                                                                                                          |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [// First create paragraphs to go into the list item.]                                                                                        |
|                                                                                                                                                                                                 |
| [Paragraph paragraphListItem1 = [new] Paragraph([new] Run([\"ListItem 1\"]));]            |
|                                                                                                                                                                                                 |
| [Paragraph paragraphListItem2 = [new] Paragraph([new] Run([\"ListItem 2\"]));]            |
|                                                                                                                                                                                                 |
| [Paragraph paragraphListItem3 = [new] Paragraph([new] Run([\"ListItem 3\"]));]            |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [// Add ListItems with paragraphs in them.]                                                                                                   |
|                                                                                                                                                                                                 |
| [myList.ListItems.Add([new] ListItem(paragraphListItem1));]                                                                            |
|                                                                                                                                                                                                 |
| [myList.ListItems.Add([new] ListItem(paragraphListItem2));]                                                                            |
|                                                                                                                                                                                                 |
| [myList.ListItems.Add([new] ListItem(paragraphListItem3));]                                                                            |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [// Create a FlowDocument with the paragraph and list.]                                                                                       |
|                                                                                                                                                                                                 |
| [FlowDocument myFlowDocument = [new] FlowDocument();]                                                                                  |
|                                                                                                                                                                                                 |
| [myFlowDocument.Blocks.Add(myParagraph);]                                                                                                                   |
|                                                                                                                                                                                                 |
| [myFlowDocument.Blocks.Add(myList);]                                                                                                                        |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [grid.Model\[10, 2\].CellType = [\"RichText\"];]                                                                                    |
|                                                                                                                                                                                                 |
| [grid.Model\[10, 2\].CellValue = myFlowDocument][;]                                                                     |
|                                                                                                                                                                                                 |
| [}]                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

 

The following output is generated using the code above.

[] 

{border="0"}

Figure 42: Rich Text Box Cell

[]{#related-topics}

