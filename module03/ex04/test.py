from Kmeans import KmeansClustering



kmns = KmeansClustering(ncentroid=4)

kmns.dataset_import("solar_system_census.csv")

kmns.dataset_plot()

kmns.fit()

kmns.dataset_plot()

topred = kmns.data[0:20, :-1]

res = kmns.predict(topred)

print(res)