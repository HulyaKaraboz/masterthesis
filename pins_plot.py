import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

headersCustom = ['grip', 'wall', 'button', 'timestamp', 'id_no', 'grip_letter', 'orientationX', 'orientationY',
                         'orientationZ', 'accelerometerX', 'accelerometerY', 'accelerometerZ', 'gyroscopeX',
                         'gyroscopeY', 'gyroscopeZ', 'calcTimestamp', 'calcOrientationX']

#Hier liegt die zu vearbeitende CSV-Datei
FILESPACE="C:\FILESPACE"
df = pd.read_csv(os.path.normpath(FILESPACE+'/data/'+"p_grip.csv"))
print(df)

#wenn timestamp und steptimestamp gleich sind, wird es rausgefiltert, da sonst diese hohe zahl drin steht und keine differenz
rslt_df = df[df['calcTimestamp'] < 1700000000000]
#rslt_df = rslt_df.sort_values(by=['calcTimestamp'])
print('\nResult dataframe :\n', rslt_df)

#linien
#rslt_df.plot('calcTimestamp', 'orientationX')

#bunte punkte
#color = np.random.rand(len(rslt_df),3)

#plot für orientationX
axs1 = sns.lineplot(data=rslt_df,
                    x="calcTimestamp", y="calcOrientationX",
                    lw=0.1,
                    estimator=None, units='id_no')
#axs1 = rslt_df.plot.scatter(x='calcTimestamp', y='orientationX', c='red')
axs1.set_title('Orientation X (Pins)')
axs1.set_xlabel('timestamp')
axs1.set_ylabel('orientation X')
plt.savefig("p_orientationX_plot.pdf".format('calcOrientationX'), format="pdf", bbox_inches="tight")
plt.show()

#plot für orientationY
axs2 = sns.lineplot(data=rslt_df, x="calcTimestamp", y="orientationY", lw=0.1, estimator=None, units='id_no') #, hue='id_no', style='id_no')
#axs2 = rslt_df.plot.scatter(x='calcTimestamp', y='orientationY', c='blue')
axs2.set_title('Orientation Y (Pins)')
axs2.set_xlabel('timestamp')
axs2.set_ylabel('orientation Y')
plt.savefig("p_orientationY_plot.pdf".format('orientationY'), format="pdf", bbox_inches="tight")
plt.show()

#plot für orientationZ
axs3 = sns.lineplot(data=rslt_df, x="calcTimestamp", y="orientationZ", lw=0.1, estimator=None, units='id_no')   #, hue='id_no', style='id_no')
#axs3 = rslt_df.plot.scatter(x='calcTimestamp', y='orientationZ', c='green')
axs3.set_title('Orientation Z (Pins)')
axs3.set_xlabel('timestamp')
axs3.set_ylabel('orientation Z')
plt.savefig("p_orientationZ_plot.pdf".format('orientationZ'), format="pdf", bbox_inches="tight")
plt.show()

#plot für accelerometerX
axs4 = sns.lineplot(data=rslt_df, x="calcTimestamp", y="accelerometerX", lw=0.1, estimator=None, units='id_no')
#axs4 = rslt_df.plot.scatter(x='calcTimestamp', y='accelerometerX', c='red')
axs4.set_title('Accelerometer X (Pins)')
axs4.set_xlabel('timestamp')
axs4.set_ylabel('accelerometer X')
plt.savefig("p_accelerometerX_plot.pdf".format('accelerometerX'), format="pdf", bbox_inches="tight")
plt.show()

#plot für accelerometerY
axs5 = sns.lineplot(data=rslt_df, x="calcTimestamp", y="accelerometerY", lw=0.1, estimator=None, units='id_no') #, hue='id_no', style='id_no')
#axs5 = rslt_df.plot.scatter(x='calcTimestamp', y='accelerometerY', c='blue')
axs5.set_title('Accelerometer Y (Pins)')
axs5.set_xlabel('timestamp')
axs5.set_ylabel('accelerometer Y')
plt.savefig("p_accelerometerY_plot.pdf".format('accelerometerY'), format="pdf", bbox_inches="tight")
plt.show()

#plot für accelerometerZ
axs6 = sns.lineplot(data=rslt_df, x="calcTimestamp", y="accelerometerZ", lw=0.1, estimator=None, units='id_no') #, hue='id_no', style='id_no')
#axs6 = rslt_df.plot.scatter(x='calcTimestamp', y='accelerometerZ', c='green')
axs6.set_title('Accelerometer Z (Pins)')
axs6.set_xlabel('timestamp')
axs6.set_ylabel('accelerometer Z')
plt.savefig("p_accelerometerZ_plot.pdf".format('accelerometerZ'), format="pdf", bbox_inches="tight")
plt.show()

#plot für gyroscopeX
axs7 = sns.lineplot(data=rslt_df, x="calcTimestamp", y="gyroscopeX", lw=0.1, estimator=None, units='id_no') #, hue='id_no', style='id_no')
#axs7 = rslt_df.plot.scatter(x='calcTimestamp', y='gyroscopeX', c='red')
axs7.set_title('Gyroscope X (Pins)')
axs7.set_xlabel('timestamp')
axs7.set_ylabel('gyroscope X')
plt.savefig("p_gyroscopeX_plot.pdf".format('gyroscopeX'), format="pdf", bbox_inches="tight")
plt.show()

#plot für gyroscopeY
axs8 = sns.lineplot(data=rslt_df, x="calcTimestamp", y="gyroscopeY", lw=0.1, estimator=None, units='id_no') #, hue='id_no', style='id_no')
#axs8 = rslt_df.plot.scatter(x='calcTimestamp', y='gyroscopeY', c='blue')
axs8.set_title('Gyroscope Y (Pins)')
axs8.set_xlabel('timestamp')
axs8.set_ylabel('gyroscope Y')
plt.savefig("p_gyroscopeY_plot.pdf".format('gyroscopeY'), format="pdf", bbox_inches="tight")
plt.show()

#plot für gyroscopeZ
axs9 = sns.lineplot(data=rslt_df, x="calcTimestamp", y="gyroscopeZ", lw=0.1, estimator=None, units='id_no') #, hue='id_no', style='id_no')
#axs9 = rslt_df.plot.scatter(x='calcTimestamp', y='gyroscopeZ', c='green')
axs9.set_title('Gyroscope Z (Pins)')
axs9.set_xlabel('timestamp')
axs9.set_ylabel('gyroscope Z')
plt.savefig("p_gyroscopeZ_plot.pdf".format('gyroscopeZ'), format="pdf", bbox_inches="tight")
plt.show()