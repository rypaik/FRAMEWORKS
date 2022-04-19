import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#TODO: seaborn snippets

#snippets #seaborn 
# gets all sns dataset names

print(sns.get_dataset_names())



data_frame=sns.load_dataset('planets')
print(data_frame.head())

def main():
    page = st.sidebar.selectbox(
        "Select a Page", 
        [
            "Line Plot",
            "Count Plot",
            "Violin Strip Plot"
        ]
    )

    if page == "Line Plot":
        linePlot()
    elif page =="Count Plot":
        countPlot()
    elif page == "Violin Strip Plot":
        violinStrip_plot()




# lineplot function
def linePlot():
    fig = plt.figure(figsize=(10,4))
    sns.lineplot(x ='distance', y = 'mass', data = data_frame)
    st.pyplot(fig)

# countplot function
def countPlot():
    fig = plt.figure(figsize=(10,4))
    sns.countplot(x='year', data = data_frame)
    st.pyplot(fig)



def violinStrip_plot():
    st.header("Violin & Strip Plot")
    sd = st.selectbox(
        "Select a Plot", #Drop Down Menu Name
        [
            "Violin Plot", #First option in menu
            "Strip Plot"   #Seconf option in menu
        ]
    )

    fig = plt.figure(figsize=(12, 6))

    if sd == "Violin Plot":
        sns.violinplot(x = "year", y = "mass", data = data_frame)
    
    elif sd == "Strip Plot":
        sns.stripplot(x = "mass", y = "distance", data = data_frame)

    st.pyplot(fig)



if __name__ == "__main__":
    main()








