
import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show() 

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis("equal")
    plt.show()

nombres = ["México", "Bolivia", "Colombia"]
pib = [2000,1800,2200]

if __name__ == "__main__":
    #generate_bar_chart(nombres, pib)
    generate_pie_chart(nombres, pib)




