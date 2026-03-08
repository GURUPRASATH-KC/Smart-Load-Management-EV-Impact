import pandas as pd
import matplotlib.pyplot as plt

data = {'Time': ['10:00','10:10','10:20','10:30','10:40'],
        'Voltage':[230,225,220,218,215],
        'EV_Charging':[0,1,1,2,2]}

df = pd.DataFrame(data)

plt.plot(df['Time'], df['Voltage'], marker='o', label='Voltage (V)')
plt.bar(df['Time'], df['EV_Charging']*5, alpha=0.3, color='orange', label='EV Load Effect')
plt.xlabel('Time')
plt.ylabel('Voltage / EV Load')
plt.title('Impact of EV Charging on Voltage')
plt.legend()
plt.grid(True)
plt.show()
