---
title: keyboardnavigation1.md
original_path: WinForms_Docs/99_Uncategorized/keyboardnavigation1.md
created_at: 2025-08-05
---






#### Keyboard Navigation {#keyboard-navigation style="tab-stops: 0pt"}

[] 

Gauge Silverlight now comes with keyboard navigation support. The keys can be used to change the pointer value in the Circular Gauge.

[] 

Default Keys

[] 

By default, the following keys on the keyboard can be used to change the pointer value:

[] 

[·      ]**UP ARROW** and **PAGE UP** keys can be used to increase the pointer value of a gauge.

[·      ]**DOWN ARROW** and **PAGE DOWN** keys can be used to decrease the value.

[·      ]**RIGHT ARROW** and **LEFT ARROW** keys increase and decrease the pointer value.

[·      ]**HOME** and **END** keys are used to set the value to Minimum and Maximum.

[·      ]**TAB** key selects the pointer to navigate.

[] 


{border="0"}Note:

By default, when the pointer gets focus, its border color changes to black. This can be modified by using PointerSelectionBrush property.

Custom keys can be added to increase and decrease the pointer value by using the IncrementKey and DecrementKey properties.


[] 

The following screen shots illustrate the effect of default keys on gauge pointers:

[] 

1.   Initial Circular Gauge

[] 

{border="0"}

[] 

Figure 66: Circular Gauge

[] 

2.   Focus is shifted to Circular Gauge Pointer.

[] 

{border="0"}

[] 

Figure 67: Circular Gauge Pointer Focused

[] 

3.   Focus is removed from the Circular Gauge Pointer.

[] 

{border="0"}

[] 

Figure 68: Circular Gauge Pointer Focus Lost

[] 

4.   Circular Gauge Pointer value is increased.

[] 

[{border="0"}][]

[] 

Figure 69: Increase in Circular Gauge Pointer Value

[] 

5.   Circular Gauge Pointer value is decreased.

[] 

{border="0"}

[] 

Figure 70: Decrease in Circular Gauge Pointer Value

[] 

6.   HOME key is pressed.

[] 

{border="0"}

[] 

Figure 71: Circular Gauge Pointer returns to the Start

[] 

7.   END key is pressed.

[] 

{border="0"}

[] 

Figure 72: Circular Gauge Pointer returns to the End

 

[]{#p57} 

 

More:









