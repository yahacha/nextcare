import streamlit as st
import base64
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./samples_datasets.csv")

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

st.sidebar.markdown(
            """
            <img src='data:image/png;base64,{}' class='img-fluid' width=250 height=100>""".format(
                img_to_bytes("./nextcare_logo.png")
            ),
            unsafe_allow_html=True,
        )
st.sidebar.markdown("<strong> We are trusted partners to insurers, businesses and healthcare providers around the world. </strong> ",
            unsafe_allow_html=True)
st.sidebar.subheader("")
st.sidebar.subheader("")


st.sidebar.selectbox("Select Option",["Data visualization","Predict Frauds"])

st.title("Nextcare Fraud Detection Solution")
st.subheader("")
st.subheader("")
st.subheader("")
c = st.columns(3)

fig1, ax1 = plt.subplots()
data = df.Reimbursement.value_counts()
ax1.pie(data, labels=["No","Yes"], autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Reimbursement")
c[0].pyplot(fig1)

fig1, ax1 = plt.subplots()
data = df["Gender Desc"].value_counts()
print(data)
ax1.pie(data, labels=["Female","Male"], autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Gender Distribution")
c[1].pyplot(fig1)

fig1, ax1 = plt.subplots()
data = df["Dependency"].value_counts()
print(data)
ax1.pie(data, labels=data.index.values, autopct='%1.1f%%',
        shadow=True, startangle=90,explode=[0.2, 0, 0, 0,0.1])
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Dependency")
c[2].pyplot(fig1)

focGender = df.loc[:,["FOC","Gender"]]
f, ax = plt.subplots(figsize=(20, 10))



sns.countplot(data = focGender,x="FOC",hue="Gender", alpha=0.8)
plt.title('Family Of Causes Distribution per Gender')
plt.ylabel('Count Causes', fontsize=12)
plt.xlabel('FOC', fontsize=12)
st.pyplot(f)

prov = df["Provider Type"]
f, ax = plt.subplots(figsize=(20, 10))
sns.countplot(y=prov, alpha=0.8)
plt.title('Provider Type')
plt.ylabel('Providers', fontsize=12)
plt.xlabel('count', fontsize=12)
st.pyplot(f)


def per(x):
  return(str(round(100 * x)) + "%")
c = df.loc[:,["Claim Status"]].value_counts()

p = df.loc[:,["Claim Status"]].value_counts(normalize=True)
idd = pd.concat([c,p], axis=1, keys=['counts', '%'])
idd["%"] = idd["%"].apply(per)

f, ax = plt.subplots(figsize=(20, 10))
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

x = [idd.index.values[i][0] for i in range(len(idd))]

ax = sns.barplot(x=x, y=idd["counts"], palette='PuBuGn_r')
patches = ax.patches
for i in range(len(patches)):
   x = patches[i].get_x() + patches[i].get_width()/2
   y = patches[i].get_height()+.05
   ax.annotate(idd["%"].values[i], (x, y), ha='center')
   
st.pyplot(f)

c=st.columns(4)

OP = df[df["FOB"]=="Out-Patient"]["Claim Status"].value_counts()
IP = df[df["FOB"]=="In-Patient"]["Claim Status"].value_counts()
Optical = df[df["FOB"]=="Optical"]["Claim Status"].value_counts()
Dental = df[df["FOB"]=="Dental"]["Claim Status"].value_counts()
op_perc = [round(i/OP.values.sum()*100) for i in OP.values]
ip_perc = [round(i/IP.values.sum()*100) for i in IP.values]
opt_perc = [round(i/Optical.values.sum()*100) for i in Optical.values]
den_perc = [round(i/Dental.values.sum()*100) for i in Dental.values]

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

x = [OP.index.values[i] for i in range(len(OP))]
f, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x=x,y=OP.values, palette='PuBuGn_r')
plt.title("%OP")
patches = ax.patches
for i in range(len(patches)):
   x = patches[i].get_x() + patches[i].get_width()/2
   y = patches[i].get_height()+.05
   ax.annotate(str(op_perc[i])+"%", (x, y), ha='center')

c[0].pyplot(f)

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

x = [IP.index.values[i] for i in range(len(IP))]
f, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x=x,y=IP.values, palette='PuBuGn_r')
plt.title("%IP")
patches = ax.patches
for i in range(len(patches)):
   x = patches[i].get_x() + patches[i].get_width()/2
   y = patches[i].get_height()+.05
   ax.annotate(str(ip_perc[i])+"%", (x, y), ha='center')

c[1].pyplot(f)

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

x = [Optical.index.values[i] for i in range(len(Optical))]
f, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x=x,y=Optical.values, palette='PuBuGn_r')
plt.title("%Optical")
patches = ax.patches
for i in range(len(patches)):
   x = patches[i].get_x() + patches[i].get_width()/2
   y = patches[i].get_height()+.05
   ax.annotate(str(opt_perc[i])+"%", (x, y), ha='center')

c[2].pyplot(f)

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

x = [Dental.index.values[i] for i in range(len(Dental))]
f, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x=x,y=Dental.values, palette='PuBuGn_r')
plt.title("%Dental")
patches = ax.patches
for i in range(len(patches)):
   x = patches[i].get_x() + patches[i].get_width()/2
   y = patches[i].get_height()+.05
   ax.annotate(str(den_perc[i])+"%", (x, y), ha='center')
c[3].pyplot(f)

# Providers that have more than 1000 patient
prov = df["Provider"].value_counts()[df["Provider"].value_counts()>1000]
f, ax = plt.subplots(figsize=(20, 10))
sns.barplot(y= prov.index,x=prov.values, alpha=0.8)
plt.title('Top Providers that has more than 1000 patient')
plt.ylabel('Providers', fontsize=12)
plt.xlabel('count', fontsize=12)
st.pyplot(f)
