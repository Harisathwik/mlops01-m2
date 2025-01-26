## MLOps
**Group 1 Assignment 1**<br>

## M2: Process and Tooling
## Objective: 
Gain hands-on experience with popular MLOps tools and understand the processes they support.

## Tasks:
1.	Experiment Tracking:
	-	Use MLflow to track experiments for a machine learning project.
	-	Record metrics, parameters, and results of at least three different model training runs.
2.	Data Versioning:
	-	Use DVC (Data Version Control) to version control a dataset used in your project.
  	-	Show how to revert to a previous version of the dataset.

## Deliverables:
1.	MLflow experiment logs with different runs and their results.
2.	A DVC repository showing different versions of the dataset.

## Experiment Tracking and Data Versioning:

This project demonstrates the use of MLOps tools such as MLflow for experiment tracking and DVC (Data Version Control) for dataset versioning. Below are the details and steps for each task.

---

## Project Structure

- model_tracking.py : contains the script for training the model on the iris dataset

---

## Tasks Overview

### 1. Experiment Tracking with MLflow

#### Prerequisites
- Python environment with the following installed:
  - `mlflow`
  - `pandas`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
  - `dvc`
 
#### Hyperparameter Configs
- Parameters used for the sklearn model are:
  - `n_estimators` as 50, 100, 150
  - `max_depth` as 5, 10, None
 
- Metrics used for evaluation are:
  - Accuracy, Precision, Recall, F1_Score

### 2. Data Versioning

#### Prerequisities
- Configured **Google Drive** as the remote storage with this [link](https://dvc.org/doc/user-guide/data-management/remote-storage/google-drive) as reference.
- Configure **git** as well.

#### Data Modification
- Dataset is modified by making duplicates and a new version has been pushed to the remote storage.

  		! cp dataset/iris.csv /tmp/iris.csv
		! cat /tmp/iris.csv >> dataset/iris.csv

#### Restore to previous version
- Restoring to a version behind the HEAD.

  		! git checkout HEAD^1 dataset/iris.csv.dvc

#### Delieverables
- Dashboard
  ![image](https://github.com/user-attachments/assets/c8e13260-2303-468b-a17b-d90c21eb856d)
- First run with max_depth 5 and n_estimators 50
  ![image](https://github.com/user-attachments/assets/ed9ac21a-6092-4e42-9ad3-c76293f181a5)
- Second run with max_depth 10 and n_estimators 100
  ![image](https://github.com/user-attachments/assets/94185b68-7f1a-4c69-9161-2fde7218510a)
- Third run with max_depth None and n_estimators 150
  ![image](https://github.com/user-attachments/assets/5fd473b2-0b9c-4208-b1c5-e5c6fdfce7e6)

- DVC Remote Storage with different versions on google drive
- Modified version of the dataset
  ![image](https://github.com/user-attachments/assets/849973d2-022a-4ca6-9c43-de93135c9187)

- Original Unmodified verison of the data
  ![image](https://github.com/user-attachments/assets/1c9fecc3-0b81-468a-8452-35b2abb80948)

- Compare the hashes from the above with the below ones available of the file explorer inside of .dvc/cache/
  ![image](https://github.com/user-attachments/assets/3ec5ee9a-fdab-4573-a41b-5265df84c293)


  




