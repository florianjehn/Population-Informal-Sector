# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:51:19 2020

@author: Florian Jehn
"""

import pandas as pd
import matplotlib.pyplot as plt

infor = pd.read_csv("Population in informal sector.csv", sep=";", encoding="latin-1", index_col=2)
labor_force = pd.read_csv("labor_force_2019.csv", sep=";", encoding="latin-1", index_col=0)
infor = infor.merge(labor_force, left_index=True, right_index=True, how="inner")
unemploy = pd.read_csv("unemployment_2019.csv", sep=";", encoding="latin-1", index_col=0)
infor = infor.merge(unemploy, left_index=True, right_index=True, how="inner")
infor.columns =  ["Continent", "Region", "Pop. informal [%]", "Labor Force Total", "Unemployment [%]"]

#infor["Population in Informal Sector"] = infor[infor.columns[-1]] * infor[infor.columns[-2]]
#infor = infor["Population in Informal Sector"]
infor["Pop. informal Total"] = infor["Labor Force Total"] * ((100-infor["Unemployment [%]"])/100) * (infor["Pop. informal [%]"]/100)

ax = infor["Pop. informal Total"].sort_values().tail(15).plot(kind="barh", color="#2E9246", zorder=5, legend=False )
plt.ticklabel_format(style='plain', axis='x')
plt.locator_params(nbins=4, axis="x")
ax.set_xlabel("Absolute Population in Informal Sector")
ax.set_xticklabels(["", "100 Million", "200 Million", "300 Million"])
# Make plots nicer
ax.xaxis.grid(True, zorder=0)
ax.tick_params(axis=u'both', which=u'both',length=0)
for i, spine in enumerate(ax.spines.values()):
  spine.set_visible(False)
fig = plt.gcf()
fig.set_size_inches(8,3)
fig.tight_layout()


plt.savefig("informal.png", dpi=200, bbox_inches="tight")
plt.close()