import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.feature_selection import SelectKBest, RFE
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.preprocessing import FunctionTransformer,Binarizer, Imputer, LabelBinarizer, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline, make_union, FeatureUnion
from sklearn import metrics


def main(dataframe):
    return dataframe['MAIN'].values.reshape(-1,1)

def branch(dataframe):
    return dataframe['NUMBRANCH'].values.reshape(-1,1)

def hbcu(dataframe):
    return dataframe['HBCU'].values.reshape(-1,1)

def pbi(dataframe):
    return dataframe['PBI'].values.reshape(-1,1)

def women(dataframe):
    return dataframe['WOMENONLY'].values.reshape(-1,1)

def distance(dataframe):
    return dataframe['DISTANCEONLY'].values.reshape(-1,1)

def ugds(dataframe):
    return dataframe['UGDS'].values.reshape(-1,1)

def ageentry(dataframe):
    return dataframe['AGE_ENTRY'].values.reshape(-1,1)

def female(dataframe):
    return dataframe['FEMALE'].values.reshape(-1,1)

def married(dataframe):
    return dataframe['MARRIED'].values.reshape(-1,1)

def dependent(dataframe):
    return dataframe['DEPENDENT'].values.reshape(-1,1)

def mdfam(dataframe):
    return dataframe['MD_FAMINC'].values.reshape(-1,1)

def preddeg(dataframe):
    return dataframe['PREDDEG'].values.reshape(-1,1)

def columnisopred(series):
    return series[:,1:]

def highdeg(dataframe):
    return dataframe['HIGHDEG'].values.reshape(-1,1)

def control(dataframe):
    return dataframe['CONTROL'].values.reshape(-1,1)

def locale(dataframe):
#     dataframe['LOCALE'] = dataframe['LOCALE'].apply(lambda x: 21.0 if x == -3.0 else x)
    return dataframe['LOCALE'].values.reshape(-1,1)

def columnisoloc(series):
    return series[:,2:]

main_pipe = make_pipeline(FunctionTransformer(main, validate = False),
                         Imputer(strategy = 'most_frequent'))

branch_pipe = make_pipeline(FunctionTransformer(branch, validate = False),
                           Imputer())

hbcu_pipe = make_pipeline(FunctionTransformer(hbcu, validate = False),
                         Imputer(strategy = 'most_frequent'))

pbi_pipe = make_pipeline(FunctionTransformer(pbi, validate = False),
                        Imputer(strategy = 'most_frequent'))

women_pipe = make_pipeline(FunctionTransformer(women, validate = False),
                          Imputer(strategy = 'most_frequent'))

distance_pipe = make_pipeline(FunctionTransformer(distance, validate = False),
                             Imputer(strategy = 'most_frequent'))

ugds_pipe = make_pipeline(FunctionTransformer(distance, validate = False),
                         Imputer())

ageentry_pipe = make_pipeline(FunctionTransformer(ageentry, validate = False),
                             Imputer())

female_pipe = make_pipeline(FunctionTransformer(female, validate = False),
                           Imputer())

married_pipe = make_pipeline(FunctionTransformer(married, validate = False),
                            Imputer())

dependent_pipe = make_pipeline(FunctionTransformer(dependent, validate = False),
                              Imputer())

mdfam_pipe = make_pipeline(FunctionTransformer(mdfam, validate = False),
                          Imputer())

preddeg_pipe = make_pipeline(FunctionTransformer(preddeg, validate = False),
                             Imputer(),
                            LabelBinarizer(),
                            FunctionTransformer(columnisopred, validate = False))

highdeg_pipe = make_pipeline(FunctionTransformer(highdeg, validate = False),
                             Imputer(),
                            LabelBinarizer(),
                            FunctionTransformer(columnisopred, validate = False))

control_pipe = make_pipeline(FunctionTransformer(control, validate = False),
                             Imputer(),
                            LabelBinarizer(),
                            FunctionTransformer(columnisopred, validate = False))

locale_pipe = make_pipeline(FunctionTransformer(locale, validate = False),
                            Imputer(),
                           LabelBinarizer(),
                           FunctionTransformer(columnisoloc, validate = False))

fu = make_union(main_pipe,branch_pipe, hbcu_pipe, pbi_pipe,women_pipe, distance_pipe,ugds_pipe,ageentry_pipe,
               female_pipe, married_pipe, dependent_pipe, dependent_pipe, mdfam_pipe, preddeg_pipe,
               highdeg_pipe, control_pipe, locale_pipe)

test = pd.read_csv('university_test.csv')

training = pd.read_csv('university_train.csv')

fu.fit(training)

y = training['percent_on_student_loan'].values

lm = LinearRegression()
lm.fit(fu.transform(training),y)
lm.score(fu.transform(training),y)

def evaluation_transformationlm(dataset, predictions):
    dataset = dataset.join(pd.DataFrame(predictions, columns=['Prediction']))
    dataset[['id_number', 'Prediction']].to_csv('submissionlmtest.csv', index=False)
    
predictionlm = lm.predict(fu.transform(test))

evaluation_transformationlm(test, predictionlm)