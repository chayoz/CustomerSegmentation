import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def show_accuracy(model,X_train):
    print(model.cluster_centers_)

    centroids_x = model.cluster_centers_[:, 0]
    centroids_y = model.cluster_centers_[:, 1]
    centroids_z = model.cluster_centers_[:, 2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xx = np.array(X_train['Age'])
    yy = np.array(X_train['Gender'])
    zz = np.array(X_train['AnnualIncome'])

    colors = ['green', 'red', 'blue', 'magenta']
    labels = model.labels_
    ax.scatter(xx, yy, zz, c=np.array(colors)[labels], alpha=0.3)

    ax.scatter(centroids_x, centroids_y, centroids_z, marker="x", s=150, linewidths=5, alpha=1, c=colors)

    plt.show()


def show_cl(X_train):
    Sum_of_squared_distances = []
    K = range(1,10)
    for num_clusters in K :
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(X_train)
        Sum_of_squared_distances.append(kmeans.inertia_)
    plt.plot(K,Sum_of_squared_distances,'bx-')
    plt.xlabel('Values of K') 
    plt.ylabel('Sum of squared distances/Inertia') 
    plt.title('Elbow Method For Optimal k')
    plt.show()
    
def testingpoints(model, scaler, x1, x2, x3 ,x4):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Create a test point
    x_test = x1
    y_test = x2
    z_test = x3
    v_test = x4
    # Define corresponding numpy array
    test = np.array([[x_test, y_test, z_test, v_test]])
    # Apply scaler's transformation
    test = scaler.transform(test)
    # Create an empty list
    dist_list = []
    print(model.cluster_centers_)
    # Iterate over the centroids of the 4 clusters
    for c in range(4):
        # Extract each centroid
        centroid = model.cluster_centers_[c, :]
        # Calculate distance between test point and current centroid
        dist = np.linalg.norm(test-centroid)
        # and store the value to the list
        dist_list.append(dist)

    # Find min value of the list, namely closest centroid
    min_val = min(dist_list)
    # and its index on dist_list
    min_index = dist_list.index(min_val)
    # The index is simply the cluster where the test point belongs 
    print(min_index)
    # Or just use kmeans' algorithm predict method!
    print(model.predict(test))

    ax.scatter(test[:, 0], test[:, 1], test[:, 2], marker="x", s=150, linewidths=5, alpha=1,
               c=['black'])

    plt.show()