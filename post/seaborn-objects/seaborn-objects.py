import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt


sns.set_theme(style="white", palette="deep6", font="Times New Roman", font_scale=1.5)

tips=sns.load_dataset("tips")
penguins=sns.load_dataset("penguins")

# (
#     so.Plot(tips, y="day", color="sex")
#     .add(so.Bar(), so.Hist(), so.Dodge())
#     .show()
#     # .save("fig.png",bbox_inches="tight")
# )

# (
#     so.Plot(penguins, "bill_length_mm", "bill_depth_mm")
#     .add(so.Dots())
#     # .facet("species", "sex")
#     .show()
# )

(
    so.Plot(tips, "total_bill", "tip", color="day")
    .facet(col="day")
    .add(so.Dot(color="#aabc"), col=None, color=None)
    .add(so.Dot())
    .theme(plt.rcParams)
    .show()
)
