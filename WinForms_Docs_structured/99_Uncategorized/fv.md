---
title: fv.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\fv.md
created_at: 2025-07-03
---








  









### FV {#fv style="tab-stops: 0pt"}

The **FV** function returns the future value of an investment, based on an interest rate and a constant payment schedule.

 

**Syntax:**

FV( interest_rate, number_payments, payment, PV, Type )

 

where,

[·      ]interest_rate is the interest rate for the investment.

[·      ]number_payments is the number of payments for the annuity.

[·      ]payment is the payment made on each period.

[·      ]PV is the present value of the payments. This is optional. The FV function assumes PV value as 0, when this parameter is omitted.

[·      ]Type indicates the payments due. Type accepts the following values:

[o  ]0 - Payments at the end of the period (default).

[o  ]1 - Payments at the beginning of the period.

               

This is optional. The FV function assumes Type value as 0, when this parameter is omitted.

 

[]{#related-topics}

