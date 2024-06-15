# Participants:
## Jimmy Patel jpate289@uic.edu Github username: jaymeet2003
## Kalash Shah kshah216@uic.edu Github username: KalashShah15
## Prateek Majji smajji3@uic.edu Github username: CodeHub007
## Dishant Desle ddesle3@uic.edu Github username: desledishant10
## Josephine Huss jhuss2@uic.edu Github username: josephinehuss

# COVID-19 Open Research Dataset
## Big Idea:- 
The big idea behind this dataset appears to be tracking the progress and impact of the COVID-19 pandemic across different states in the United States. By compiling these metrics, the dataset helps in monitoring the spread of the virus, the response of the
healthcare systems, and the overall public health situation.

## What is the problem you want to solve, question you want to answer, or decision making you want to support?
The problem this data aims to solve is related to understanding how different states are affected by COVID-19, how their healthcare
systems are coping, and identifying trends or patterns in the spread or containment of the virus. It could also be aimed at supporting
policy decisions, healthcare planning, and public health interventions.

## Why should others care about it?
Others should care about this data as it provides insights into the severity and progression of the COVID-19 pandemic, which affects
public health, economies, and daily life globally. It's crucial for government officials, health organizations, researchers, and the general
public to understand the dynamics of the pandemic to make informed decisions, comply with health guidelines, and support containment
efforts.

## How did you choose this problem? 
The problem was chosen due to the ongoing impact of the COVID-19 pandemic and the clear
need for improved public health response mechanisms. The availability of detailed data makes it a ripe area for applying data science
and machine learning techniques.

## Do you have any specific hypotheses? 
There are predictable patterns in the spread of COVID-19 that can be uncovered through
data analysis. At times indicators (for instance: positivity rates, mobility data, social distancing policies) can be powerful predictors of
future trends.The impact of the vaccination and variants can be specified and included into the predictive models.

# Data- Questions

## What is the data that you plan to use?
The data that we plan to use is COVID-19 Open Research Dataset (CORD-19). This dataset is a collection of
scholarly articles about COVID-19, SARS-CoV-2, and related coronaviruses. It’s designed to facilitate
research on COVID-19 by providing a corpus optimized for machine readability aiding the researchers in
gaining new insights to combat the pandemic.

## Do you currently have access to this data or do you need to collect it?
We currently have access to this data as we’re focusing on data based on COVID and its progress which
started to be collected since 2019 and is currently being recorded.

## How much effort is that data collection and can you complete it within a reasonable amount of time?
Effort Involved in working with the CORD-19 dataset is significant but manageable and we can complete
the project within the designated timeframe however it will be challenging due to the sophisticated
machine learning techniques involved, which require extensive data processing and analysis.

## Describe your data in terms of size (e.g., number of rows per table or number of images), type of data, type of features, and any other relevant details.
The size of our data has 22261 rows and 31 columns. There are floats, objects, and ints within the data.
The data includes variables such as test results, death count, increases of people who are hospitalized,
recovered patients, icu count, ventilator count, etc.

# Solution

## How do you plan to approach the problem?
### Exploratory Data Analysis (EDA): This will involve statistical summaries and visualizations to understand the distributions, trends, and patterns in the data. Feature Engineering: We will create new features that will be able to be predictive of the variables we are interested in, like growth rates, moving averages, and ratios between different metrics. Model Development: We will run diverse statistical and machine learning models that will forecast the outcomes like positive case increases, hospitalization rates, or recovery trends. 
### Validation: The models will be validated by looking at historical data to check their predictive power and accuracy.

## What is the proposed scope of your project and the next steps?
### Proposed scope: Developing a model that can predict future trends of the pandemic on a state level. Providing insights into the effectiveness of health measures and interventions. Identifying potential hotspots and predicting hospitalization needs.
### Next steps: Acquiring the latest data and any additional variables that could be relevant. Setting up a data processing pipeline. Beginning exploratory data analysis. Selecting and testing preliminary models.

## What do you envision the end result to be?
Hereby, the goal is to develop a strong predictive model or set of models which can be used as an instrument to formulate decisions on
the basis of objective data. This could mean a dashboard, report, or forecasting tool.

# What techniques do you think you will use to analyze the data?
Data Visualization, Correlation Analysis, Predictive Modeling, Data Integration, and Clustering

# Do you envision your system to be interactive or static?
The system is envisioned to be interactive, allowing users to select specific states, time frames, and metrics to view and predict trends.
This would likely be in the form of a web-based dashboard.

# What do you hope to have achieved for the Progress report?
Completed data preprocessing and a comprehensive EDA. A clear definition of the model's scope and preliminary results from initial
models. A basic prototype of the interactive system