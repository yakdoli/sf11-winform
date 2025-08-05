---
title: events93.md
original_path: WinForms_Docs/99_Uncategorized/events93.md
created_at: 2025-08-05
---








  









### Events {#events style="tab-stops: 0pt"}

The following table lists the events available in EditControl class and its purpose.

[] 

Table 7: EditControl Events


  ------------------------ ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Event                    Type                          Description
  DocumentSourceChanged    PropertyChangedCallback       A property changed event gets raised when the **DocumentSource** property value is changed.
  IntellisenseBoxOpening   IntellisenseBoxEventHandler   Gets raised before the **Intellisense popup** is displayed. This event can be used to cancel the **Intellisense popup** display or change **ItemsSource** of the **Intellisense ListBox** and so on.
  IntellisenseDrillDown    IntellisenseBoxEventHandler   Drill down in Intellisense occurs when the user types the drill down char specified in the CurrentLanguage instance. When the drill down occurs, the Intellisense looks for any sub items are available for the selected Intellisense item and displays it the popup if any. This event gets raised before the Intellisense popup is displayed after a drill down char is typed by the user. This event can be used to perform any operations related to Intellisense during drill down.
  SelectedTextChanged      PropertyChangedCallback       A **PropertyChangedCallback** gets raised when the text in the EditControl is **selected.**
  TextChanged              PropertyChangedCallback       A **PropertyChangedCallback get** raised when the text in the EditControl gets **changed.**
  ------------------------ ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

 

[]{#p15} 

 

[]{#related-topics}

