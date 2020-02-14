import pandas as pd
import matplotlib.pyplot as plt
import datetime
import requests
import json

def send_slack():

    content = "ストレスは溜まっていませんか？"

    payload = {
        "text": content,
        "icon_emoji": ':snake:',
    }

    data = json.dumps(payload)

    requests.post(SLACK_URL, data)

    
fname = "{}.csv".format(datetime.datetime.now().strftime("%Y%m%d"));
flabel="{}".format(datetime.datetime.now().strftime("%Y/%m/%d"));

df = pd.read_csv(fname, names=['num1', 'num2'])
dfmax=max(df['num2'])
dfmin=min(df['num2'])
dfave=(dfmin+dfmax)/2
plt.plot(df['num1'],df['num2'],marker="o",label=flabel)
df2 = pd.read_csv(fname, names=['num1', 'num2'])
df2max=max(df2['num2'])
df2min=min(df2['num2'])
df2ave=(df2min+df2max)/2
print(df2max)
print(df2min)
print(df2ave)

test=df2ave-dfave
if test>=0.2:
    #print('WQRNING STRESS')
    send_slack()
else:
    #print('NOTSTRESS')
    
plt.plot(df2['num1'],df2['num2'],marker="o",label=flabel)

plt.title('temperature()', fontsize = 20)
plt.xlabel('time', fontsize = 16)
plt.ylabel('temperature', fontsize = 16)
plt.tick_params(labelsize=14)

plt.legend()
plt.grid(True)

plt.show()


