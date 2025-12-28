income = 70000
single_person_tax_allowance = 42000
taxable_At_20_Percent = income - single_person_tax_allowance
taxable_At_40_Percent = income - taxable_At_20_Percent
percent_tax_20 = taxable_At_20_Percent * .2
percent_tax_40 = taxable_At_40_Percent * .4
total_tax = percent_tax_20 + percent_tax_40
print(total_tax)