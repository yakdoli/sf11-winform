---
title: currencytextbox2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\currencytextbox2.md
created_at: 2025-07-03
---






#### CurrencyTextBox {#currencytextbox style="tab-stops: 0pt"}

\
Essential Tools provides the** CurrencyTextBox control** for currency specific behavior in edit controls. CurrencyTextBox is derived from** System.Windows.Forms.TextBox** and implements all the functionality needed for formatting currency input and validation.[]

[] 

{border="0"}

[] 

Figure 499: CurrencyTextBox

[] 

The text box control provided with Windows Forms is capable of displaying and editing string values. This control is generic in nature and some custom enhancements are needed to be able to effectively collect numeric data. For example, if you are   allowed to enter only currency values, the following enhancements will have to be added to the text box control.[]

[] 

[·      ]**Keyboard input validation -** Intercept user\'s keyboard input and prevent entry of any keys that shouldn\'t be present in a currency value.[]

[·      ]**Data type - **Provide the text contained in the text box as an appropriate data type (such as decimal) that can be used by the developer.[]

[·      ]**Culture formatting - **Ensure that the formatting of the display is culture sensitive.[]

 

More:



















