# WeightedPairedScheduling

Just initialize the list and give the parameters:
  - How many times do you want it to execute?
  - How many people exist in a pair?

Algorithm provides that:
  - No one will be selected in a row (If it is forced code crashes)
  - Everybody will be selected nearly equal times

Sample output
---------------
- ['ECE', 'GOZDEGUL']
- ['AYKUT', 'CAN']
- ['MEHMET', 'MUGE']
- ['AYDAN', 'GIZEM']
- ['CANBURAK', 'YASIN']
- ['GIZEM', 'ECE']
- ['GOZDEGUL', 'AYKUT']
- ['YASIN', 'MUGE']
- ['CAN', 'MEHMET']
- ['CANBURAK', 'AYDAN']
- {'ECE': 2, 'CANBURAK': 2, 'GOZDEGUL': 2, 'MUGE': 2, 'MEHMET': 2, 'AYDAN': 2, 'YASIN': 2, 'CAN': 2, 'AYKUT': 2, 'GIZEM': 2}
