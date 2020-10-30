# Psych Predict

**Weill Cornell Medicine**   
[Department of Population Health Sciences](https://phs.weill.cornell.edu/)  
[Division of Health Informatics](https://phs.weill.cornell.edu/research-collaboration/our-divisions/health-informatics)  
New York, NY

----
<br />__Repository Overview__: Predicting incident psychiatric hospitalizations (depression, bipolar/manic/other mood, schizophrenia, psychoses/delusional disorder) between 2012-2018 using inpatient/outpatient/ER/ambulatory electronic health record data in the OMOP data model.  
<br />

#### __Instructions for Setup__:
1. Ensure that you have the following installed on your machine:
   - [Git](https://git-scm.com/about): Distributed version-control system
   - [pyenv](https://github.com/pyenv/pyenv#installation): Python version management 
      - Python 3.7 or greater: `pyenv install 3.7.0`
   - [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv): Pyenv virtual environment plugin
   - [Poetry](https://python-poetry.org/docs/#installation): Package/Dependency Manager
2. Clone the repository by navigating to your desired directory and typing the following command into your terminal:
```
git clone https://github.com/jdeferio/psych_predict.git
```
3. Initalize the repository with the following command:
```
poetry shell
poetry install
```
<br />

---
#### __Data Collection Overview__
<br />

Script Name|Description|Data Type
:---|:---|:---
`sql_all_dx_1218.py`|Pull all patient diagnosis data between years 2012-2018 for patient population|ICD-9,  ICD-10
`sql_all_visits_1218.py`|Pull all visit data between years 2012-2018
`sql_procedures_1218.py`|Pull all procedures performed during the years 2012-2018|ICD-9, ICD-10, *CPT (_to be included / replace ICD_)
`sql_drug_exposure_1218.py`|All output medications prescribed during the 2012-2018 period|VA Class
`sql_pt_demographics.py`|Age, gender, and birthdate for the population
