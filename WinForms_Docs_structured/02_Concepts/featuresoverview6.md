---
title: featuresoverview6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\featuresoverview6.md
created_at: 2025-07-03
---








  









### Features Overview {#features-overview style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

The Tabs framework contains the TabControlAdv with a full set of features to support efficient tab usage to create rich user applications.

[] 

{border="0"}

[] 

Figure 1030: TabControlAdv Features

[] 

Features

[] 

[·      ]**TabStyles**

 

Tabs framework provides a number of pre-defined TabStyles and also allows to apply custom style settings to the control.

 

[·      ]**Appearance settings**

 

The Tab appearance can be easily customized by stating the style definitions for the TabItems, TabPages and TabPanels individually.

 

[·      ]**TabPrimitives**

 

TabControlAdv provides an easy way to navigate through tabs. By setting TabPrimitives (previously, TabControlAdv\'s  NavigationControl property), users can traverse between tabs and pages easily which enables to go to the next or previous tab / page and first / last tab, close buttons can be added which closes the active tabpage when clicked and the dropdown with all the tabpages listed can be accessed by the user to select the tabpage to be traversed.

 

NavigationControl offers more flexibility that allows you to change the button\'s image, show / hide certain buttons and also cancel the navigation and use it as an Add or Remove TabPages through code.

 

[·      ]**Alignment and Sizing**

 

The TabStrip can be aligned to the Top, Left, Right or Bottom of the control. Text alignment can be changed using the RotateTextWhenVertical property which will rotate the text and draw it horizontally when the alignment is set to Left. The Tabs can also be set to be displayed in Multiple lines using the Multiline property. The TabItems can be aligned from Left to Right and vice versa using the RightToLeft property. When the RightToLeft mode is activated and RotateTabsWhenRTL property is enabled, tab rotation is allowed. The SizeMode can be set to either Normal, Fixed, ShrinkToFit or FillToRight.

 

[·      ]**LabelEdit**

 

TabPage\'s text can be edited during run-time using LabelEdit property.

 

LabelEdit feature has the following events associated with it.

 

[o  ]BeforeEdit - Occurs when the text enters into the edit mode.

[o  ]AfterEdit - Occurs after the new text is entered.

[o  ]LabelEditTextChanged - Occurs when the text of the tab is changed.

[o  ]LabelEditChanged **-*[ ]***Occurs when the LabelEdit property is toggled.

**[]** 

[·      ]**Image Support**

 

TabPage\'s text can be associated with images. Images can be aligned according to the alignment of the tabs.

 

[·      ]**Color Properties**

 

TabControlAdv allows the user to set different colors for active and inactive tabs using ActiveTabColor, InactiveTabcolor, TabBackColor, TabForeColor and TabPanelBackColor properties.

 

[·      ]**Themes Support**

 

TabControlAdv provides complete[ ]theme support. Using the ThemesEnabled property, XP themes can be enabled for this control.

 

[·      ]**TabPersistence**

 

Complete[ ]persistence support is now available for TabControlAdv using the PersistTabState property.

[] 


{border="0"} Note:[ ]TabState has been saved at the following location: C:\\Documents and Settings\\Username\*\\Local Settings\\Application Data\\IsolatedStorage.


[] 

[·      ]Close button can be added for each TabPage like IE7 to close the tabpage.

[] 

{border="0"}

***[]*** 

Figure 1031: Close button added for Tab Page

[] 

[·      ]Lets you set tooltips for every TabPrimitives.

[·      ]Added VS2008 [[TabStyle]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_TabStyles)[ ]{.UGHyperlink}for TabControlAdv.

[·      ]Added [[Border]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Border_for_TabControlAdv) settings for the control which is implemented especially for VS2008 TabStyle.

[·      ]TabPage Closed and Closing [[events]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_TabControlAdv_Events) are added.

[] 

A sample which illustrates the features of TabControlAdv is available in the following sample installation location.

[] 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Tools.Windows\\Samples\\2.0\\Tabs Package\\TabControlAdvDemo***

 

 

 

 

[]{#related-topics}

