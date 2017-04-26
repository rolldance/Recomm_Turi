# Recommendation Engine Demo
![img](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### python version



#### Method
- **Case 1**: Recommend the most popular items.
A simple apporach could be to recommend the items which are liked by most number of users. This is a blazing fast and dirty approach and thus has a major drawback. Because there is no personalization involved with this approach.

- **Case 2**: Using classifiers to make recommendation
There are lots of classification algorithms. Classifier are parametric solutions as we just set some parameters(features) of the user and the item. But there are some absolute drawbacks just using this approach.

- **Case 3**: Use some recommendation algorithms that are much popular, such as the content based algorithms, collaborative filtering algorithms and the hybrid filtering algorithms

#### Dataset
The dataset in this project is called the `MovieLens dataset` which has been collected by the GroupLens Research Project at the University of Minnesota. The dataset can download [here](https://grouplens.org/datasets/movielens/100k/)

#### Engine
- **case 1**: We first use a simple Popularity Model, the algorithm will recommend the most popular(with the highest ratings) one to the users.

- **case 2**: The second case we use the item [similarity](http://mines.humanoriented.com/classes/2010/fall/csci568/portfolio_exports/lguo/similarity.html) for the recommendation, here are four similairty methods that are often used, `Jaccard Similarity`, `Cosine Similarity`, `Euclidean Similarity`, `Pearson Similarity`, we use the `Pearson Similairty` for the case.

#### Evaluation
- **Recall**:
This method measures the recommendation system with if there are enough items have been recommended to the users, if the user rated 5 items, but the system just recommend 3 to the users, the recall is 0.6
- **Precision**:
This method measures the recommendation system with if there are more items recommendated to the users. If the users rated 4 items, but the engine choose 5 items to the users, the precision is 0.8

#### Develop
- Version
The python version in this program is 2.7
- Pachage [`GraphLab`](https://turi.com/)  [`Crab`](http://muricoca.github.io/crab/)
 [`Surprise`](https://github.com/NicolasHug/Surprise)
 [`python-recsys`](https://github.com/ocelma/python-recsys) [`mrec`](https://github.com/Mendeley/mrec)