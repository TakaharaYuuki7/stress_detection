import csv
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import requests
import json

SLACK_URL = "https://hooks.slack.com/services/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"

def send_slack():

    content = "ストレスは溜まっていませんか？"

    payload = {
        "text": content,
    }

    data = json.dumps(payload)

    requests.post(SLACK_URL, data)



now=datetime.datetime.now()
now2=now - datetime.timedelta(days=1)
past=now - datetime.timedelta(days=36)

fname= "{}.csv".format(now2.strftime("%Y%m%d"));
flabel="{}".format(now2.strftime("%Y/%m/%d"));
fname2= "{}.csv".format(past.strftime("%Y%m%d"));
flabel2="{}".format(past.strftime("%Y/%m/%d"));


df = pd.read_csv(fname, sep="\t")
#print(df)
dfmax=(df['Temperature'].max())
#print(dfmax)
dfmin=(df['Temperature'].min())
#print(dfmin)
dfave=(dfmin+dfmax)/2

df2 = pd.read_csv(fname2,sep="\t")
df2max=max(df2['Temperature'])
df2min=min(df2['Temperature'])
df2ave=(df2min+df2max)/2
#test=-df2ave+dfave
print(test)
#reader = csv.reader(fname)
#l = [row for row in reader]
count=0
#print(df['Temperature'][2])
for num in range(31, 298):
    #print(num)
    x=df['Temperature'][num]
    #print(float(x))
    y=df['Temperature'][num-30]
    #print(y)
    if (x-y) >= 1.5:
        count=1

for num in range(31, 298):
    #print(num)
    x=df2['Temperature'][num]
    #print(float(x))
    y=df2['Temperature'][num-30]
    #print(y)
    if (x-y) >= 1.5:
        count=1
#print(count)
if count==0 and test>=0.19:
    send_slack()

plt.plot(df.index,df['Temperature'],label=flabel)
plt.plot(df.index,df2['Temperature'],label=flabel2)

plt.title('temperature', fontsize = 20)
plt.xlabel('time', fontsize = 16)
plt.ylabel('temperature', fontsize = 16)
plt.tick_params(labelsize=14)

plt.legend()
plt.grid(True)

plt.show()


