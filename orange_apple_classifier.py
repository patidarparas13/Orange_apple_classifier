from sklearn import tree
features=[[150,0],[170,0],[140,1],[130,1]] #0 =Bumpy ,1 =Smooth
labels=[1,1,0,0] #1 = Orange , 0 =Apple
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
prediction=clf.predict([[150,0]])
print(prediction)
