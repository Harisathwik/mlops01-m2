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
- Parameters used as:
  - `n_estimators' as 50, 100, 150
  - `max_depth` as 5, 10, None
